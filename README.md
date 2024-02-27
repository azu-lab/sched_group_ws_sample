# sched_group_ws_sample
Sample procedures are described in each jupyter notebook (.ipynb).

## 0. install dependency package
```bash
pip3 install -r ./requirements.txt
```

## 1. RD-Gen Reader
get DAG status from RD-Gen (https://github.com/azu-lab/RD-Gen)

RDG_DAG takes as input the array of execution times and the array of edges

in addition, methods related to graph structures use the networkx library

for detail, please refer src/dag_rd_gen.py
### 1. 1. Basic status of DAG
### 1. 2. Graph status of DAG

## 2. Utility of Scheduling_Visualization
visualize scheduling result

visualisation is done in an external library (https://github.com/atsushi421/Scheduling_Visualization)

two methods have been implemented: to prepare objects for visualisation and to provide arrays of data
### 2. 1. Generate visualizing target
### 2. 2. visualize from array

## 3. RD-Gen -> scheduling -> Scheduling_Visualization
minimum workflow of scheduling simulation

scheduler/ directory is a simple implementation of list scheduling

For details of sample list scheduling, refer to the following:
https://github.com/rokamu623/list_scheduling

## 4. evaluate taskset
a sample of evaluate scheduling algorithm

implementation is refered in src/simulate.py
### 4. 1. load RD-Gen from directory
### 4. 2. evaluate taskset
scheduling algorithm is implemented in src.simulate.simulate function

src.simulate.simulate return evaluated value (ex. WCRT)

src.simulate.simulate_taskset return list of evaluated values for all DAG (dags)
### 4. 3. visualize

**↓ appendix (not refactored) ↓**

## 5. prepare to existing method
### 5. 1. load RD-Gen from directory
### 5. 2. prepare to existing method
## 6. evaluate with varing parameter (extra)
### 6. 1. load RD-Gen from directory
### 6. 2. evaluate with varing parameter
### 6. 3. visualize

# directory
- output/            : graphs and files are outputted here
- sample_input/      : input files of samples are here
- sample_shceduler/  : scheduling algorithm using sample (not refactored)
- src/
  - dag_rd_gen.py    : RDG_DAG class which can load data from RD-Gen file is implemented
  - sched_vis_util.py: Visualize helper class is implemented
  - simulate.py      : sample function of evaluate scheduling algorithm
- n.xxx.ipynb        : sample of function of this repository
- README.md          : this
- requirements.txt   : package list of requirement packages

