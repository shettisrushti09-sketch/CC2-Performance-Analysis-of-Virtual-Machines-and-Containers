import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/processed/startup_results.csv"
)

print(df)

summary = df.groupby("environment")[
    "real_time_seconds"
].mean()

print("\nAverage Startup Time:")
print(summary)

summary.plot(
    kind="bar",
    title="Average Container Startup Time"
)

plt.ylabel("Startup Time (seconds)")
plt.xlabel("Environment")
plt.tight_layout()

plt.savefig(
    "results/figures/startup_performance.png",
    dpi=300
)

plt.show()
