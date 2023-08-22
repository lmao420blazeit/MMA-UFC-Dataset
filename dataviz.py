import pandas as pd
from sklearn import preprocessing


data = pd.read_csv("raw_total_fight_data.csv", sep=';')

data = data.query("win_by in ('Decision - Split', 'Decision - Majority', 'Decision - Unanimous', 'KO/TKO')")
data = data[["R_fighter", "B_fighter", "R_SIG_STR.", "B_SIG_STR.", "R_TOTAL_STR.", "B_TOTAL_STR.", "last_round", "R_TD", "B_TD", "R_SUB_ATT", "B_SUB_ATT", "Winner", "Fight_type"]]

data2 = data.copy()

# labeling winners into 0 = red, 1 = black wins
data.loc[data['Winner'] == data['R_fighter'] , "winner_label"] = "0"
data.loc[data['Winner'] == data['B_fighter'] , "winner_label"] = "1"

classifier_list = ["R_SIG_STR.", "B_SIG_STR.", "R_TD", "B_TD"]

"""Analyze significant strikes and takedowns normalized by number of rounds

Returns:
    list: SIGNIFICANT STRIKES/LAST ROUND
"""
for _classifier in classifier_list:
    data[_classifier] = data[_classifier].str.split(" of ").str[0]
    data[_classifier] = data[_classifier].astype("int32")
    data[_classifier] = data[_classifier].div(data["last_round"])
    
classifier_list = ["R_TOTAL_STR.", "B_TOTAL_STR."]

"""Compute percentage strikes hit

Returns:
    _type_: TOTAL STRIKES HITS/TOTAL STRIKES
"""

for _classifier in classifier_list:
    data[_classifier] = data[_classifier].str.split(" of ").str[0]
    data["R_TOTAL_STR.TEMP"] = data2[_classifier].str.split(" of ").str[-1]
    data[_classifier] = data[_classifier].astype("int32")
    data["R_TOTAL_STR.TEMP"] = data["R_TOTAL_STR.TEMP"].astype("int32")
    data[_classifier] = data[_classifier].div(data["R_TOTAL_STR.TEMP"])

data.drop(["R_TOTAL_STR.TEMP", "last_round", "B_fighter", "R_fighter"], axis=1, inplace=True)
import re

# Create a feature based on the weight class derived from the fight type
# Label encode the feature space
def regex_match(x): 
    i = re.search(r'[a-zA-Z]*weight[a-zA-Z]*', str(x))
    if i is None:
        return(x)
    return (i.group(0))

data["Fight_type"] = [regex_match(x) for x in data["Fight_type"]]
data["Fight_type"] = preprocessing.LabelEncoder().fit_transform(data["Fight_type"].tolist())

data["R_SIG_STR."] = preprocessing.MinMaxScaler().fit(data["R_SIG_STR."].values.reshape(-1, 1)).transform(data["R_SIG_STR."].values.reshape(-1, 1))
data["B_SIG_STR."] = preprocessing.MinMaxScaler().fit(data["B_SIG_STR."].values.reshape(-1, 1)).transform(data["B_SIG_STR."].values.reshape(-1, 1))

from sklearn.model_selection import train_test_split

data = data.dropna()
data = data.reset_index()

X_train, X_test, y_train, y_test = train_test_split(data.drop(['winner_label', "Winner"], axis=1), data["winner_label"], test_size = 0.25, random_state = 42)
