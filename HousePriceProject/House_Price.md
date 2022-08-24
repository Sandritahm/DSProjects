# House Price Project

Data obtained from Kaggle: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)

I did this project to practice my newly acquired skills, and if you have any suggestions or comments, do not hesitate to contact me.

## Process:

1. [**Preprocessing**](https://github.com/Sandritahm/DSProjects/blob/b6acc1fcce023310ced95873daa2931ca9e675ee/HousePriceProject/House_price_Preprocessing1.ipynb):

    I used Pandas, NumPy and Scikit-Learn to preprocess the data. This includes:
    - Checking correlation of values.
    - Dealing with missing values.
![Correlation_of_variables](https://user-images.githubusercontent.com/92321983/186543088-c9c6bf1b-dae0-4c64-a1e7-925629f16fca.png)

    1.2. [**Preparing data to feed the model**](https://github.com/Sandritahm/DSProjects/blob/9f0b96f09ce60cd1b5b9a6ee378f266395bcec00/HousePriceProject/Preparing%20data%20to%20feed%20NN.ipynb)
    - Standardize the inputs.
    - Split the data set into training, validation and testing.
    - Saving the preprocessed datasets.

2. [**Build Neural Network Model**](https://github.com/Sandritahm/DSProjects/blob/9f0b96f09ce60cd1b5b9a6ee378f266395bcec00/HousePriceProject/NN%20model.ipynb):

    - Because the problem at hand is a regression, I used the ReLu activation function, Adam optimizer and Mean Squared Error as loss functions.

After training my model, the Accuracy was approx—87% and here is a graph shows the predicted values vs the targets.

![Accuracy of the Model Predictions vs Targets](https://user-images.githubusercontent.com/92321983/186260195-f4acd91c-70a7-436f-b3e4-de5c140b6b30.png)


3. [**Preprocessing Testing Data Set for Kaggle Competition**](https://github.com/Sandritahm/DSProjects/blob/bb6753e5aa365caf03e70565e1753f39bc8499bd/HousePriceProject/House_price_preprocessing-Predictions.py):

    I repeated the same steps as with the training data set. I used Pandas, NumPy and Scikit-Learn to preprocess the data, which includes:
    - Dealing with missing values.
    - Standardize the inputs.
    - Split the data set into training, validation and testing.
    - Saving the preprocessed datasets.

4. [**Testing the Model**](https://github.com/Sandritahm/DSProjects/blob/399130a81ef808850c1ca2a553ff767b7208ed47/HousePriceProject/NN%20model.py):

    Finally, I use the prediction model to get the model's predictions for the test data provided in Kaggle.
