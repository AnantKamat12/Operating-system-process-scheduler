import time
import random
import os
import sys
from scheduler.Process import Process
from utils.Predefined_Processes import Predefined_Processes
# from scheduler.FCFS import FCFS
# from scheduler.SJF import SJF
# from scheduler.Priority import PriorityScheduler
# from scheduler.RoundRobin import RoundRobin
# from statistics.metrics import Metrics

#this must take input from user and creat process with
#attribute burst time, priority and and assign process id
#and print output params tbd
# main.py
#    ↓
# Take input from user
#    ↓
# Create Process objects
#    ↓
# Store them in a list(done)
#    ↓
# Choose scheduling algorithm (tbd)
#    ↓
# Run scheduler
#    ↓
# Scheduler computes metrics
#    ↓
# Print results
#we need to import variosu module once written we can use them to create process and assign attributes
def main():
    print("Welcome to the Operating System Process Scheduler Simulation!")
    x=int(input("Give input of processes: 1 OR use predefined processes input:0  \n "))
    process_list=[]
    if x:
        num_of_process=int(input(("Enter the num of process you want to create:")))
        for i in range(num_of_process):

            process_num = i + 1
            burst_time = int(input(f"Enter burst time for Process {process_num}: "))
            priority = int(input(f"Enter priority for Process {process_num}: "))
            arrival_time = int(input(f"Enter arrival time for Process {process_num}: "))
            process = Process(process_num, burst_time, priority, arrival_time)
            process_list.append(process)
    else:
        
        Predefined_Processes_obj=Predefined_Processes()
        Predefined_Processes_obj.print_all_trains()
        print("#"*50 +"Choose_one_from_the_above" + "#"*50+"\n")
        choose=int(input("Choose a list of processes from given list of processes: "))
        
        chosen_train=Predefined_Processes_obj.get_processes(choose)
        for i, process in enumerate(chosen_train):
            process_num = i + 1
            burst_time = process['burst_time']
            priority = process['priority']
            arrival_time = process['arrival_time']
            process_obj = Process(process_num, burst_time, priority, arrival_time)
            process_list.append(process_obj)

    print("\nCreated Processes:")
    for i, process in enumerate(process_list, start=1):
        #print(f"  [PID {process.pid}], Process_encrypt_id: {process.process_id}, Burst: {process.burst_time}, Priority: {process.priority}, Arrival: {process.arrival_time}")
        print(f"  [Process {i}] {process}")

    print("\nProcess list created successfully. will run all scheduling algorithms on train of processes now.")
    #just do FCFS.run(process_list) SJF.run(process_list) Priority.run(process_list) RoundRobin.run(process_list) and print the output of each algorithm


if __name__ == "__main__":
    main()
# list_TODO
# [ ] Add option to run a specific scheduling algorithm, create run_in_detail utility in every---
# --- scheduling algorithm class and ask input from user to run specific algorithm or all algorithms on the same train of processes
# [ ] Add CSV/TXT input support
# [ ] Add Gantt chart generation
# [ ] Add algorithm comparison summary table
# [ ] Add export of results to TXT/CSV
# [ ] Add workload statistics (CPU utilization, throughput)

# [ ] Add run_detail() method to all scheduling algorithms
# [ ] Explain scheduling decisions step-by-step
# [ ] Explain process preemption and queue movements
# [ ] Add ready queue visualization



