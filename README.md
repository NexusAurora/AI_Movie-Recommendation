
# Movie Recommendation System

This project implements a movie recommendation system using vector search and cosine similarity. The system takes user input in the form of a movie title or overview and returns the most similar movies based on their embeddings.

## Features

- Vectorized search for movie recommendations
- Cosine similarity calculation for finding similar movies
- RESTful API built with Flask
- Docker support for easy deployment

## Requirements

- Python 3.10
- Flask
- txtai
- NumPy
- Gunicorn
- Pickle

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NexusAurora/MovieApp.git
   cd MovieApp
   ```

2. Build the Docker image:

   ```bash
   docker build -t MovieApp .
   ```

3. Run the Docker container:

   ```bash
   docker run -p 8000:8000 MovieApp
   ```

## Usage

Once the application is running, you can make POST requests to the `/search` endpoint to get movie recommendations.

### Request Format

- **URL**: `http://localhost:8000/search`
- **Method**: `POST`
- **Body** (JSON):

```json
{
    "query": "Your movie title or overview",
    "results": 5
}
```

### Response Format

The response will be a JSON object containing the recommended movies and their probabilities:

```json
[
    {
        "Output": {
            "title": "Movie Title 1",
            "overview": "Overview of Movie 1"
        },
        "Probability": 0.95
    },
    {
        "Output": {
            "title": "Movie Title 2",
            "overview": "Overview of Movie 2"
        },
        "Probability": 0.92
    }
]
```

## Steps to Create the Recommendation System

1. **Import and parse dataset**: Load the dataset containing movie titles and overviews.
2. **Extract relevant data**: Keep only the title and overview, discarding other parameters.
3. **Calculate vector embeddings**: Vectorize each overview and store the embeddings.
4. **Accept user input**: Transform user input into an embedding.
5. **Find cosine similarities**: Calculate the cosine similarities between the user input embedding and the movie embeddings.
6. **Return top results**: Return the top N movies with the highest similarities.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [txtai](https://github.com/neuml/txtai) for the embeddings model.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Docker](https://www.docker.com/) for containerization.

## Author

My Name  
[My GitHub Profile](https://github.com/NexusAurora)
