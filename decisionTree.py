import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

# load training data

jiraTicketTraining = pd.read_csv("tickets_training.csv")
inputs = jiraTicketTraining.iloc[:, :-1]
output = jiraTicketTraining.iloc[:, -1]

fitCen0 = DecisionTreeClassifier().fit(inputs, output)

#print predict
print(fitCen0.predict(inputs))

#load test data 
jiraTicketTesting = pd.read_csv("tickets_testing.csv")

inputs_test = jiraTicketTesting.iloc[:, :-1]
output_test = jiraTicketTesting.iloc[:, -1]

predicted_outputs = fitCen0.predict(inputs_test)
probabilities = fitCen0.predict_proba(inputs_test)
 
for i in range(10):
    print("Real output: ", output_test[i], "; Predicted output: ", predicted_outputs[i], "; Probability: ", probabilities[i])
