# Operating System Process Scheduler Simulator

A Python-based simulator for classical CPU scheduling algorithms built using Object-Oriented Programming principles.

## Planned Features

- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Round Robin (RR)
- Priority Scheduling
- Gantt Chart Visualization
- Command Line Interface (CLI)
- File-based Process Input
- Scheduling Statistics and Reports
- Unit Testing

## Planned Class Design

```text
Process
Scheduler (Abstract Base Class)
├── FCFSScheduler
├── SJFScheduler
├── RoundRobinScheduler
└── PriorityScheduler

Statistics
Simulation
```

## Technologies

- Python 3
- Object-Oriented Programming
- Git & GitHub
- unittest

## Learning Goals

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Clean Code and Project Structure
- Software Development using Git Branches

## Status
v1.0
------
✅ FCFS
✅ SJF
✅ Priority
✅ Round Robin
✅ Metrics

v1.1
------
□ Statistics module(TBD)
□ Comparison table(TBD)
□ Unit tests(TBD)

v1.2
------
□ Gantt chart
□ Detailed simulation mode
□ Ready queue visualization

v1.3
------
□ CSV import/export (TBD after statistics module implemenatation)
□ Throughput
□ CPU utilization

v2.0
------
□ Preemptive schedulers
□ GUI
