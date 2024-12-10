Movie Recommendation System with Streamlit Deployment
This project implements a movie recommendation system using machine learning techniques and deploys it as a user-friendly web application.

The model has been deployed as a user-friendly web application on Streamlit, accessible at https://movie-recommendation-jznjdabwtfpoepj6qurefy.streamlit.app/.

Dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
#### What it Does:
- Takes a user-provided movie title as input.
- Analyzes the movie's characteristics (genre, keywords, cast, director) and compares them to other movies in the dataset.
- Utilizes cosine similarity to identify movies with similar characteristics.
- Recommends the top 5 most similar movies to the user, along with their posters retrieved from the TMDb API.

#### How it Works:
1. **Data Preprocessing:**
    - A dataset of 4803 movies from TMDb is imported and cleaned.
    - Textual data like genre, keywords, cast, and director undergoes processing (removing spaces, stemming) for better model performance.
2. **Feature Engineering:**
    - Text data is converted into numerical representations using CountVectorizer.
    - This creates a matrix where each row represents a movie and each column represents a unique word in the dataset. The value indicates how many times that word appears in the movie's description.
3. **Similarity Calculation:**
    - Cosine similarity is applied to the vectorized data to measure the similarity between movies.
    - Movies with higher cosine similarity scores share more characteristics and are considered more relevant to the user's input.
4. **Model Deployment:**
    - The model is deployed as a web application using Streamlit.
    - Users can interact with the app through a web browser by entering a movie title.
    - The app retrieves the recommendations and displays them with their corresponding posters fetched from TMDb.

#### Benefits and Usefulness:
- **Personalized Recommendations:** By considering various movie attributes, the system recommends movies that align with the user's personal preferences.
- **Exploration and Discovery:** Users can discover new movies they might enjoy based on their existing taste.
- **Improved User Experience:** The web application interface provides a convenient and interactive way to explore movies.

#### Scalability and Future Improvements:
This project serves as a foundation for a movie recommendation system. With further development, it can be enhanced in several ways:

- **Larger Dataset:** Utilizing a more extensive dataset with additional movie information could improve recommendation accuracy.
- **Hybrid Recommendation Systems:** Combining content-based filtering (used here) with collaborative filtering (considering user preferences) could further refine recommendations.
- **User Reviews and Ratings:** Integrating user reviews and ratings could personalize recommendations based on user tastes and community trends.
- **Advanced Recommendation Techniques:** Implementing matrix factorization or deep learning approaches could unlock even more complex relationships between movies.

Overall, this project showcases the potential of machine learning for creating engaging and personalized movie recommendation systems. By continuously improving the model and incorporating user feedback, this technology can offer valuable tools for discovering new and exciting movies.