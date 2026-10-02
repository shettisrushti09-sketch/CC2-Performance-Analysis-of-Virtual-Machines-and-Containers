# Performance Analysis of Virtual Machines and Containers

## CC2 – Performance Analysis of Virtual Machines and Containers

### Abstract

This project presents a practical performance analysis of Virtual Machines (VMs) and Containers using CPU, memory, disk I/O, network, application, startup-time, and scalability workloads.

The experiments were conducted in a controlled Linux environment using benchmark tools such as Sysbench, FIO, iPerf3, ApacheBench, and WRK. The collected benchmark outputs were processed using Python and Pandas, and performance graphs were generated using Matplotlib.

The purpose of the project is to observe the performance characteristics of virtualization and containerization under different workloads and to analyze the measured results using statistical methods.

---

## 1. Objectives

The main objectives of this project are:

- To study the performance characteristics of Virtual Machines and Containers.
- To measure CPU performance.
- To measure memory performance.
- To evaluate disk I/O performance.
- To measure network performance.
- To evaluate application-level performance using FastAPI.
- To measure container startup time.
- To study scalability under increasing workload.
- To collect and process benchmark results.
- To visualize experimental results using graphs.
- To perform statistical analysis of the collected measurements.
- To document the complete experimental methodology and results.

---

## 2. Research Questions

The experiments are designed to investigate the following questions:

1. How does CPU performance behave under the tested virtualization/container environment?
2. How does memory performance behave under the tested workload?
3. How does disk I/O performance behave under the tested configuration?
4. What network throughput is achieved during the benchmark?
5. How does the FastAPI application perform under load?
6. How quickly can the containerized application be started?
7. How does system/application performance change as workload and concurrency increase?

---

## 3. Experiments

The project consists of seven major performance experiments:

1. CPU Benchmark
2. Memory Benchmark
3. Disk I/O Benchmark
4. Network Benchmark
5. FastAPI/Application Benchmark
6. Startup-Time Benchmark
7. Scalability Benchmark

Each experiment produces measured data that is stored as raw benchmark output and/or processed CSV data.

---

## 4. Experimental Environment

### Hardware

The experiments were performed inside a Linux virtualized environment.

Hardware and system information collected during the experiment is available in:

- `docs/cpu-info.txt`
- `docs/memory-info.txt`
- `docs/storage-info.txt`
- `docs/kernel-info.txt`

### Software and Tools

The following tools were used during the experiments:

- Ubuntu Linux
- Docker
- Sysbench
- FIO
- iPerf3
- FastAPI
- Uvicorn
- ApacheBench (ab)
- WRK
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter

---

## 5. Project Architecture

The experimental setup contains a Linux virtual-machine environment and Docker-based container workloads.

The benchmarks are executed using controlled workloads, and their outputs are collected for further processing and analysis.

```text
Host System
    |
    └── Linux Virtual Machine
          |
          ├── VM-based Benchmarks
          |
          └── Docker
                |
                └── Container-based Workloads
