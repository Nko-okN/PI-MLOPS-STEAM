<p align=center>

# <h1 align=center> **INDIVIDUAL PROJECT - STEAM** </h1>

# <h1 align=center> **`Nicolas Aranda`** </h1>

</p>

Welcome to my first individual project in the labs stage! In this assignment, I am working in the role of an **MLOps Engineer**.

<hr>  

## Context

I have been provided with three .json filesthat were scraped from Steam, an international video game platform. The task is to create an API to query the database.

## Role Played

I started by working as a **Data Engineer**, performing an ETL (Extract, Transform, Load) process on the three files. I cleaned the data by handling null values and duplicates, normalized formats. According to the requirements, I formatted the final datasets to perform the requested queries.


## Proposed Work: Company Requirements

**Transformations**: The transformations were performed using Python Pandas.

**Sentiment Analysis**: For better understanding, I rated the reviews on a scale: '0' for negative, '1' for neutral, and '2' for positive. This transformation was carried out using libraries such as nltk with StopWord, re to prepare the texts, and TextBlob for text analysis.

**API Development**: I exposed the company's data using **FastAPI**. The requested queries are as follows:

+ def **PlaytimeByGenr(*genre*: str)**:
   Endpoint to calculate the year with the most playtime for a given genre.

    Args:
        genre (str): The genre for which to find the year with the most playtime.

    Returns:
        dict: A dictionary containing the result with the year of most playtime for the genre.
  
Example of return: {"Year with the most played hours for Genre X": 2013}

+ def *TotalPlaytimeByGenre(*genre*: str)**:
Endpoint to calculate the user with the most playtime and their playtime breakdown by year for a given genre.

    Args:
        genre (str): The genre for which to find the user with the most playtime.

    Returns:
        dict: A dictionary containing the user with the most playtime and their playtime breakdown by year.


+ def **Top3ItemsBySentiment(*year*)**:
Endpoint to find the top 3 items with the highest sentiment scores for a given year.

    Args:
        year (int): The year for which to find the top items.

    Returns:
        list: A list of dictionaries containing the top 3 items for the given year.
    

+ def **/Bottom3ItemsBySentiment(*year*: int)**:
Endpoint to find the bottom 3 items with the lowest sentiment scores for a given year.

    Args:
        year (int): The year for which to find the bottom items.

    Returns:
        list: A list of dictionaries containing the bottom 3 items for the given year.
   

+ def **SentimentAnalysisByYear(*year*: int)**:
 Endpoint to retrieve sentiment analysis data (negative, neutral, positive) for a given year.

    Args:
        year (int): The year for which to retrieve sentiment analysis data.

    Returns:
        dict: A dictionary containing sentiment analysis data for the given year.
    
Link to the [API]([(https://steam-project-api-f98r.onrender.com])

## EDA (Exploratory Data Analysis)

**Exploratory Data Analysis**: With clean data, I conducted EDA, searching for relationships between games using a correlation matrix, identifying patterns, creating rankings of the most played games, and the quantity and types of reviews. For this purpose, Python libraries such as matplotlib and seaborn were used.



