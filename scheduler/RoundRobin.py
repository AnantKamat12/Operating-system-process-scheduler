from scheduler.Scheduler import Scheduler


class RoundRobin(Scheduler):
    def __init__(self,
                 process_list,
                 quantum=2):
        super().__init__(process_list)
        self.quantum = quantum

    def run(self):

        queue = []
        remaining = sorted(
            self.process_list,
            key=lambda p: p.arrival_time
        )

        self.current_time = 0

        while remaining or queue:

            while (
                remaining
                and remaining[0].arrival_time
                <= self.current_time
            ):
                queue.append(
                    remaining.pop(0)
                )

            if not queue:
                self.current_time += 1
                continue

            process = queue.pop(0)

            if process.response_time is None:
                process.response_time = (
                    self.current_time
                    - process.arrival_time
                )

            execution_time = min(
                self.quantum,
                process.remaining_time
            )

            self.current_time += execution_time

            process.remaining_time -= (
                execution_time
            )

            while (
                remaining
                and remaining[0].arrival_time
                <= self.current_time
            ):
                queue.append(
                    remaining.pop(0)
                )

            if process.remaining_time > 0:
                queue.append(process)
            else:
                process.completion_time = (
                    self.current_time
                )

                process.turnaround_time = (
                    process.completion_time
                    - process.arrival_time
                )

                process.waiting_time = (
                    process.turnaround_time
                    - process.burst_time
                )

    def run_detail(self):
        print(
            f"Running Round Robin "
            f"(Quantum={self.quantum})"
        )
        self.run()