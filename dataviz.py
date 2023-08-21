import pandas as pd

data = pd.read_csv("raw_total_fight_data.csv", sep=';')

data = data.query("win_by in ('Decision - Split', 'Decision - Majority', 'Decision - Unanimous', 'KO/TKO')")
data = data[["R_fighter", "B_fighter", "R_SIG_STR.", "B_SIG_STR.", "R_TOTAL_STR.", "B_TOTAL_STR.", "last_round", "R_TD", "B_TD", "R_SUB_ATT", "B_SUB_ATT", "Winner", "Fight_type"]]

data2 = data.copy()

# labeling winners into 0 = red, 1 = black wins
data.loc[data['Winner'] == data['R_fighter'] , "winner_label"] = "0"
data.loc[data['Winner'] == data['B_fighter'] , "winner_label"] = "1"

data["R_SIG_STR."] = data["R_SIG_STR."].str.split(" of ").str[0]
data["R_SIG_STR."] = data["R_SIG_STR."].astype("int32")
data["R_SIG_STR."] = data["R_SIG_STR."].div(data["last_round"])


data["B_SIG_STR."] = data["B_SIG_STR."].str.split(" of ").str[0]
data["B_SIG_STR."] = data["B_SIG_STR."].astype("int32")
data["B_SIG_STR."] = data["B_SIG_STR."].div(data["last_round"])

data["R_TD"] = data["R_TD"].str.split(" of ").str[0]
data["R_TD"] = data["R_TD"].astype("int32")
data["R_TD"] = data["R_TD"].div(data["last_round"])

data["B_TD"] = data["B_TD"].str.split(" of ").str[0]
data["B_TD"] = data["B_TD"].astype("int32")
data["B_TD"] = data["B_TD"].div(data["last_round"])

data["R_TOTAL_STR."] = data["R_TOTAL_STR."].str.split(" of ").str[0]
data["R_TOTAL_STR.TEMP"] = data2["R_TOTAL_STR."].str.split(" of ").str[-1]
data["R_TOTAL_STR."] = data["R_TOTAL_STR."].astype("int32")
data["R_TOTAL_STR.TEMP"] = data["R_TOTAL_STR.TEMP"].astype("int32")
data["R_TOTAL_STR."] = data["R_TOTAL_STR."].div(data["R_TOTAL_STR.TEMP"])

data["B_TOTAL_STR."] = data["B_TOTAL_STR."].str.split(" of ").str[0]
data["B_TOTAL_STR.TEMP"] = data2["B_TOTAL_STR."].str.split(" of ").str[-1]
data["B_TOTAL_STR."] = data["B_TOTAL_STR."].astype("int32")
data["B_TOTAL_STR.TEMP"] = data["B_TOTAL_STR.TEMP"].astype("int32")
data["B_TOTAL_STR."] = data["B_TOTAL_STR."].div(data["B_TOTAL_STR.TEMP"])

data.drop(["R_TOTAL_STR.TEMP", "B_TOTAL_STR.TEMP", "Winner", "last_round", "B_fighter", "R_fighter"], axis=1, inplace=True)
import re

#data["Fight_type"] = data["Fight_type"].apply(re.match("[a-zA-Z]*weight[a-zA-Z]*"))
data["Fight_type"] = [re.match(r'[a-zA-Z]*weight[a-zA-Z]*', str(x)) for x in data["Fight_type"]]

from sklearn import preprocessing
print(len(data["Fight_type"].unique()))
data["Fight_type"] = preprocessing.LabelEncoder().fit_transform(data["Fight_type"].tolist())

print(data.head())

"""
PREDICTORS


"""