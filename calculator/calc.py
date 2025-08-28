import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class Calculator:

    def __init__(self, addition, subtraction, multiplication, division, percentage):
        self.addition = addition
        self.subtraction =  subtraction
        self.multiplication = multiplication
        self.division = division
        self.percentage = percentage