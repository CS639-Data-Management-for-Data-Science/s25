![Static Badge](https://img.shields.io/badge/Deadline-Apr%2023-blue)
![Static Badge](https://img.shields.io/badge/topics-data%20science%2C%20time%20series%20analysis-green)
![Static Badge](https://img.shields.io/badge/course-CS639-purple)

# P5 Time Series Analysis

* **Competition invite link: https://www.kaggle.com/t/9727942d265a48bdb9f5e317b065dc5d**
* **Github Classroom Invite for P5: https://classroom.github.com/a/VIgYrpSu**

---
# Clarification/Fixes

1. You can submit your plots separately if your notebook keeps dying on you.

---

## Learning Objectives

1. Carrying out thorough exploratory data analysis (and carry out basic feature engineering)
2. Implement simple statistical models: EMA and ARIMA (understand PACF and ACF)
3. Implement (out of the box) and contrast popular gradient boosting algorithms for time series prediction: XGBoost, LightGBM, and CatBoost
4. **[Optional]** Compete in addition to time-attack deadlines - for fun and handling the constant technological innovation mental burden
5. Another main objective of this assignment is to go through a typical data analysis/science project's life cycle: <img src="assets/lifecycle.png" width="400" height="400" align="center">

---

## Setup

1. Create a Kaggle account *with your wisc email*, if you don't have one already. Signup here: https://www.kaggle.com/
2. Join the Kaggle competition: https://www.kaggle.com/t/9727942d265a48bdb9f5e317b065dc5d
3. You can work on implementing your code on your local machines or use the GCP VMs
4. Submit the CSV generated to the competition.

---
## Helper Utilities. Read the Function names at least so that you are not re-writing code(Refer to the helper.py)

* **make_submission**: Helps you convert your predictions to competition submission ready files.
* **rmsle**: Implementation of the metric used to evaluate your score on the leaderboard.
* **lgbm_rmsle**: Definition that can be used to do train-val type training while printing metric scores.
* **data import**: Imports the necessary files into the notebook
* **preprocess_holidays**: Performs some necessary cleaning on the holiday dataset
* **preprocess_test_train**: Performs some necessary cleaning on the test and train dataset

---


## Section 1: EDA & Feature Engineering

Concepts: Plotting, correlations, data imputation, leakage, one-hot encoding.

---

**Please perform the following preprocessing steps before you get start answering the questions.**

- Merge the test and train dataset
- save this new dataframe as merged_df

### Analyzing the feature: Transactions (Correlations and average trends)

**Q1. Left join transaction to merged_df and then print the *Spearman Correlation* between Total Sales and Transactions for a particular store on a particular date. [0.1 Points]**

1. Start by performing the left join on date & store_nbr
2. Group merged_df on date & store_nbr
3. Look at the resulting dataframe after the step 1. You're trying to get total sales and average transactions!

**Q2. Plot an 'ordinary least squares' trendline between transactions and sales to verify the spearman correlation value in Q1. [0.1 Points]**

**Q3. Plot these **line** charts in the notebook:**

1. Transactions vs Date (all stores color coded in the same plot)
2. Average monthly transactions
3. Average Transactions on the days of the week

**What observations can you draw from these plot? [0.3 Points]**

1. X-axis should only display years (2013, 2014, 2015, 2016 and 2017) for plot A. Month for plot B and days of the week for plot C.
2. A, B and C are single plots. Use plotly.

**NOTE:** Your plots should be rendered in the notebook for you to receive credit.

---

### Analyzing the feature: Oil (Data Imputation, Correlation can be deceptive)

**Q4. Use pandas' in-build (linear) interpolation to impute the missing oil values then (plot) overlay the imputed feature over the original.**

* Learn to use [NumPy's where](https://numpy.org/doc/stable/reference/generated/numpy.where.html) and [Pandas' interpolate](https://pandas.pydata.org/docs/reference/api/pandas.Series.interpolate.html)

**Q5. Again, left join the interpolated oil values on the dataframe from Q1 and report the spearman correlation between `oil and sales` and `oil and transactions`. [0.1 Points]**

- Use the hints from Q1
- Look at the resulting dataframe after the step 1. You're trying to get total sales and average transactions!

**Q6. Report the top-3 highest negative correlations between `oil and sales of a particular product family`. Now think whether oil should be discarded as a feature? [0.1 Points]**

* Always think intuitively as well: Oil should affect an oil-dependent country! The problem statement/dataset description also said that.
* Maybe not all products are affected by oil change. People still need to eat. So bread might not be affected so much!
* If correlation values don't align with your intuition or facts, maybe you're hypothesis or dataset view is wrong?

**Q7. Implement the One hot encode function**

### Section 2: Statistical Models

**Recommendation:** Even though the assignment does not ask for plots. Visualizing the prediction helps build intuition.

**Q8. Make a submission using an exponential moving average (EMA) model for each of the product families per store.**

* ```each of the product families per store``` means you will have to train 1782 models (should take ~7 mins to fit on CPU)
* Use the make_submission function to generate a csv file named as ```"EMA_results.csv"```

Unlike Simple Moving Average and Cumulative Moving Average (concepts you should also be familiar with), Exponential Moving Average gives more weight to the recent observations and as a result of which, it can be a better model or better capture the movement of the trend (and is also faster).
(EMA's reaction is directly proportional to the jumps in data unlike other MA methods)

**Q9. What are PACF and ACF? Analyze the time series by plotting the ACF and PACF with lag 20 for total sales value per day**

* Briefly describe the what the plots indicate and talk about the stationary nature of the data

**Q10. Perform the ADF test on the difference series for a valid ARIMA model. Then fit an ARIMA/SARIMA model with the appropriate p, d and q values. Make a submission.**

* Print the ADF statistic and corresponding p-value.
* Print the summary after fitting the model. (Should have Jarque-Bera, Ljung-Box, Heteroskedasticity, Skew and Kurtosis) $\rightarrow$ lookup what these tests mean!
* Are the MA and AR coefficients statistically signficant?
* Make predictions for next 15 days.
* Save the predictions as ```"ARIMA_results.csv"```

---

### FYI

Comparison Summary Table
| Model                   | Use Case                  | Advantages                                              | Limitations                                          |
|-------------------------|---------------------------|---------------------------------------------------------|------------------------------------------------------|
| **ARIMA**               | Complex time series data with autocorrelation | Handles trends, seasonality, noise                      | Requires stationary data, parameter tuning           |
| **EMA**                 | Short-term trend analysis | Easy to implement, recent data weighted more            | Limited forecasting capability, doesn't handle seasonality well |
| **Linear Regression**   | Linear relationships      | Simple, interpretable, works with multiple predictors   | Assumes linearity, limited in non-stationary series   |


---

## Section 3: Gradient Boosted Tree Methods

**NOTE 1:** Do not worry/get hung up on Q12-14 trying to find the best hyperparameters by hit and trial. Q15 will show you a method that finds (sub) optimal hyperparamters automatically.

**NOTE 2:** You should be using all features so far except `id` for the subsequent submission questions.

**Q11. Define a validation set. What will be the most appropriate time period for this validation set?**

<details>
  <summary>
    Hint:
  </summary>
  <p>
    The validation set should ideally reflect the entire distribution of sales to make robust and generalizable models. However, since the test set is also biased towards a time-period here, the validation set should represent the test set well to achieve a lower metric score. <b>This is a big reason why models from Kaggle are often over-fitted and not deployable unless the competition hosts come up with extensive testing sets and/or metrics.</b>
  </p>
</details>


**Q12. Make a submission using LightGBM**


**Q13. Make a submission using a CatBoost model**


**Q14. Make a submission using an XGBoost model.**


**Q15. Use optuna for automatic hyperparameter optimization for your models in questions 10, 11 and 12  to achieve a lower RMSLE.**

* Recommendation: Try 10 trials for each method.

**Q16. Which out of the three Catboost vs LightGBM vs XGBoost provides the best score? Why do you think this model is more suited to this dataset/problem?**

## [OPTIONAL] Does competition get the blood flowing for ya? 🤠 Then climb the ranks! Potential to earn extra credit*

*To earn *extra credit 💰*, achieve a *top-3 position* on the leaderboard. If your total score points is closer to a better letter grade, we'll use this ranking to boost the letter grade.

<details>
  <summary>
    Hint 1:
  </summary>
  <p> Having a solid/robust/represenatative of the underlying (true) distribution cross-validation set will help you more than you can imagine. Advice applicable till the end of times. </p>
</details>

<details>
  <summary>
    Hint 2:
  </summary>
  <p>Most Kaggle competitions are won by using an <b>ensemble</b> of methods. Try different variations! </p>
</details>

<details>
  <summary>
    Hint 3:
  </summary>
  <p>N-BEATS is a great deep learning based method. Try it out!</p>
</details>

---

## Submission

Download your final Kaggle notebook and upload it on your github repo for p5.

**NOTE: For this assignment, the TAs will grade manually. There is NO autograder.**

---

## Think Data Science is dying?

### Hear it from a Kaggle Grand Master himself on the state of current research for AI with data science:

![Relevant](assets/relevant.png)

