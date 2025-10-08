import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Salary": np.random.randint(5000, 99000, size=5)
}

df = pd.DataFrame(data)

print("=== Original DataFrame ===")
print(df)
filtered_df = df[df["Salary"] > 50000]

print("\n=== Filtered DataFrame (Salary > 50,000) ===")
print(filtered_df)