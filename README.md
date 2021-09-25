# Zillow Regression Project

<!-- Add buttons here -->

![GitHub release (latest by date including pre-releases)](https://img.shields.io/badge/release-draft-yellow)
![GitHub last commit](https://img.shields.io/badge/last%20commit-Sep%202021-green)

---

# Table of contents
<!-- Add a table of contents for your project -->

- [Project Title](#project-title)
- [Executive Summary](#executive-summary)
- [Table of contents](#table-of-contents)
- [Data Dictionary](#data-dictionary)
- [Data Science Pipeline](#data-science-pipline)
    - [Acquire](#acquire)
    - [Prepare](#prepare)
    - [Explore](#explore)
    - [Model](#model)
    - [Evaluate](#evaluate)
- [Conclusion](#conclusion)
- [Given More Time](#given-more-time)
- [Reproduce My Project](#recreate-this-project)
- [Footer](#footer)

---

<img src="https://1000logos.net/wp-content/uploads/2017/12/Zillow_logo_PNG2.png" alt="Zillow" title="Zillow Logo" width="400" height="200" />

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Project Summary

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> **Conclusions/Takaways:**
> - Best predictors discovered were...
> - Best-peforming model outperformed baseline and increased R^2 value by...

> **Next Steps:**
> - Improve model performance by...
>> - ...

#### Project Objectives
> - Discover drivers of log error of Zestimate to determine how current model could potentially be improved
> - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report
> - Create modules (acquire.py, prepare.py) that make my process repeateable
> - Include all work in github repo with README to provide high level overview and instructions for replication
> - Use clustering techniques as part of exploration process
> - Construct a model to predict Zestimate log error using regression techniques
> - Deliver a 4-minute, audience-appropriate presentation consisting of a high-level walkthrough of my notebook
> - Answer panel questions about your code, process, findings and key takeaways, and model

#### Business Goals
> - Find drivers Zestimate log error
> - Construct a ML regression model that accurately predicts Zestimate log error
> - Document process well enough to be presented or read like a report

#### Audience
> - The Zillow Data Science team

#### Project Context
> - The Zillow dataset I'm using came from the Codeup database


#### Data Dictionary
[(Back to top)](#table-of-contents)

---
| Feature                        | Description                                                                                                            | Data Type | Notes |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | --------- | ----- |
| `bathroomcnt`                  |  Number of bathrooms in home including fractional bathrooms                                                            |   float     |   Used in model    |
| `bedroomcnt`                   |  Number of bedrooms in home                                                                                            |   int     |   Used in model    |
| `calculatedfinishedsquarefeet` |  Calculated total finished living area of the home                                                                     |     int      |   Used in model    |
| `fips`                         |  Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS\_county\_code for more details |     string      |   Used in model    |
| `propertylandusetypeid`        |  Type of land use the property is zoned for                                                                            |      int     |    Used to filter properties from database   |
| `yearbuilt`                    |  The Year the principal residence was built                                                                            |       int    |    Used in model   |
| `taxamount`                    | The total property tax assessed for that assessment year                                                               |      float     |    Used to calculate tax rates by county   |

---
| Target | Definition | Data Type | Notes |
| ----- | ----- | ----- | ----- |
| `log_error` | Error in current Zestimate model | float | Value being predicted |

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### Initial, Informal Hypotheses
> - Add the ones that I end up exploring from the long list I have already created

#### Formal Hypotheses

>  **Hypotheses (Correlation Tests):**
> - alpha = .05

> Null Hypotheses:
> 1. H_0: 

> Alternative Hypotheses:
> 1. H_a: 

> **Conclusions:**
> 1. 

> **Hypotheses (Mann-Whitney Tests):** 
> - alpha = .05

> Null Hypotheses:
> 1. H_0: 

> Alternative Hypotheses:
> 1. H_a: 

> **Conclusions:**
> 1. 

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>
[(Back to top)](#table-of-contents)

##### ***Plan***
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

##### Plan -> ***Acquire***
> - Store functions that are needed to acquire data from the database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
> - The final function will return a pandas DataFrame.
> - Import the acquire function from the wrangle.py module and use it to acquire the data in the Final Report Notebook.
> - Complete some initial data summarization (`.info()`, `.describe()`, `.value_counts()`, ...).
___

##### Plan -> Acquire -> ***Prepare***
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

##### Plan -> Acquire -> Prepare -> ***Explore***
> - Answer key questions, my hypotheses, and figure out the features that can be used in a regression model to best predict the target variable. 
> - Run at least 2 statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
> - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). 
> - Explore the data using at least 1 clustering model
> - Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Plan -> Acquire -> Prepare -> Explore -> ***Model***
> - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 4 different models. Document these steps well.
> - Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
> - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
> - Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
> - Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
> - Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.
___

##### Plan -> Acquire -> Prepare -> Explore -> Model -> ***Deliver***
> - Introduce myself and my project goals at the very beginning of my presentation.
> - Summarize my findings at the beginning like I would for an Executive Summary.
> - Walk Zillow Data Science Team through the analysis I did to answer my questions and that lead to my findings. (Visualize relationships and Document takeaways.) 
> - Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.
> - Finish with key takeaways, recommendations, and next steps and be prepared to answer questions from the data science team about your project.

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>
[(Back to top)](#table-of-contents)

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download the wrangle.py, evaluate.py, explore.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook