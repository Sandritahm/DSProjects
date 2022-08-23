# House Price Project

Data obtained from Kaggle: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)

I did this project to practice my newly acquired skills, and if you have any suggestions or comments, do not hesitate to contact me.

## Process:

1. [**Preprocessing**](https://github.com/Sandritahm/DSProjects/blob/6324df16bd4a769c6ca3efea7acbb9153a9fab6b/HousePriceProject/House_price_preprocessing.py):

    I used Pandas, NumPy and Scikit-Learn to preprocess the data. This includes:
    - Dealing with missing values.
    - Standardize the inputs.
    - Split the data set into training, validation and testing.
    - Saving the preprocessed datasets.

2. [**Build Neural Network Model**](https://github.com/Sandritahm/DSProjects/blob/399130a81ef808850c1ca2a553ff767b7208ed47/HousePriceProject/NN%20model.py):

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
