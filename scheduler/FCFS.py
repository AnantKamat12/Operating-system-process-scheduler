from scheduler.Scheduler import Scheduler


class FCFS(Scheduler):
    def __init__(self, process_list):
        super().__init__(process_list)

    def run(self):
        self.process_list.sort(key=lambda p: p.arrival_time)

        for process in self.process_list:
            if self.current_time < process.arrival_time:
                self.current_time = process.arrival_time

            process.waiting_time = (
                self.current_time - process.arrival_time
            )

            process.response_time = process.waiting_time

            self.current_time += process.burst_time

            process.completion_time = self.current_time

            process.turnaround_time = (
                process.completion_time
                - process.arrival_time
            )

    def run_detail(self):
        print(
            "This is a non-preemptive FCFS scheduler. "
            "Processes are executed according to arrival time."
        )
        self.run()