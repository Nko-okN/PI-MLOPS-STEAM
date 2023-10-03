from fastapi import FastAPI
import uvicorn
import json
import pandas as pd

app =FastAPI()

# load the files optimized for the functions requests
function1 = pd.read_parquet('function1.parquet')
function2 = pd.read_parquet('function2.parquet')
function3 = pd.read_parquet('function3.parquet')
function4 = pd.read_parquet('function4.parquet')
function5 = pd.read_parquet('function5.parquet')

# healthcheck
@app.get("/")
def read_root():
    """
    Healthcheck endpoint that returns a JSON response with the status "ok".
    """
    return {"status": "ok"}


# Function 1
@app.get("/PlaytimeByGenre")
def function_1(genre):
    """
    Endpoint to calculate the year with the most playtime for a given genre.

    Args:
        genre (str): The genre for which to find the year with the most playtime.

    Returns:
        dict: A dictionary containing the result with the year of most playtime for the genre.
    """
     
    if genre in function1['genres'].values:
        max_playtime = function1.loc[function1['genres'] == genre, 'playtime_forever'].max()
        year_with_max_playtime = function1.loc[function1['playtime_forever'] == max_playtime, 'year'].values[0]
        response = {f"Year with the most playtime for Genre {genre}": str(year_with_max_playtime)}
    else:
        response = "Enter a valid genre"
    return response


# Function 2
@app.get("/TotalPlaytimeByGenre")
def function_2(genre):
    """
    Endpoint to calculate the user with the most playtime and their playtime breakdown by year for a given genre.

    Args:
        genre (str): The genre for which to find the user with the most playtime.

    Returns:
        dict: A dictionary containing the user with the most playtime and their playtime breakdown by year.
    """
    if genre in function2['genres'].values:
        genre_data = function2[function2['genres'] == genre]
        total_playtime_by_user = genre_data.groupby('user_id')['playtime_forever'].sum().reset_index()
        user_with_max_playtime = total_playtime_by_user.loc[total_playtime_by_user['playtime_forever'].idxmax(), 'user_id']
        max_playtime = total_playtime_by_user['playtime_forever'].max()
        years_user_with_max_playtime = genre_data[genre_data['user_id'] == user_with_max_playtime]
        playtime_by_year = years_user_with_max_playtime.groupby('year')['playtime_forever'].sum().reset_index()
        playtime_by_year = playtime_by_year.rename(columns={'year': 'Year', 'playtime_forever': 'Playtime (hours)'})
        playtime_data = playtime_by_year.to_dict(orient='records')
        response = {f"User with the most playtime for Genre {genre}": str(user_with_max_playtime),
                    "Max Playtime": max_playtime,
                    "Playtime by Year": playtime_data}
    else:
        response = "Enter a valid genre"
    return response

# Function 3
@app.get("/Top3ItemsBySentiment")
def function_3(year):
    """
    Endpoint to find the top 3 items with the highest sentiment scores for a given year.

    Args:
        year (int): The year for which to find the top items.

    Returns:
        list: A list of dictionaries containing the top 3 items for the given year.
    """
    year = int(year)
    if year in function3['year'].values:
        year_data = function3[function3['year'] == year]
        top3_items = year_data.sort_values(by='sentiment', ascending=False).head(3)
        top3_items = top3_items.reset_index(drop=True)
        top3_items_data = top3_items['item_name'].to_dict()
        top3_items_list = [{"Rank " + str(index + 1): value} for index, value in enumerate(top3_items_data.values())]
        response = top3_items_list
    else:
        response = "Enter a valid year"
    return response


# Function 4
@app.get("/Bottom3ItemsBySentiment")
def function_4(year):
    """
    Endpoint to find the bottom 3 items with the lowest sentiment scores for a given year.

    Args:
        year (int): The year for which to find the bottom items.

    Returns:
        list: A list of dictionaries containing the bottom 3 items for the given year.
    """
    year = int(year)
    if year in function4['year'].values:
        year_data = function4[function4['year'] == year]
        bottom3_items = year_data.sort_values(by='sentiment', ascending=True).head(3)
        bottom3_items = bottom3_items.reset_index(drop=True)
        bottom3_items_data = bottom3_items['item_name'].to_dict()
        bottom3_items_list = [{"Rank " + str(index + 1): value} for index, value in enumerate(bottom3_items_data.values())]
        response = bottom3_items_list
    else:
        response = "Enter a valid year"
    return response


# function 5
@app.get("/SentimentAnalysisByYear")
def function_5(year):
    """
    Endpoint to retrieve sentiment analysis data (negative, neutral, positive) for a given year.

    Args:
        year (int): The year for which to retrieve sentiment analysis data.

    Returns:
        dict: A dictionary containing sentiment analysis data for the given year.
    """
    year = int(year)
    if year in function5['year'].values:
        year_data = function5[function5['year'] == year]
        sentiment_data = {
            "Negative": year_data['Negative'].values[0],
            "Neutral": year_data['Neutral'].values[0],
            "Positive": year_data['Positive'].values[0]
        }
        response = sentiment_data
    else:
        response = "Enter a valid year"
    return response