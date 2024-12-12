import pickle
from txtai import Embeddings
import numpy as np
from numpy import dot
from numpy.linalg import norm
import heapq
import ultraprint.common as p

from flask import Flask, request, jsonify

app = Flask(__name__)


embedding = Embeddings() 

with open('data.pkl', 'rb') as file: 
    # Load the object 
    data = pickle.load(file)
    
with open('embedding.pkl', 'rb') as file: 
    # Load the object 
    embeddings = pickle.load(file)
    
def search(query_embedding, num_results):

    #convert to numpy array of float16
    query_embedding = np.array(query_embedding, dtype=np.float16)
    cosine_similarity = lambda x, y: dot(x, y) / (norm(x) * norm(y))

    # Calculate similarity
    similarities = []
    index_count = 0
    for vector in embeddings:
        similarity = cosine_similarity(query_embedding, vector)
        # Use negative similarity because heapq is a min-heap
        heapq.heappush(similarities, (similarity, index_count))
        if len(similarities) > num_results:
            heapq.heappop(similarities)
        index_count += 1
        #print(similarities)

    #sort the results
    similarities = sorted(similarities, reverse=True)

    # add the result from books_batches
    similarities = [{"Output":data.iloc[index].to_dict(), "Probability" :round(float(similarity), 3)} for similarity, index in similarities]

    return similarities
    
@app.route('/search', methods=['POST'])
def post_request():
    # Access JSON data from the request
    data = request.get_json()
    UserInput= data.get("query","")
    NumResults= int(data.get("results",5))
    user_embedding=embedding.transform(UserInput)
    
    return jsonify(search(user_embedding,NumResults))

if __name__ == '__main__':
    app.run(debug=True)