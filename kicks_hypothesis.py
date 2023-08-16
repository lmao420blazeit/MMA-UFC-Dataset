import pandas as pd
import pymannkendall as mk

data = pd.read_csv("raw_total_fight_data.csv", sep=';')
print(data.info())
#data = data[["date", "R_LEG", "B_LEG"]]


# preprocessing data

data["date"] = data["date"].str.strip().str[-4:] # use string manipulation to get last 4 digits instead of date methods
data["R_LEG_HITS"], data["R_LEG_TOTAL"] = data["R_LEG"].str.split(" of ", expand=False).str[0], data["R_LEG"].str.split(" of ", expand=False).str[1] #
data["B_LEG_HITS"], data["B_LEG_TOTAL"] = data["B_LEG"].str.split(" of ", expand=False).str[0], data["B_LEG"].str.split(" of ", expand=False).str[1] #
data["TOTAL_LEG"] = data["B_LEG_TOTAL"] + data["R_LEG_TOTAL"]

median = data.groupby("date")[["TOTAL_LEG"]].median()
print(median.iloc[::-1])

print(mk.original_test(median.iloc[::-1], alpha=0.05)) # making sure the order is from the latest to the newest
