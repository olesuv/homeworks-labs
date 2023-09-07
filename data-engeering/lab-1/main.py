import pandas as pd
import numpy as np

df = pd.read_csv("ranked_users_kaggle.csv")


# Basic Pandas methods
def read_csv_custom():
    # Returns full table
    return df


def custom_header():
    # Returns first n rows
    return df.head()


def custom_tail():
    # Returns last n rows
    return df.tail()


def custom_sample():
    # Return a random sample of items from an axis of object
    return df.sample()


def custom_shape():
    # Return a tuple representing the dimensionality of the DataFrame
    return df.shape


def custom_columns():
    # The column labels of the DataFrame
    return df.columns


def custom_index():
    # Returns row by index
    return df.index


def custom_dtypes():
    # Returns types of columns
    return df.dtypes


# Create sum of values from 2 columns: `CurrentRanking`, `HighestRanking`
def create_sum_column() -> None or str:
    ranking_sum: list = []
    new_column_name = "RankingSum"

    if new_column_name in df:
        return "Column with this name already exists"
    else:
        current_ranking_values = df["CurrentRanking"].values
        highest_ranking_values = df["HighestRanking"].values

        for i in range(len(current_ranking_values)):
            temp_res = current_ranking_values[i] + highest_ranking_values[i]
            ranking_sum.append(temp_res)

        df[new_column_name] = ranking_sum

    print(df)


# Indexing, Selecting & Assigning
def select_columns():
    # Select a few columns
    return df[["CurrentRanking", "HighestRanking"]]


def select_rows():
    # Select a few rows
    return df[0:5]


def select_columns_loc():
    # Select multiple columns using `loc` method
    return df.loc[:, ["CurrentRanking", "HighestRanking"]]


def select_columns_iloc():
    # Select multiple columns using `iloc` method
    return df.iloc[:, 0:2]


def select_rows_loc():
    # Select multiple rows using `loc` method
    return df.loc[[1, 2]]


def select_rows_iloc():
    # Select multiple rows using `iloc` method
    return df.iloc[[1, 2]]


def drop_columns():
    # Delete 2 columns
    return df.drop(columns=["Continent", "Country"])


def conditional_selection():
    # Conditional selection
    return df.loc[(df.Country == "Ukraine") & (df.Points > 1000)]


def set_index():
    # Change index of table
    return df.set_index(["Continent", "Country"])


if __name__ == "__main__":
    # print(read_csv_custom())
    # print(custom_header())
    # print(custom_tail())
    # print(custom_sample())
    # print(custom_shape())
    # print(custom_columns())
    # print(custom_index())
    # print(custom_dtypes())

    # create_sum_column()

    # print(select_columns())
    # print(select_rows())
    # print(select_columns_loc())
    # print(select_columns_iloc())
    # print(select_rows_loc())
    # print(select_rows_iloc())
    # print(drop_columns())
    # print(conditional_selection())
    # print(set_index())
