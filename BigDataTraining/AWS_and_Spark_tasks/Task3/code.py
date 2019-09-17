"""Runs a Spark job for calculating movie ratings for Sci-Fi and Action genres."""

if __name__ == '__main__':
    MOVIES = spark.read\
        .option('header', 'true')\
        .csv('FileStore/tables/movies.csv')
    FILTERED_MOVIES = MOVIES.filter(MOVIES['genres'].rlike('.*(Sci-Fi|Action).*(Sci-Fi|Action).*'))

    RATINGS = spark.read\
        .option('header', 'true')\
        .csv('FileStore/tables/ratings.csv')

    MOVIE_RATINGS = RATINGS.join(
        FILTERED_MOVIES, RATINGS['movieId'] == FILTERED_MOVIES['movieId'], 'inner'
    ).select(
        FILTERED_MOVIES['movieId'], FILTERED_MOVIES['title'], RATINGS['rating'].cast('float')
    )

    AVERAGE_RATINGS = MOVIE_RATINGS.groupBy(MOVIE_RATINGS['movieId'], MOVIE_RATINGS['title']).avg()

    AVERAGE_RATINGS = AVERAGE_RATINGS.select(
        AVERAGE_RATINGS['movieId'],
        AVERAGE_RATINGS['title'],
        AVERAGE_RATINGS['avg(rating)'].alias('avg_ratings')
    )

    AVERAGE_RATINGS.coalesce(1).write.parquet('FileStore/tables/average-movie-ratings.parquet')
