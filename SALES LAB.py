import pandas as pd
import numpy as np

# Step 1 — Create a sample DataFrame with random salaries
np.random.seed(42)  # For reproducible results
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Salary": np.random.randint(5000, 99000, size=5)  # Random salaries
}

df = pd.DataFrame(data)

print("=== Original DataFrame ===")
print(df)

# Step 2 — Filter rows where Salary > 50,000
filtered_df = df[df["Salary"] > 50000]

print("\n=== Filtered DataFrame (Salary > 50,000) ===")
print(filtered_df)  