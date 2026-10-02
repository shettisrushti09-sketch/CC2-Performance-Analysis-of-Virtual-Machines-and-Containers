import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/processed/scalability_results.csv"
)

print(df)

cpu = df[df["workload"] == "cpu"]
api = df[df["workload"] == "api"]

plt.figure()

plt.plot(
    cpu["threads"],
    cpu["throughput"],
    marker="o",
    label="CPU"
)

plt.xlabel("Threads")
plt.ylabel("Throughput (Events per Second)")
plt.title("CPU Scalability Performance")
plt.legend()
plt.tight_layout()

plt.savefig(
    "results/figures/cpu_scalability.png",
    dpi=300
)

plt.show()
