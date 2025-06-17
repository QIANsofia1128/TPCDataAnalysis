# import numpy as np
# from scipy.stats import chi2_contingency, fisher_exact
# import pandas as pd

# df = pd.read_csv("/Users/qianqian/profile-clustering-filterCol-combCol-2.csv")
# filtered_df = df[df['cluster'] == 0]
# filtered_df = filtered_df.drop(['cluster','Participant ID'], axis=1)

# # Generate cross-tabs for all pairs of columns
# columns = filtered_df.columns
# with open("chi_square_results.txt", "w") as file:
#     for i in range(len(columns)):
#         for j in range(i + 1, len(columns)):  # ensure not comparing the same pair
#             file.write(f"\nCross-tab for {columns[i]} vs {columns[j]}:\n")
#             crosstab = pd.crosstab(df[columns[i]], df[columns[j]])
#             chi2, p, dof, expected = chi2_contingency(crosstab)
#             #writing result to the txt file
#             file.write("\nChi-Square Test Results:\n")
#             file.write(f"Chi-Square Statistic: {chi2}\n")
#             file.write(f"P-Value: {p}\n")
#             file.write(f"Degrees of Freedom: {dof}\n")
#             file.write(f"Expected Frequencies:\n{expected}\n")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Load and filter the data
df = pd.read_csv("/Users/qianqian/profile-clustering-filterCol-combCol-2.csv")
#filtered_df = df[df['cluster'] == 0]
filtered_df = df.drop(['Participant ID', 'cluster'], axis=1)

# Prepare a matrix to store p-values
filtered_df = filtered_df.rename(columns={
    'Teniendo en cuenta el número de personas que viven en su hogar, y la cantidad de ingresos que entran en su hogar, ¿de cuántos euros mensuales dispone por persona? Un rango aproximadamente. No hace falta que sea exacto': 'Average income per family member',
    '¿Cuál es el nivel más alto de estudios que ha cursado usted?': 'highest education level',
    '¿Cuál es su situación laboral actual?' : 'labor situation',
    '¿Cómo se identifica?': 'gender',
    '¿En qué continente está su país de nacimiento?' : 'birth continent',
    '¿En qué rango de edades está su edad?' : 'age',
    '¿Entiende la lengua española?' : 'spanish level',
    '¿Tiene usted algún tipo de dificultad para usar el ratón o el teclado con las manos?' : 'dificulty using mouse or keyboard',
    '¿Tiene usted algún tipo de dificultad para ver o leer en pantallas digitales?' : 'dificulty reading/viewing screen',
    '¿Tiene usted personas a su cargo que dependan de usted para asegurar su bienestar (hijos/as, padres, personas dependientes por ejemplo con discapacidad, etc)?' : 'people who need to be take case of',
    'Educación más alta de padres' : 'highest parental education level'
})
columns = filtered_df.columns
print(columns)
pval_matrix = pd.DataFrame(np.ones((len(columns), len(columns))), 
                           index=columns, columns=columns)

# Fill the matrix with Chi-square test p-values
for i in range(len(columns)):
    for j in range(i + 1, len(columns)):
        crosstab = pd.crosstab(filtered_df[columns[i]], filtered_df[columns[j]])
        try:
            chi2, p, dof, expected = chi2_contingency(crosstab)
        except ValueError:
            p = np.nan  # Handle cases where the test fails
        pval_matrix.iloc[i, j] = p
        pval_matrix.iloc[j, i] = p  # Symmetric matrix

# Plot the heatmap
plt.figure(figsize=(13, 8))
sns.heatmap(pval_matrix, annot=True, fmt=".2g", cmap='coolwarm', cbar_kws={'label': 'p-value'})
plt.title("Chi-Square Test p-value Matrix")
plt.tight_layout()
plt.show()

