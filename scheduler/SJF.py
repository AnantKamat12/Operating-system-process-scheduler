from scheduler.Scheduler import Scheduler


class SJF(Scheduler):
    def __init__(self, process_list):
        super().__init__(process_list)

    def run(self):
        remaining = self.process_list.copy()
        self.current_time = 0

        while remaining:

            available = [
                p for p in remaining
                if p.arrival_time <= self.current_time
            ]

            if not available:
                self.current_time += 1
                continue

            process = min(
                available,
                key=lambda p: p.burst_time
            )

            process.waiting_time = (
                self.current_time
                - process.arrival_time
            )

            process.response_time = (
                process.waiting_time
            )

            self.current_time += process.burst_time

            process.completion_time = (
                self.current_time
            )

            process.turnaround_time = (
                process.completion_time
                - process.arrival_time
            )

            remaining.remove(process)

    def run_detail(self):
        #I wanted to implement a more detailed version of SJF,/by adding more logging
        print("Running Shortest Job First...")
        self.run()