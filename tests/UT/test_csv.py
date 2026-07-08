import unittest
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from utils.ReadCsv import read_processes_from_csv


class TestCSVReader(unittest.TestCase):

    def test_read_csv(self):
        processes = read_processes_from_csv("tests/testcsv.csv")

        self.assertEqual(len(processes), 5)

        self.assertEqual(processes[0]["burst_time"], 5)
        self.assertEqual(processes[0]["priority"], 2)
        self.assertEqual(processes[0]["arrival_time"], 0)

        self.assertEqual(processes[4]["burst_time"], 2)
        self.assertEqual(processes[4]["priority"], 1)
        self.assertEqual(processes[4]["arrival_time"], 4)
        


if __name__ == "__main__":
    unittest.main()