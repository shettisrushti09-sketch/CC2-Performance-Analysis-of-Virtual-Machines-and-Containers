# Performance Analysis of Virtual Machines and Containers

## 1. Project Overview

This project presents a practical performance analysis of **Virtual Machines (VMs)** and **Containers** using CPU, memory, disk I/O, network, application, startup-time, and scalability workloads.

The experiments were performed in a Linux environment using benchmark tools such as:

- Sysbench
- FIO
- iPerf3
- FastAPI
- ApacheBench (ab)
- WRK
- Python
- Matplotlib
- Pandas

The objective is to collect measurable performance data and study how virtualization and containerization behave under different workloads.

---

## 2. Objectives

The main objectives of this project are:

1. To understand the performance characteristics of virtual machines and containers.
2. To measure CPU performance.
3. To measure memory performance.
4. To evaluate disk I/O performance.
5. To evaluate network performance.
6. To evaluate application-level performance using FastAPI.
7. To measure container startup time.
8. To study scalability with increasing CPU threads and API connections.
9. To collect raw benchmark data and process it using Python.
10. To visualize benchmark results using graphs.
11. To organize the complete experiment in a reproducible GitHub repository.

---

## 3. Research Questions

This experiment investigates the following questions:

1. How does CPU performance behave under different workloads?
2. How does memory performance behave?
3. What disk I/O performance is obtained?
4. What network throughput is achieved?
5. How does the FastAPI application perform under load?
6. How much time does container startup require?
7. How does CPU throughput change as the number of threads increases?
8. How does API throughput change as the number of connections increases?

---

# 4. Experimental Environment

## Hardware and Software

The experiments were performed using a Linux virtual machine environment.

### Software and Tools

| Tool | Purpose |
|---|---|
| Ubuntu | Linux experimental environment |
| Docker | Container execution |
| Sysbench | CPU and memory benchmarking |
| FIO | Disk I/O benchmarking |
| iPerf3 | Network benchmarking |
| FastAPI | Application workload |
| ApacheBench | HTTP benchmarking |
| WRK | Scalability testing |
| Python | Data processing |
| Pandas | Statistical analysis |
| Matplotlib | Graph generation |
| Git | Version control |
| GitHub | Project repository |

---

# 5. Project Architecture

The project follows a benchmark-and-analysis architecture:

```text
                 Performance Analysis
                         |
          +--------------+--------------+
          |                             |
     Virtual Machine                Container
          |                             |
     Benchmark Tests              Benchmark Tests
          |                             |
          +--------------+--------------+
                         |
                   Raw Results
                         |
                 Processed CSV Data
                         |
                  Python Analysis
                         |
                    Graphs/Tables
                         |
                  Final Comparison
6. Project Structure
vm-vs-container-performance/
│
├── README.md
├── .gitignore
│
├── docs/
│   ├── cpu-info.txt
│   ├── memory-info.txt
│   ├── storage-info.txt
│   └── kernel-info.txt
│
├── docker/
│   ├── Dockerfile
│   └── Dokerfile
│
├── api/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── scripts/
│   ├── analyze_results.py
│   ├── analyze_memory.py
│   ├── analyze_disk.py
│   ├── analyze_network.py
│   ├── analyze_api.py
│   ├── analyze_startup.py
│   ├── analyze_scalability.py
│   └── analyze_api_scalability.py
│
├── results/
│   ├── raw/
│   ├── processed/
│   └── figures/
│
└── analysis/
7. Methodology

The experiments followed this general workflow:

Prepare Environment
        ↓
Configure VM
        ↓
Configure Docker
        ↓
Establish Baseline
        ↓
CPU Benchmark
        ↓
Memory Benchmark
        ↓
Disk Benchmark
        ↓
Network Benchmark
        ↓
FastAPI Benchmark
        ↓
Startup Test
        ↓
Scalability Test
        ↓
Collect Raw Data
        ↓
Python Analysis
        ↓
Graphs and Tables
        ↓
Discussion and Conclusion

Raw benchmark outputs were stored separately from processed CSV files.

8. CPU Benchmark

The CPU benchmark was performed using Sysbench.

Command
sysbench cpu --cpu-max-prime=20000 --threads=1 run
Observed Result
Metric	Value
Total time	10.0012 s
Events	1108
Average latency	9.01 ms
95th percentile latency	17.63 ms
CPU Performance Graph

9. Memory Benchmark

Memory performance was measured using Sysbench.

Workload
Block size: 1 MB
Total memory size: 1 GB
Threads: 1
Result
Metric	Value
Total time	0.6910 s
Events	1024
Average latency	0.63 ms
95th percentile latency	2.00 ms
Memory Performance Graph

10. Disk I/O Benchmark

Disk performance was evaluated using FIO with a sequential write workload.

Configuration
Parameter	Value
Workload	Sequential write
File size	1 GB
Block size	1 MB
Direct I/O	Enabled
Runtime	30 seconds
Result
Metric	Value
Bandwidth	126915.14 KiB/s
IOPS	123.52
CPU user	6.43%
CPU system	68.12%
Disk Performance Graph

11. Network Benchmark

Network performance was measured using iPerf3.

Configuration
Parameter	Value
Duration	30 seconds
Throughput	2.29 Gbits/s
Retransmissions	4
Network Performance Graph

12. Application Benchmark — FastAPI

A FastAPI application was created with three endpoints:

/health
/compute
/memory

The /compute endpoint performs a computational workload by calculating the sum of squares from 1 to 1,000,000.

FastAPI Compute Test

ApacheBench was used with:

1000 requests
10 concurrent requests
Result
Metric	Value
Requests	1000
Failed requests	0
Total time	521.569 s
Requests per second	1.92
Mean time per request	5215.690 ms
API Performance Graph

13. Container Startup-Time Benchmark

Container startup time was measured using repeated Docker runs.

Startup Measurements
Run	Startup Time
Run 1	7.084 s
Run 2	3.164 s
Run 3	2.949 s
Statistics
Statistic	Value
Mean	4.399 s
Median	3.164 s
Minimum	2.949 s
Maximum	7.084 s
Standard deviation	2.308 s
Startup Performance Graph

14. Scalability Experiment

Scalability was studied for both CPU and API workloads.

14.1 CPU Scalability

The CPU workload was executed with increasing numbers of threads.

Threads	Events/sec	Avg Latency (ms)	P95 Latency (ms)
1	122.98	8.11	12.52
2	218.57	9.14	15.27
4	257.60	15.51	37.56
8	284.29	28.07	58.92
CPU Scalability Graph

14.2 API Scalability

The FastAPI workload was tested with increasing numbers of client connections.

Threads	Connections	Requests/sec	Avg Latency (ms)	Total Requests
1	10	112.87	92.69	3392
2	50	150.28	331.02	4512
4	100	171.42	577.22	5153
4	200	147.64	1290.00	4439

The 200-connection test recorded a maximum latency of approximately 2000 ms. This value is not treated as a P95 value.

API Scalability Graph

15. Statistical Analysis

The benchmark results were processed using Python and Pandas.

The following statistics were calculated where multiple measurements were available:

Mean
Median
Minimum
Maximum
Standard deviation
CPU Statistics
Statistic	Events/sec
Mean	220.86
Median	238.085
Minimum	122.98
Maximum	284.29
Standard deviation	70.61
Startup Statistics
Statistic	Time (s)
Mean	4.399
Median	3.164
Minimum	2.949
Maximum	7.084
Standard deviation	2.308
Scalability Statistics
Workload	Mean Throughput
CPU	220.86 events/sec
API	145.55 requests/sec
16. VM vs Container Comparison

The collected experiments provide measurements for different workloads across the experimental environments.

Workload	Environment Measured	Main Metric
CPU	VM	220.86 events/sec average
Memory	Container	1024 events
Disk I/O	Container	126915.14 KiB/s
Network	VM	2.29 Gbits/s
FastAPI	VM	1.92 requests/sec
Startup	Container	4.399 s average

The measurements should be interpreted according to the specific workload and environment tested. Not every benchmark has paired VM and container measurements, so the results should not be treated as a direct one-to-one comparison for every workload.

17. Results Summary

The experiments produced measurable results for:

CPU performance
Memory performance
Disk I/O
Network throughput
Application performance
Container startup time
CPU scalability
API scalability

All processed measurements are stored in:

results/processed/

Raw benchmark outputs are stored in:

results/raw/

Generated graphs are stored in:

results/figures/
18. Discussion

The experiments demonstrate how different workload types can be measured using standardized benchmarking tools.

CPU scalability increased as the number of threads increased, although latency also increased with higher thread counts.

For the API scalability experiment, throughput increased up to the 100-connection test and decreased at 200 connections, while average latency increased substantially.

The startup experiment showed different startup times across repeated container launches, with an average measured startup time of 4.399 seconds.

The results demonstrate the importance of evaluating virtualization and containerization using multiple workload categories rather than relying on a single benchmark.

19. Limitations

The following limitations apply to the experiment:

Not every workload was measured in both VM and container environments.
The experiments were performed in a controlled laboratory environment.
Hardware and host-system conditions can influence benchmark results.
Network performance can vary depending on the virtual networking configuration.
Application performance depends on workload characteristics and server configuration.
A larger number of repeated runs could provide more statistical confidence.
20. Conclusion

This project implemented a practical performance analysis workflow for virtual machines and containers.

The experiments covered:

CPU
Memory
Disk I/O
Network
Application performance
Startup time
Scalability

Benchmark results were collected as raw data, converted into processed datasets, analyzed using Python, and visualized using graphs.

The project demonstrates a complete workflow from environment preparation and benchmarking to statistical analysis, visualization, and GitHub-based documentation.

21. Future Work

Future extensions could include:

Running every benchmark in both VM and container environments.
Increasing the number of benchmark repetitions.
Testing additional CPU workloads.
Testing random disk I/O workloads.
Testing multiple network configurations.
Testing additional application workloads.
Performing larger-scale container and VM scalability experiments.
Adding confidence intervals to statistical analysis.
Automating the complete benchmark pipeline.
22. Reproduction Instructions

Clone the repository:

git clone https://github.com/shettisrushti09-sketch/CC2-Performance-Analysis-of-Virtual-Machines-and-Containers.git

Enter the project directory:

cd CC2-Performance-Analysis-of-Virtual-Machines-and-Containers

The processed benchmark data is available in:

results/processed/

The generated graphs are available in:

results/figures/

The raw benchmark outputs are available in:

results/raw/
23. Technologies Used
Ubuntu Linux
Docker
Sysbench
FIO
iPerf3
FastAPI
ApacheBench
WRK
Python
Pandas
Matplotlib
Git
GitHub
24. Repository

GitHub Repository:

https://github.com/shettisrushti09-sketch/CC2-Performance-Analysis-of-Virtual-Machines-and-Containers

Project Summary

This project provides a practical benchmark-based study of virtualization and containerization performance using multiple workload categories.

The complete workflow includes:

Benchmarking
     ↓
Raw Data Collection
     ↓
CSV Processing
     ↓
Statistical Analysis
     ↓
Graph Generation
     ↓
Performance Discussion
     ↓
GitHub Documentation
