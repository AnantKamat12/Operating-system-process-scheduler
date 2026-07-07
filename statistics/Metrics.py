import pandas as pd


class Metrics:
    def __init__(self):
        self.results = []

    def add_result(self, algorithm_name, scheduler):
        self.results.append(
            {
                "Algorithm": algorithm_name,
                "Average_WT":
                    round(
                        scheduler.average_waiting_time,
                        2
                    ),
                "Average_TAT":
                    round(
                        scheduler.average_turnaround_time,
                        2
                    ),
                "Average_RT":
                    round(
                        scheduler.average_response_time,
                        2
                    ),
            }
        )

    def print_comparison(self):
        print("\nComparison Table")
        print("-" * 65)

        print(
            f"{'Algorithm':<15}"
            f"{'Avg WT':<15}"
            f"{'Avg TAT':<15}"
            f"{'Avg RT':<15}"
        )

        print("-" * 65)

        for row in self.results:
            print(
                f"{row['Algorithm']:<15}"
                f"{row['Average_WT']:<15}"
                f"{row['Average_TAT']:<15}"
                f"{row['Average_RT']:<15}"
            )

    def export_to_csv(
            self,
            filename="metrics.csv"
    ):
        df = pd.DataFrame(self.results)
        df.to_csv(filename, index=False)

        print(
            f"\nMetrics exported to "
            f"{filename}"
        )