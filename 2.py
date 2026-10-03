import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_score
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Student': ['Shrikant','Shrikant','Shrikant','naitika','naitika','naitika',
                'yash','yash','onkar','onkar','Tanvi','Tanvi','Tanvi'],
    'Interests': ['AI/ML','Web Dev','Cloud Computing','AI/ML','Cyber Security',
                  'UI/UX','Web Dev','Cloud Computing','AI/ML','Data Science',
                  'Cyber Security','Cloud Computing','DevOps']
}

df = pd.DataFrame(data)
df

incidence = pd.crosstab(df["Student"], df["Interests"])
incidence

binary_matrix = (incidence > 0).astype(int)
binary_matrix

student_sim_df = pd.DataFrame(
    binary_matrix.values @ binary_matrix.values.T,
    index=incidence.index,
    columns=incidence.index
)
student_sim_df

cos_df = pd.DataFrame(
    cosine_similarity(binary_matrix),
    index=incidence.index,
    columns=incidence.index
)
cos_df

def jaccard_matrix(X):
    return np.array([[jaccard_score(a, b) for b in X] for a in X])

jac_df = pd.DataFrame(
    jaccard_matrix(binary_matrix.values),
    index=incidence.index,
    columns=incidence.index
)
jac_df

plt.figure(figsize=(6,4))
sns.heatmap(cos_df, annot=True, cmap="YlGnBu")
plt.title("Student Intrest Similarity (Cosine)")
plt.show()
