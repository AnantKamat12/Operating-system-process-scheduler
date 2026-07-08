import unittest
import copy
import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    ),
)
from scheduler.Process import Process
from scheduler.FCFS import FCFS
from scheduler.SJF import SJF
from scheduler.PriorityScheduler import PriorityScheduler
from scheduler.RoundRobin import RoundRobin
from statistics.Metrics import Metrics

class TestAllAlgorithms(unittest.TestCase):

    def setUp(self):
        self.process_list = [
            Process(1, 5, 2, 0),
            Process(2, 3, 1, 1),
            Process(3, 8, 3, 2),
            Process(4, 6, 2, 3),
            Process(5, 2, 1, 4),
        ]

    def test_fcfs(self):
        scheduler = FCFS(copy.deepcopy(self.process_list))
        scheduler.run()

        self.assertGreaterEqual(
            scheduler.average_waiting_time, 0
        )
        self.assertGreaterEqual(
            scheduler.average_turnaround_time, 0
        )
        self.assertGreaterEqual(
            scheduler.average_response_time, 0
        )

    def test_sjf(self):
        scheduler = SJF(copy.deepcopy(self.process_list))
        scheduler.run()

        self.assertGreaterEqual(
            scheduler.average_waiting_time, 0
        )
        self.assertGreaterEqual(
            scheduler.average_turnaround_time, 0
        )
        self.assertGreaterEqual(
            scheduler.average_response_time, 0
        )

    def test_priority(self):
        scheduler = PriorityScheduler(copy.deepcopy(self.process_list))
        scheduler.run()

        self.assertGreaterEqual(
            scheduler.average_waiting_time, 0
        )
        self.assertGreaterEqual(
            scheduler.average_turnaround_time, 0
        )
        self.assertGreaterEqual(
            scheduler.average_response_time, 0
        )

    def test_round_robin(self):
        scheduler = RoundRobin(
            copy.deepcopy(self.process_list),
            quantum=2
        )
        scheduler.run()

        self.assertGreaterEqual(
            scheduler.average_waiting_time, 0
        )
        self.assertGreaterEqual(
            scheduler.average_turnaround_time, 0
        )
        self.assertGreaterEqual(
            scheduler.average_response_time, 0
        )

    def test_metrics_and_csv_export(self):
        scheduler_fcfs = FCFS(copy.deepcopy(self.process_list))
        scheduler_fcfs.run()

        metrics = Metrics()

        metrics.add_result("FCFS", scheduler_fcfs)

        self.assertEqual(metrics.results[0]["Algorithm"], "FCFS")
        self.assertGreaterEqual(metrics.results[0]["Average_WT"], 0)
        self.assertGreaterEqual(metrics.results[0]["Average_TAT"], 0)
        self.assertGreaterEqual(metrics.results[0]["Average_RT"], 0)

        self.assertEqual(
            scheduler_fcfs.average_waiting_time,
            metrics.results[0]["Average_WT"]
        )

        metrics.export_to_csv("test_metrics.csv")

        self.assertTrue(os.path.exists("test_metrics.csv"))

if __name__ == "__main__":
    unittest.main()