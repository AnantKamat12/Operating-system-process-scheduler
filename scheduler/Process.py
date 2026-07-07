import time
import random
import os
class Process:
    def __init__(self, process_id, burst_time, priority, arrival_time):
        # We encrypt the sequential process_id immediately upon initialization
        self.pid=process_id
        self.process_id = self._encrypt_id(process_id)
        
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.arrival_time = arrival_time
        self.completion_time=None
        self.respnse_time=None

    def _encrypt_id(self, val):
        """
        A simple 16-bit Feistel Cipher to obfuscate sequential IDs.
        Guarantees unique, non-repeating outputs for inputs 0 to 65535.
        """
        # A secret key or seed to change the 'randomness' pattern
        SECRET_KEY = random.randint(1, 255)  # Random key between 1 and 255 for scrambling
        
        # Split the ID into two 8-bit halves (since 2^16 = 65536)
        left = (val >> 8) & 0xFF
        right = val & 0xFF
        
        # Run 4 rounds of scrambling
        for round_num in range(4):
            # A simple mathematical function to scramble the bits
            f = ((right ^ SECRET_KEY) + round_num) & 0xFF
            next_right = left ^ f
            left = right
            right = next_right
            
        # Recombine the two halves back into a single unique integer
        encrypted_val = (left << 8) | right
        return encrypted_val

    def addnumber(self,x,y):
        return x+y


    def __str__(self):
        return (f"Process PID: {self.pid}, Process Encrypt ID: {self.process_id}, Burst Time: {self.burst_time}, Priority: {self.priority}, "
                f"Remaining Time: {self.remaining_time}, Waiting Time: {self.waiting_time}, Turnaround Time: {self.turnaround_time}, "
                f"arrival_time: {self.arrival_time}, "
                f"completion_time: {self.completion_time}, response_time: {self.respnse_time}")

