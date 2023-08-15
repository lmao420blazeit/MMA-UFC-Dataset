# MMA-UFC-Dataset
MMA UFC Dataset from Kaggle 
(https://www.kaggle.com/datasets/rajeevw/ufcdata/versions/2?resource=download)

This small project started as a pet project to understand the evolution of lower body attacks in UFC. As a fan, I couldn't stop notice the rise of the calf kicks and leg checks. The question this project aims to answer is: Are calf kicks taking over modern UFC?

A way I found to answer this curiosity was to find a suitable dataset for the purpose. I was able to find a dataset from Kaggle which was parsed from the ufcstats website using beautifulsoup. The data include stats from different oponents, represented as R for red fighter and B for blue. R_ and B_ prefix signifies red and blue corner fighter stats respectively.

# Mann-Kendall test

M-K test will be used to evaluate if there is a trend in a time series.
> The Mann Kendall Trend Test (sometimes called the M-K test) is used to analyze data collected over time for consistently increasing or decreasing trends (monotonic) in Y values.

How it works:

- The null hypothesis, for this test is that there is no monotonic trend

 ## Approaches to statistically test this hypothesis:

 - Test the evolution of the total leg attacks using Mann-Kendall test
Simply gather the total leg attacks by fighter, group it by year and consider the median value.
  - This considers sazonality is non existent
  - This considers there is not effect of covariates (factors that would influence the total leg attacks such as fighter, weightclass and fighter type)
  - There is only one data point per time period (year). Considering we have multiple time periods, the median value is considered

 
