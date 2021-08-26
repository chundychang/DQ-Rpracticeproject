# Screen 459.3: A Different App Structure
# In the line below, import the shiny library so that it's available
library(shiny)
# in both ui.R and server.R



# Screen 459.5: Data Introduction And Cleaning
# In the lines below, import the hospital_los.csv file and process it according
# to the screen instructions. Categorical variables should be converted into 
# factor
library(readr)
library(tidyverse)
library(DT)
heart <- read.csv("www/heart.csv")
colnames(heart)
str(heart)

# cp = chest pain type (4 values); trestbps = resting blood pressure; chol = serum cholestorol in mg/dl; fbs = fasting blood sugar > 120 mg/dl;
# restecg = resting electrocardiographic results (values 0,1,2); thalach = maximum heart rate achieved; exang = exercise induced angina
# oldpeak = ST depression induced by exercise relative to rest; slope = slope of peak exercise ST segment; ca = number of major vessels (0-3) colored by flourosopy
# thal: 3 = normal, 6 = fixed defect, 7 = reversable defect

library(dplyr)
heart_convert <- heart %>%
  mutate(sex=as.factor(sex),
         cp=as.factor(cp),
         restecg=as.factor(restecg),
         exang=as.factor(exang),
         ca=as.factor(ca),
         thal=as.factor(thal))
str(heart_convert)
heart_convert <- heart_convert %>%
  rename(
    age=ï..age
  )
library(ggplot2)
