import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
import csv
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.csv"
        self.tm = TaskManager("test.csv")
        
    def tearDown(self):
        if os.path.exists("test.csv"):
            os.remove("test.csv")
    
    def test_save_task(self):
        task_list = [1, "Code", "Study", "25-08-2025 06:00:00 pm"]
        self.tm.save_task(task_list)

        with open(self.test_file, mode="r") as f:
            reader = csv.reader(f)
            rows = list(reader)
 
        self.assertEqual(rows[1][0], str(task_list[0]))
    
    def test_non_save_task(self):
        task_list = ["abc", "Code", "Study", "26-08-2025 06:00:00 pm"]
        
        with self.assertRaises(ValueError):
            self.tm.save_task(task_list)
    
    def test_remove_task(self):
        task_list = [1, "Code", "Study", "25-08-2025 06:00:00 pm"]
        self.tm.save_task(task_list)

        with open(self.test_file, mode="r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        self.assertEqual(rows[1][0], str(task_list[0]))

        self.tm.remove_task(task_id=task_list[0])

        with open(self.test_file, mode="r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        self.assertEqual(len(rows), 1)
    
    def test_update_task(self):
        task_list = [1, "Code", "Study", "25-08-2025 06:00:00 pm"]
        self.tm.save_task(task_list)

        self.tm.update_task(task_id=1, task="Write", additional_info="Exam")

        with open(self.test_file, mode="r") as f:
            reader = csv.reader(f)
            rows = list(reader)

        self.assertEqual(rows[1], ["1", "Write", "Exam", "25-08-2025 06:00:00 pm"])

    def test_search_task(self):
        task_list = [1, "Code", "Study", "25-08-2025 06:00:00 pm"]
        self.tm.save_task(task_list)

        # Search by task
        results = self.tm.search_task(task="Code")
        
        # কমপক্ষে একটা row এ 'Code' আছে কিনা চেক করো
        self.assertTrue(any(row[1] == "Code" for row in results))

        # Invalid id দিলে exception উঠবে
        with self.assertRaises(ValueError):
            self.tm.search_task(task_id=99)

        

    def test_task_list(self):
        task_list = [1, "Code", "Study", "25-08-2025 06:00:00 pm"]
        self.tm.save_task(task_list)

        with open(self.test_file, mode='r') as f:
            reader = csv.reader(f)
            rows = list(reader)
        
        self.assertListEqual(rows[1], ["1", "Code", "Study", "25-08-2025 06:00:00 pm"])



if __name__ == "__main__":
    unittest.main()