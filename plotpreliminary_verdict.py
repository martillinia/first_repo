import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Mantamonis_bacterial_contamination_analysis (3).xlsx")

print(df.columns)

counts = df["Preliminary Verdict:"].value_counts()

counts.plot(kind='bar', color='skyblue')
plt.title("Counts of Preliminary Verdicts")
plt.xlabel("Preliminary Verdict:")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("preliminary_classification.png")
plt.show()