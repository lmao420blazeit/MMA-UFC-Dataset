# MMA-UFC-Dataset
MMA UFC Dataset from Kaggle 
(https://www.kaggle.com/datasets/rajeevw/ufcdata/versions/2?resource=download)

This small project started as a pet project to understand the evolution of lower body attacks in UFC. As a fan, I couldn't stop notice the rise of the calf kicks and leg checks. The question this project aims to answer is: Are calf kicks taking over modern UFC?

A way I found to answer this curiosity was to find a suitable dataset for the purpose. I was able to find a dataset from Kaggle which was parsed from the ufcstats website using beautifulsoup. The data include stats from different oponents, represented as R for red fighter and B for blue. R_ and B_ prefix signifies red and blue corner fighter stats respectively.

 c   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   R_fighter        6012 non-null   object
 1   B_fighter        6012 non-null   object
 2   R_KD             6012 non-null   int64
 3   B_KD             6012 non-null   int64
 4   R_SIG_STR.       6012 non-null   object
 5   B_SIG_STR.       6012 non-null   object
 6   R_SIG_STR_pct    6012 non-null   object
 7   B_SIG_STR_pct    6012 non-null   object
 8   R_TOTAL_STR.     6012 non-null   object
 9   B_TOTAL_STR.     6012 non-null   object
 10  R_TD             6012 non-null   object
 11  B_TD             6012 non-null   object
 12  R_TD_pct         6012 non-null   object
 13  B_TD_pct         6012 non-null   object
 14  R_SUB_ATT        6012 non-null   int64
 15  B_SUB_ATT        6012 non-null   int64
 16  R_REV            6012 non-null   int64
 17  B_REV            6012 non-null   int64
 18  R_CTRL           6012 non-null   object
 19  B_CTRL           6012 non-null   object
 20  R_HEAD           6012 non-null   object
 21  B_HEAD           6012 non-null   object
 22  R_BODY           6012 non-null   object
 23  B_BODY           6012 non-null   object
 24  R_LEG            6012 non-null   object
 25  B_LEG            6012 non-null   object
 26  R_DISTANCE       6012 non-null   object
 27  B_DISTANCE       6012 non-null   object
 28  R_CLINCH         6012 non-null   object
 29  B_CLINCH         6012 non-null   object
 30  R_GROUND         6012 non-null   object
 31  B_GROUND         6012 non-null   object
 32  win_by           6012 non-null   object
 33  last_round       6012 non-null   int64
 34  last_round_time  6012 non-null   object
 35  Format           6012 non-null   object
 36  Referee          5980 non-null   object
 37  date             6012 non-null   object
 38  location         6012 non-null   object
 39  Fight_type       6012 non-null   object
 40  Winner           5902 non-null   object

 ## Approaches to statistically test this hypothesis:

 - Test the evolution of the total leg attacks using Mann-Kendall test
Simply gather the total leg attacks by fighter, group it by year and consider the median value.
  - This considers sazonality is non existent
  - This considers there is not effect of covariates (factors that would influence the total leg attacks such as fighter, weightclass and fighter type)
  - There is only one data point per time period (year). Considering we have multiple time periods, the median value is considered

 
