import copy

from scheduler.Process import Process
from utils.Predefined_Processes import Predefined_Processes
from utils.ReadCsv import read_processes_from_csv

from scheduler.FCFS import FCFS
from scheduler.SJF import SJF
from scheduler.PriorityScheduler import PriorityScheduler
from scheduler.RoundRobin import RoundRobin

from statistics.Metrics import Metrics


def main():
    print("Welcome to the Operating System Process Scheduler Simulation!")

    print("\nInput Modes:")
    print("1 -> Manual Input")
    print("0 -> Predefined Process Trains")
    print("2 -> Read Processes From CSV")

    x = int(input("\nChoose input mode: "))

    process_list = []

    # ==========================
    # Manual Input
    # ==========================
    if x == 1:
        num_of_process = int(
            input("Enter number of processes: ")
        )

        for i in range(num_of_process):
            process_num = i + 1

            burst_time = int(
                input(
                    f"Enter burst time for Process {process_num}: "
                )
            )

            priority = int(
                input(
                    f"Enter priority for Process {process_num}: "
                )
            )

            arrival_time = int(
                input(
                    f"Enter arrival time for Process {process_num}: "
                )
            )

            process = Process(
                process_num,
                burst_time,
                priority,
                arrival_time
            )

            process_list.append(process)

    # ==========================
    # Predefined Input
    # ==========================
    elif x == 0:
        predefined = Predefined_Processes()

        predefined.print_all_trains()

        print(
            "\n"
            + "#" * 20
            + " Choose One From Above "
            + "#" * 20
        )

        choose = int(
            input(
                "Choose a process train: "
            )
        )

        chosen_train = predefined.get_processes(
            choose
        )

        for i, process in enumerate(
            chosen_train,
            start=1
        ):
            process_obj = Process(
                i,
                process["burst_time"],
                process["priority"],
                process["arrival_time"]
            )

            process_list.append(process_obj)

    # ==========================
    # CSV Input
    # ==========================
    elif x == 2:
        print(
            "\nCSV must contain exactly 3 columns "
            "in the following order:\n"
            "1 -> burst_time\n"
            "2 -> priority\n"
            "3 -> arrival_time\n"
        )
        print("Find Example csvs in tests/ module")

        file_path = input(
            "Enter CSV file path: "
        )

        chosen_train = read_processes_from_csv(
            file_path
        )

        if not chosen_train:
            print(
                "No processes loaded from CSV."
            )
            return

        for process in chosen_train:
            process_obj = Process(
                process["process_id"],
                process["burst_time"],
                process["priority"],
                process["arrival_time"]
            )

            process_list.append(process_obj)

    else:
        print("Invalid choice.")
        return

    # ==========================
    # Print Created Processes
    # ==========================
    print("\nCreated Processes:\n")

    for i, process in enumerate(
        process_list,
        start=1
    ):
        print(f"[Process {i}] {process}")

    print(
        "\nRunning all scheduling algorithms...\n"
    )

    # ==========================
    # Algorithms
    # ==========================
    algorithms = [
        ("FCFS", FCFS(copy.deepcopy(process_list))),
        ("SJF", SJF(copy.deepcopy(process_list))),
        (
            "Priority",
            PriorityScheduler(
                copy.deepcopy(process_list)
            ),
        ),
        (
            "Round Robin",
            RoundRobin(
                copy.deepcopy(process_list),
                quantum=2,
            ),
        ),
    ]

    metrics = Metrics()

    for name, algo in algorithms:
        print(
            "\n"
            + "=" * 20
            + f" {name} "
            + "=" * 20
        )

        algo.run()

        algo.print_result()
        algo.print_final_order_of_completion()

        print(
            f"Average WT : "
            f"{algo.average_waiting_time:.2f}"
        )

        print(
            f"Average TAT: "
            f"{algo.average_turnaround_time:.2f}"
        )

        print(
            f"Average RT : "
            f"{algo.average_response_time:.2f}"
        )

        metrics.add_result(
            name,
            algo
        )

    # ==========================
    # Comparative Statistics
    # ==========================
    metrics.print_comparison()
    metrics.export_to_csv()


if __name__ == "__main__":
    main()