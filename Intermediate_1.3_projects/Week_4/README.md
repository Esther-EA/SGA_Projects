# Medical-appointment-no-show

## Project Overview
Using Python, including NumPy, Pandas and Matplotlib to investigate a data set recording from 100k medical appointments in a public hospital in May 2016 in Brazil.
The study contains several parts from data profiling, cleaning, aggregation, question-raising to data exploration and visualization as well as result interpretations and recommendations.
The principal objective was to identify the main factor(s) affecting patients’ medical appointment attendance from their’ gender, age, appointment day, the duration between the scheduled and the appointment day, SMS notification, being suffered from different maladies, locations.

## Data Sources

The primary dataset used for this analysis is the ["Medical-appointment-no-show"](https://drive.google.com/file/d/1g9z4TdO6xjJCKw0fs2mwdm7KgsHmVIrn/view?usp=sharing) data, containing detailed information about the subject data.
## Data Cleaning/Preparation

In the initial preparation phase, we performed the following tasks:

1.	Data loading and inspection.
2.	Data wrangling
3.	Data Exploratory ananlysis


## Findings
While doing EDA, it became apparent that it would make sense to look only at data where scheduling and appointment did not happen on the same day. On this reduced data set, the main findings are the following:

1. Appointments of alcoholics are skipped more frequently than the average appointments are.
  
2. Appointments of patients with hypertension or diabetes have lower no show up rate than those without the disease.
   
3. Appointments of patients on scholarship have higher no show rates than appointments without a scholarship.

4. Receiving an SMS reminder has a positive effect on no show rate, i.e. appointments with an SMS have lower no show rate than those without a reminder and in general.
Appointments of males and females have very similar no show rates.

5. No show rate decreases with age in our dataset.
