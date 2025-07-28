Repository status = Archived

# TPCDataAnalysis

This Master thesis presents a Learning Analytics (LA) study conducted on RETOMadrID. The goal is to improve the platform by understanding students’ behavior using modern machine learning (ML) and data analysis techniques.

this work demonstrated how ML can support personalized educational interventions. Furthermore, it showcased the effective integration of Python and Elixir within Livebook, contributing a practical, reproducible work-flow for future data analysis in online education environments.

This repository contains a livebook that handles the following csv files: answers.csv, events.csv, participation.csv. These CSV files can be directly downloaded from RETOMadrID platform.

## RETOMadrID
The project ’Reequilibrio Territorial en Madrid con Inclusión Digital’, also known as RETOMadrID, is conducted in collaboration with the local Government of the Region of Madrid and the Technical University of Madrid (Universidad Politécnica de Madrid). The initiative addresses the growing need for digital skills to carry out many essential tasks in our daily life, such as booking medical appointments, staying in touch with family, or simply accessing any online services. The goal is to ensure people situated in rural areas are not left behind in the current digital era, or anyone within the target audience, by providing them with essential computer skills from scratch. The target audience includes adults over 18 living in rural areas within the region of Madrid, with a particular focus on women in vulnerable situations, the unemployed, elderly people, cultural minorities, and anyone lacking computer skills.

## Python Scripts
There are some python script in this repository. You can easily combine them into Livebook session, using Pythonx module in Elixir. Please see an example in "decisionTree.livemd" for an example.

## Future Work
1. Clustering algorithm improvement.
2. Apart from Logistic Regression, other models can be picked.
3. Work on identifying early at-risk students, by considering the constrains found from the logistic regression results. Please see chapter 5 of the PDF for an idea on how to proceed from the current work.
4. Identify what can be do in order to reengage those inactive students, since we found out how inactive students brings a negative impact on student engagement and student course completion.


