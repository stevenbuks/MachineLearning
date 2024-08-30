import pandas as pd
from sklearn.linear_model import LogisticRegression
 
# load training data
jiraTicketTraining = pd.read_csv("tickets_training.csv")
inputs = jiraTicketTraining.iloc[:, :-1]
output = jiraTicketTraining.iloc[:, -1]
 
# build logistic regression
fitCEN0 = LogisticRegression().fit(inputs, output)
 
# Print coefficients:
print("--------------------------------------------------")
print("COEFFICIENTS: {0}".format(fitCEN0.coef_.flatten()))
print("INTERCEPT: {0}".format(fitCEN0.intercept_.flatten()))
 
print(output)
print(fitCEN0.predict(inputs))
print("--------------------------------------------------")
print("")
 
# Test predictions
# load test data
jiraTicketTesting = pd.read_csv("tickets_testing.csv")
inputs_t = jiraTicketTesting.iloc[:, :-1]
output_t = jiraTicketTesting.iloc[:, -1]
 
print("--- Results from the test data ---")
 
predicted_outputs = fitCEN0.predict(inputs_t)
probabilities = fitCEN0.predict_proba(inputs_t)
 
for i in range(10):
    print("Real output: ", output_t[i], "; Predicted output: ", predicted_outputs[i], "; Probability: ", probabilities[i])
