# House Price Project

Data obtained from Kaggle: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)

I did this project to practice my newly acquired skills, and if you have any suggestions or comments, do not hesitate to contact me.

## Process:

1. **Preprocessing**:
    I used Pandas, NumPy and Scikit-Learn to preprocess the data, this includes:
    - Dealing with missing values.
    - Standardize the inputs.
    - Split the data set in training, validation and testing.
    - Saving the preprocessed datasets.

2. **Build Neural Network Model**:
    - Because the problem at hand is a regression I used the ReLu activation function, Adam optimizer and Mean Squared Error as loss fucntion.

After training my model the Accuracy was 87.23 % and here a graph shown the predicted values vs the targets.
![image](https://user-images.githubusercontent.com/92321983/186258639-6f490dd8-4b40-4834-b933-77c2e9342a65.png)

3. **Preprocessing Testing Data Set for Kaggle Competition**:
    I repeated the same steps than with the training data set, I used Pandas, NumPy and Scikit-Learn to preprocess the data, this includes:
    - Dealing with missing values.
    - Standardize the inputs.
    - Split the data set in training, validation and testing.
    - Saving the preprocessed datasets.

4. **Testing the Model**
    Finally, I use the predict model to get the predictions of the model for the test data provided in Kaggle.
