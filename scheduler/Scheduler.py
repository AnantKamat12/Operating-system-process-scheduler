class Scheduler:
    def __init__(self, process_list):
        self.process_list = process_list
        self.current_time = 0

    def run(self):
        raise NotImplementedError(
            "Subclasses must implement the run method."
        )

    def run_detail(self):
        raise NotImplementedError(
            "Subclasses must implement the run_detail method."
        )

    def print_result(self):
        print("\nProcess Results:")
        for process in self.process_list:
            print(process)

    def print_current_time(self):
        print(f"Current Time: {self.current_time}")

    def print_current_process_list(self):
        print("\nCurrent Process List:")
        for process in self.process_list:
            print(process)

    def print_final_order_of_completion(self):
        print("\nFinal Order of Completion:")

        completed_processes = sorted(self.process_list, key=lambda p: p.completion_time)

        for i, process in enumerate(completed_processes,start=1):
            print(f"{i}. {process}")
    @property
    def average_waiting_time(self):
        return (
            sum(
                p.waiting_time
                for p in self.process_list
            )
            / len(self.process_list)
        )
    @property
    def average_turnaround_time(self):
        return (
            sum(p.turnaround_time for p in self.process_list ) / len(self.process_list)
        )
    @property
    def average_response_time(self):
        return (
            sum(
                p.response_time for p in self.process_list ) / len(self.process_list)
        )