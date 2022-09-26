I made this as a project for the department-level optional course on Machine Learning in semester-4 of B.E.

A demo of the web app has been deployed <a href="https://anshumanrai.pythonanywhere.com">here</a>.
# Exoplanet_Detection_System
The proposed solution takes the data available from NASA's Kepler Space Telescope(this and more is available on the Mikulski archive if you're interested in scraping other data) and uses a classification algorithm to classify the observed extrasolar systems as either harboring an exoplanet or not. The method used to determine the probability of the system falling in either of the categories is based on the “transit” method that is used by astronomers where the light curve of a star is observed to detect the presence of an exoplanet in its orbit. The aim is to use multiple classification algorithms to develop different Machine Learning models and compare them and determine which model seems most apt for practical usage.
# ML Algorithm Selection
The most common classification models were implemented one by one and compared to see the efficacy of each solution. The resulting accuracies and scaling from one dataset to another was used to determine the most suitable model. The models used include Logistic regression, k-nearest neighbors, decision tree, random forest and Neural Network. The models found to have the highest accuracy were random forest and the neural network. But the scaling of Random Forest was found to be more consistent. The Neural Network did not give consistent enough results and was unstable when deployed. Random forest provided good enough results and consistency to be chosen over the other models.
# Project Structure
## Front End ##
A sample web-app created by incorporating the "conqueror template" with python's Flask framework that loads the trained model and uses it to count the number of observations with an exoplanet in the uploaded data.
## ML_Algo ##
A jupyter Notebook, used to collect, pre-process and clean data, training the different ML algorithms and saving the best model for deployment.
