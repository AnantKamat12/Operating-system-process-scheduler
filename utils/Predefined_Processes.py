class Predefined_Processes:
    def __init__(self):

        # Train 1: Standard mixed workload with steady arrivals
        self.train_1 = [
            {"burst_time": 5, "priority": 2, "arrival_time": 0},
            {"burst_time": 3, "priority": 1, "arrival_time": 1},
            {"burst_time": 8, "priority": 3, "arrival_time": 2},
            {"burst_time": 6, "priority": 2, "arrival_time": 3},
            {"burst_time": 2, "priority": 1, "arrival_time": 4}
        ]

        # Train 2: Short-burst heavy (Good for SJF)
        self.train_2 = [
            {"burst_time": 2, "priority": 3, "arrival_time": 0},
            {"burst_time": 1, "priority": 4, "arrival_time": 0},
            {"burst_time": 4, "priority": 1, "arrival_time": 1},
            {"burst_time": 3, "priority": 2, "arrival_time": 3}
        ]

        # Train 3: Convoy Effect
        self.train_3 = [
            {"burst_time": 30, "priority": 1, "arrival_time": 0},
            {"burst_time": 2, "priority": 2, "arrival_time": 1},
            {"burst_time": 1, "priority": 3, "arrival_time": 1}
        ]

        # Train 4: Starvation Scenario
        self.train_4 = [
            {"burst_time": 20, "priority": 3, "arrival_time": 0},
            {"burst_time": 1, "priority": 1, "arrival_time": 1},
            {"burst_time": 1, "priority": 1, "arrival_time": 2},
            {"burst_time": 1, "priority": 1, "arrival_time": 3},
            {"burst_time": 1, "priority": 1, "arrival_time": 4}
        ]

        # Train 5: All processes arrive together
        self.train_5 = [
            {"burst_time": 7, "priority": 2, "arrival_time": 0},
            {"burst_time": 3, "priority": 1, "arrival_time": 0},
            {"burst_time": 5, "priority": 4, "arrival_time": 0},
            {"burst_time": 1, "priority": 3, "arrival_time": 0}
        ]

        # Train 6: Round Robin demonstration
        self.train_6 = [
            {"burst_time": 5, "priority": 1, "arrival_time": 0},
            {"burst_time": 4, "priority": 2, "arrival_time": 1},
            {"burst_time": 6, "priority": 3, "arrival_time": 2},
            {"burst_time": 3, "priority": 1, "arrival_time": 3}
        ]

        # Train 7: CPU-bound workload
        self.train_7 = [
            {"burst_time": 25, "priority": 1, "arrival_time": 0},
            {"burst_time": 20, "priority": 2, "arrival_time": 2},
            {"burst_time": 15, "priority": 3, "arrival_time": 5}
        ]

        # Train 8: I/O-bound workload
        self.train_8 = [
            {"burst_time": 1, "priority": 2, "arrival_time": 0},
            {"burst_time": 2, "priority": 1, "arrival_time": 1},
            {"burst_time": 1, "priority": 3, "arrival_time": 2},
            {"burst_time": 2, "priority": 2, "arrival_time": 3},
            {"burst_time": 1, "priority": 1, "arrival_time": 4}
        ]

        self.all_trains = [
            self.train_1,
            self.train_2,
            self.train_3,
            self.train_4,
            self.train_5,
            self.train_6,
            self.train_7,
            self.train_8
        ]

        self.train_descriptions = [
            "Standard Mixed Workload",
            "Short-Burst Heavy Sequence",
            "Convoy Effect Sequence",
            "Starvation Scenario",
            "Simultaneous Arrival Workload",
            "Round Robin Demonstration",
            "CPU-bound Workload",
            "I/O-bound Workload"
        ]

    def print_train(self, train_list):
        for i, process in enumerate(train_list):
            print(
                f"  [Process {i + 1}] "
                f"Burst: {process['burst_time']}, "
                f"Priority: {process['priority']}, "
                f"Arrival: {process['arrival_time']}"
            )

    def print_all_trains(self):
        print("\nAvailable process trains:")

        for i, train in enumerate(self.all_trains, start=1):
            print(f"\n{i}. {self.train_descriptions[i - 1]}")
            self.print_train(train)

    def get_processes(self, choice):
        if 1 <= choice <= len(self.all_trains):
            print(
                f"\n--- Selected Train {choice}: "
                f"{self.train_descriptions[choice - 1]} ---"
            )
            return self.all_trains[choice - 1]

        print("\nInvalid choice. Defaulting to Train 1.")
        return self.train_1