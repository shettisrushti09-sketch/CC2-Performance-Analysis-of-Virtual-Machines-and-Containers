import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "results/processed/scalability_results.csv"
)

api = df[df["workload"] == "api"]

print(api)

plt.figure()

plt.plot(
    api["connections"],
    api["throughput"],
    marker="o"
)

plt.xlabel("Connections")
plt.ylabel("Requests per Second")
plt.title("API Scalability Performance")
plt.tight_layout()

plt.savefig(
    "results/figures/api_scalability.png",
    dpi=300
)

plt.show()
