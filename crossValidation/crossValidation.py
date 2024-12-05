import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier


# Read the excel file
df = pd.read_excel('data/decisionTree.xlsx')

# Data: Define Input (X) and output (y)
X = df[['Age', 'Blood_Pressure', 'Cholesterol']]
y = df['Disease']                                  


# Cross Validation: Train and test the model multiple times (5-fold)  - Increasing accuracy rate with max_depth
classifier = DecisionTreeClassifier(max_depth=1, min_samples_split=4, min_samples_leaf=2)
crossValScores = cross_val_score(classifier, X, y, cv = 5)
print(f"5-Fold Cross Validation Scores: {crossValScores}")
print(f"Mean: {crossValScores.mean():.2f}")
classifier.fit(X,y)       # Train the model with the entire dataset


# Get input from the user for prediction
print("Please enter the following infos to predict:")
age = int(input("Age: "))
bloodPressure = float(input("Blood pressure: "))
cholesterol = float(input("Cholesterol: "))


# Prepare new data and make prediction
newData = pd.DataFrame([[age, bloodPressure, cholesterol]], columns=['Age', 'Blood_Pressure', 'Cholesterol'])
guess = classifier.predict(newData)

# Output the prediction result
if guess[0] == 1:
    print("Guess: Disease has been detected!")
else:
    print("Guess: No disease.")