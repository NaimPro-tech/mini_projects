import os
import sys
import json
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class CalculatorManager:

    def __init__(self):
        pass

    
    def save_results(self, results, file_path):
        try:
            with open(file_path, "r+") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
                file.seek(0)
                data.append(results)
                json.dump(data, file, indent=4)
                file.truncate()
            return True
        except FileNotFoundError:
            with open(file_path, "w") as file:
                json.dump([results], file, indent=4)
            return True
        except Exception as e:
            print("Error saving result", e)
            return False
        
    def load_results(self, file_name="records.json"):
        file_path = self.resource_path(file_name)
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            return {"History":data, "Timestamp":str(datetime.utcnow())}
        except (FileNotFoundError, json.JSONDecodeError):
            return {"History": []}
    
    def delete_records(self, file_path):
        try:
            with open(file_path, "w") as file:
                json.dump([], file, indent=4)
                return True
        except json.JSONDecodeError:
            return False
    
    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
                
    @staticmethod
    def is_valid_operations(exp_list):
        operators = {'+', '-', '*', '/', '%'}

        for i in range(len(exp_list)):
            if i%2 == 0:
                try:
                    float(exp_list[i])
                except ValueError:
                    return False
            else:
                if exp_list[i] not in operators:
                    return False
        return True
    
    @staticmethod
    def evaluate_expression(exp_list):
        result = float(exp_list[0])
        i=1
        while i<len(exp_list):
            op = exp_list[i]
            next_item = exp_list[i+1]

            #check if next item is a percentage
            if isinstance(next_item, str) and next_item.endswith("%"):
                percent_value = float(next_item.strip("%"))

                #count percentage from previous number
                base = result if i==1 else float(exp_list[i-2])
                num = (percent_value/100)*base

            else:
                num = float(next_item)

            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            elif op == "/":
                if num == 0:
                    raise ZeroDivisionError("Cannot divide by Zero")
                result /= num
            elif op == "%":
                result = result * (num/100)
            i+=2
        return result


                    
