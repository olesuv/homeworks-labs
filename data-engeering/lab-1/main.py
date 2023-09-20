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


def value_count():
    # Returns unique values in the index
    return df.value_counts()


def unique():
    # Returns unique values from list
    temp_list = df["Country"].values
    return pd.unique(temp_list)


def sum():
    # Returns sum of selected axis
    return df["Points"].sum()


def mean():
    return df["Points"].mean()


def double_points(points: int):
    return points ** 2


def map():
    df["Country"] = df["Country"].map("Ukraine".format)
    return df


def map_lambda():
    return df["Points"].map(lambda x: x**2)


def sort_ascending():
    return df["Points"].sort_values()


def sort_descending():
    return df["Points"].sort_values(ascending=False)


def grouping_1_column():
    return df.groupby("Country")["Points"].max().reset_index()


def grouping_2_columns():
    return df.groupby(["Country", "RegisterDate"])["Points"].max().reset_index()


def grouping_3_columns():
    return df.groupby(["RegisterDate", "Country", "Continent"])["Points"].max().reset_index()


def grouping_agg():
    return df.groupby("Country").agg({"Points": "max"})


def filter():
    return df[df["Points"] > 1500]


def filter_by_country():
    return df[df["Country"] == "Ukraine"]


def query():
    return df.query('Country == "Ukraine" and Points >= 1500')


def query_python():
    return df.query('Country == "Ukraine" and Points >= 1500', engine='python')


def multiple_loc():
    return df.loc[(df["Country"] == "Ukraine") & (df["Points"] >= 1500)]


def multiple_map():
    value_mapping = {1000: "Low", 2000: "Medium", 3000: "High"}
    return df["Points"].map(value_mapping)


def multiple_paramaters_sort_values():
    print(df.sort_values(by="Points", ascending=True, ignore_index=True))
    print(df.sort_values(by="Points", ascending=False))


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

    # print(value_count())
    # print(unique())
    # print(sum())
    # print(mean())
    # print(map())
    # print(map_lambda())

    # print(sort_ascending())
    # print(sort_descending())
    # print(grouping_1_column())
    # print(grouping_2_columns())
    # print(grouping_3_columns())
    # print(grouping_agg())
    # print(filter())
    # print(filter_by_country())
    # print(query())
    # print(query_python())

    # print(multiple_loc())
    # print(multiple_map())

    multiple_paramaters_sort_values()
