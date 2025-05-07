import numpy as np
from scipy.stats import chi2_contingency, fisher_exact
import pandas as pd

df = pd.read_csv("/Users/qianqian/profile-clustering-filterCol-combCol-2.csv")
filtered_df = df[df['cluster'] == 0]
filtered_df = filtered_df.drop(['cluster','Participant ID'], axis=1)

# Generate cross-tabs for all pairs of columns
columns = filtered_df.columns
with open("chi_square_results.txt", "w") as file:
    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):  # ensure not comparing the same pair
            file.write(f"\nCross-tab for {columns[i]} vs {columns[j]}:\n")
            crosstab = pd.crosstab(df[columns[i]], df[columns[j]])
            chi2, p, dof, expected = chi2_contingency(crosstab)
            #writing result to the txt file
            file.write("\nChi-Square Test Results:\n")
            file.write(f"Chi-Square Statistic: {chi2}\n")
            file.write(f"P-Value: {p}\n")
            file.write(f"Degrees of Freedom: {dof}\n")
            file.write(f"Expected Frequencies:\n{expected}\n")

