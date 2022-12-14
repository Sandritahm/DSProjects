# Data Science Projects

## [Austing Animal Center](AustingAnimalCenter.md)

>__Libraries__:
  * Pandas
  * Numpy
  * MatPlotLib
  * Sklearn
  
>**Process**: 
  1. Cleaning and preprocessing the data.
  2. Defining the inputs: From the 41 columns in the data I use 10 in the analysis.
      * animal_type
      * breed
      * color
      * intake_condition
      * intake_type
      * sex_upon_intake
      * age_upon_intake_(days)
      * time_in_shelter_days
  3. Defining the output: 
      * outcome_type: "Adopted" or "Not Adopted"
 
> **Methods**:

#### [Decision Tree](https://github.com/Sandritahm/DSProjects/blob/d59baabd64b287718d22c532636031606dfe6ae0/Austing%20Animal%20Center-Decision%20Tree-Final.ipynb)
![image](https://user-images.githubusercontent.com/92321983/185189607-dc595577-0158-4733-9915-68d5d6ad03b7.png)

Report:
|             | precision  | recall | f1-score | support|
|-------------|:----------:|:------:|:--------:|:------:|
|           0 |     0.89   |  0.75  |   0.81   |  9351  |
|           1 |     0.71   |  0.87  |   0.78   |  6581  |
|    accuracy |            |        |   0.80   | 15932  |
|   macro avg |     0.80   |  0.81  |   0.80   | 15932  |
|weighted avg |     0.82   |  0.80  |   0.80   | 15932  |
