import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/processed/disk_results.csv"
)

print(df)

summary = df.groupby("environment")[
    "bandwidth_kib_per_sec"
].mean()

print("\nAverage Disk Performance:")
print(summary)

summary.plot(
    kind="bar",
    title="Average Disk Performance"
)

plt.ylabel("Bandwidth (KiB/s)")
plt.xlabel("Environment")
plt.tight_layout()

plt.savefig(
    "results/figures/disk_performance.png",
    dpi=300
)

plt.show()

