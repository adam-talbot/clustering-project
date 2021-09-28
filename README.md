# Zillow Clustering Project

---

# Table of contents

---

- [Executive Summary](#executive-summary)
    - [Project Objectives](#project-objectives)
    - [Conclusions and Takeaways](#conclusions-and-takeaways)
    - [Next Steps and Recommendations](#next-steps-and-recommendations)    
- [Data Dictionary](#data-dictionary)
- [Initial Questions](#initial-questions)
- [Formal Hypotheses](#formal-hypotheses)
- [Pipeline Stages Breakdown](#pipeline-stages-breakdown)
    - [Plan](#plan)
    - [Acquire](#acquire)
    - [Prepare](#prepare)
    - [Explore](#explore)
    - [Model and Evaluate](#model-and-evaluate)
- [Conclusion and Next Steps](#conclusion-and-next-steps)
- [Reproduce My Project](#reproduce-my-project)

---

<img src="https://1000logos.net/wp-content/uploads/2017/12/Zillow_logo_PNG2.png" alt="Zillow" title="Zillow Logo" width="400" height="200" />

---

### Executive Summary

[(Back to top)](#table-of-contents)

---

#### Project Objectives

> - Discover drivers of log error of Zestimate to determine how current model could potentially be improved
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report
> - Create modules as necessary that make my process repeateable
> - Include all work in github repo with README to provide high level overview and instructions for replication
> - Use clustering techniques as part of exploration process
> - Construct a model to predict Zestimate log error using regression techniques
> - Deliver a 4-minute, audience-appropriate presentation consisting of a high-level walkthrough of my notebook
> - Answer panel questions about your code, process, findings and key takeaways, and model

#### Conclusions and Takeaways 
> - The following subgroups had higher than average log error: 
>> - Orange County
>> - above 2,500 square feet
>> - below 250k dollars assessed value
>> - 7 - 12 total rooms
>> - cluster 4 from Cluster Model 1 (total rooms, sqft, assessed_value)
> - Best predictors identified via modeling were:
>> - assessed value
>> - latitude
>> - bedroom count
>> - above 2,500 square feet
>> - total rooms
>> - lot size
>> - livable square footage
> - Best-peforming model only slightly outperformed baseline

#### Next Steps and Recommendations
> - Manually look into more subgroups to see if model is performing poorly on specific portions of the population
> - Try more combinations of features in model to see if model performance can be improved/more drivers can be indentified
> - Leverage clustering to create subgroups for other single continuous variables
> - Try clustering on more combinations of features to see if more subgroups could be identified using algorithm
> - Look into creating individual models for subgroups with higher error mentioned above

#### Audience
> - The Zillow Data Science team

#### Project Context
> - The Zillow dataset I'm using came from the Codeup database

#### Data Dictionary

[(Back to top)](#table-of-contents)

---
| Feature                        | Description                                                                                                            | Data Type | Notes |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | --------- | ------------- |
| `bath_cnt`                  |  Number of bathrooms in home including fractional bathrooms                                                          |   float     |   Used in model    |
| `bed_cnt`                   |  Number of bedrooms in home                                                                                          |   int     |   Used in model    |
| `sqft`                      |  Calculated total finished living area of the home                                                                   |   int      |   Used in model    |
| `county`                         |  County where propety is located                                                                                |   string      |   Used in model    |
| `latitude`                  |  Latitude of property                                                                                                |   float     |   Used in model    |
| `longitude`                  |  Longitude of property                                                                                              |   float     |   Used in model    |
| `lot_sqft`                   |  Total square footage of lot                                                                                        |   int     |    Used in model  |
| `total_rooms`                    |  Total rooms in house                                                                                           |   int    |    Used in model   |
| `year_built`                    |  The year the principal residence was built                                                                      |   int    |    Used in model   |
| `assessed_value`                    |  Assessed value of property                                                                                  |   float    |    Used in model   |
| `sale_month`                    |  Month the property was sold                                                                                     |   int    |    Used in model   |
| `sale_week`                    |  Week the property was sold                                                                                       |   int    |    Used in model   |
| `_4_cluster_1`                    |  cluster 4 from Cluster Model 1 (total rooms, sqft, assessed_value)                                            |   int    |    Used in model   |
| `_more_than_2500_sf`           | Whether or not property is bigger than 2500 sqft                                                                  |   int     | Used in model   |
| `_less_than_250k`              | Whether or not assessed value is less than 250k dollars                                                           |   int     | Used in model   |
| `_7_to_12_total_rooms`           | Whether or not property has 7-12 total rooms                                                                    |   int     | Used in model   |

---
| Target | Definition | Data Type | Notes |
| ----- | ----- | ----- | ----- |
| `log_error` | Error in current Zestimate model | float | Value being predicted |

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Initial Questions

[(Back to top)](#table-of-contents)

> - Is logerror significantly different for properties in LA County vs Orange County vs Ventura County?
> - Is sqft related to log error?
> - Is assessed value related to log error?
> - Is year built related to log error?
> - Is total rooms related to log error?

#### Formal Hypotheses

[(Back to top)](#table-of-contents)

> - See notebook for formal hypotheses and statistical testing

---

### Pipeline Stages Breakdown

---

##### Plan

[(Back to top)](#table-of-contents)

- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x] Clearly define at least two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Utilize clustering to explore data.
- [x] Establish a baseline accuracy and document well.
- [x] Train various different regression models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

##### Acquire

[(Back to top)](#table-of-contents)

> - Store functions that are needed to acquire data from the database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the wrangle.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
___

##### Prepare

[(Back to top)](#table-of-contents)

> - Store functions needed to prepare the data; make sure the module contains the necessary imports to run the code. The final function should do the following:
>> - Split the data into train/validate/test.
>> - Handle any missing values.
>> - Handle erroneous data and/or outliers that need addressing.
>> - Encode variables as needed.
> - Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
> - Plot distributions of individual variables.
> - Add data dictionary to notebook that defines fields that will be used in your model and analysis
> - Identify unit measures and decide how to best scale any numeric data
___

##### Explore

[(Back to top)](#table-of-contents)

> - Answer key questions, my hypotheses, and figure out the features that can be used in a regression model to best predict the target variable. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). 
> - Explore the data using at least 1 clustering model
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Model and Evaluate

[(Back to top)](#table-of-contents)

> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 4 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

---

### Conclusion and Next Steps

[(Back to Executive Summary)](#executive-summary)

---

### Reproduce My Project

---

[(Back to top)](#table-of-contents)

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the modules (.py files), and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook