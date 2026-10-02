import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/processed/network_results.csv"
)

print(df)

summary = df.groupby("environment")[
    "bandwidth_gbits_per_sec"
].mean()

print("\nAverage Network Performance:")
print(summary)

summary.plot(
    kind="bar",
    title="Average Network Performance"
)

plt.ylabel("Bandwidth (Gbits/s)")
plt.xlabel("Environment")
plt.tight_layout()

plt.savefig(
    "results/figures/network_performance.png",
    dpi=300
)

plt.show()
