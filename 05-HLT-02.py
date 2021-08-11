import pandas as pd


# read the csv file using pd.read_csv
moviedata1 = pd.read_csv("Movie-Data.csv", index_col ="Director")

# # print out results of the observations
print(moviedata1.loc[["Ridley Scott", "Tom Ford"]])

# # read the csv file using pd.read_csv
moviedata2 = pd.read_csv("Movie-Data.csv", index_col = "Year")

# # print out results of the observations
print(moviedata2.loc[["2014"]])

# read the csv file using pd.read_csv
moviedata = pd.read_csv("Movie-Data.csv")

# # print the first 10 rows
print(moviedata[0:11])