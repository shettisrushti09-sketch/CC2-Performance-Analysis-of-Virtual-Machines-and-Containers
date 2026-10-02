import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/processed/memory_results.csv"
)

print(df)

summary = df.groupby("environment")[
    "events"
].mean()

print("\nAverage Memory Performance:")
print(summary)

summary.plot(
    kind="bar",
    title="Average Memory Performance"
)

plt.ylabel("Events")
plt.xlabel("Environment")
plt.tight_layout()

plt.savefig(
    "results/figures/memory_performance.png",
    dpi=300
)

plt.show()
