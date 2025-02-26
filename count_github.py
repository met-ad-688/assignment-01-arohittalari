import pandas as pd

df = pd.read_csv("question_tags.csv")

# Count occurrences of "GitHub" in the Tag column
count = df["Tag"].str.contains("GitHub", case=False, na=False).sum()

# Save the result
with open("_output/count_github.txt", "w") as f:
    f.write(str(count))

print(f"Total occurrences of 'GitHub': {count}")


