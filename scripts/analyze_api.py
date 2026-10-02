import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/processed/api_results.csv"
)

print(df)

summary = df.groupby("environment")[
    "requests_per_second"
].mean()

print("\nAverage Application Performance:")
print(summary)

summary.plot(
    kind="bar",
    title="Average Application Performance"
)

plt.ylabel("Requests per Second")
plt.xlabel("Environment")
plt.tight_layout()

plt.savefig(
    "results/figures/api_performance.png",
    dpi=300
)

plt.show()
