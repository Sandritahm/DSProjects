# Nobel Laureates EDA

## Project Overview
- Performed an Exploratory Data Analysis in the dataset.
- Dataset was obtained from Kaggle: https://www.kaggle.com/datasets/gauravarora1091/nobel-laureates-from-1901-to-2022
- __Python Version:__ 3.9
- __Packages:__ pandas, matplotlib, seaborn

## Data Cleaning
The data came in 6 separate csv files, for purpose of the analysis:
- Modify the country field by selecting the first country mentioned, because some Laureated mentioned two nationalities.
- In some files, the document contains more information, so I drop the extra columns, keeping just Year, Laureate, Country, Rationale and Field.
- Concatenated the csv files resulting in a single dataset with 988 rows.

## EDA
- The number of Laureates per field showed that the field with more prizes in the medicine field followed closely by Physics.
![image](https://user-images.githubusercontent.com/92321983/196229808-be11e635-515c-41cd-ae3f-267c6cd8539b.png)

- The number of Laureates per country showed that the United States accounts for 35% of the values of the dataset followed by the United Kingdom accounting for 11%.
Two countries account for 46% of the dataset.
![image](https://user-images.githubusercontent.com/92321983/196230262-5cec0e9d-41f7-4de2-9701-cc31bc6a9f8a.png)

- By selecting the top 10 countries with more Laureates, a horizontal bar chart was plotted that showed the distribution of the prizes among the countries and by fields.
Here we see how the United States is ahead of all the countries.
![image](https://user-images.githubusercontent.com/92321983/196233083-77672c7f-ca7f-46b1-832c-2e3c01ecacfd.png)

- Similarly, I used the same type of graph by separateing by Field and then Country, from the graph we can see that the United States has more prizes in almost all the fields. However, France has more quantity of prizes in the field of Literature.
![image](https://user-images.githubusercontent.com/92321983/196234214-98d023ee-9919-41f5-ae6b-80d0f8e195ca.png)

[Go Back](https://github.com/Sandritahm/DSProjects/blob/95ee29e002b9b9a2a38f126b5d04610a22f3dee6/README.md)
