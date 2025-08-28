import tkinter as tk
from ttkbootstrap import Style
from logic import CalculatorManager
import json
import keyboard



cal_manager = CalculatorManager()
file_path = cal_manager.resource_path("records.json")


def launch():
    style =Style("darkly") #modern theme darkly, flatly etc
    root = style.master
    root.title("Calculator")
    root.geometry("500x600")

    def show_history():
        history_window = tk.Toplevel(root)
        history_window.title("History")
        history_window.geometry("500x600")

        #try to read history from json
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        #Display the history
        text_area = tk.Text(history_window, wrap=tk.WORD)
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

        if data:
            for item in data:
                text_area.insert(tk.END, f"{item}\n")
        else:
            text_area.insert(tk.END, "No records found")

        text_area.config(state=tk.DISABLED) #make it read only

    entry = tk.Entry(root, font=("Helvetica", 20)) # type: ignore
    entry.pack(fill="both", padx=20, pady=20)


    def on_key_press(event):
        key = event.char.lower()
        special_keys = {
            '\r':'=', #Enter key as "="
            '\x08':'C', #Backspace as clear
            'h':'H', #Show History
            'd':'D' #Delete History
        }

        if key in '0123456789+/*-.%':
            button_click(key)
        elif key in special_keys:
            button_click(special_keys[key])



    def button_click(value):
        current = entry.get()
        if value == "=":
            expression = current
            for op in ['+', '-', '*', '/', '%']:
                expression = expression.replace(op, f" {op} ")
            exp_list = expression.strip().split()
            if cal_manager.is_valid_operations(exp_list):
                try:
                    result = cal_manager.evaluate_expression(exp_list)
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, str(result))

                    #save result and expression
                    records = ({
                        "Expression":exp_list,
                        "Result":result
                    })
                    cal_manager.save_results(records, file_path)
                except ZeroDivisionError:
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, "Math Error")
            else:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Invalid Input")
        elif value == "C":
            entry.delete(0, tk.END)

        elif value == "D":
            cal_manager.delete_records(file_path)

        elif value == "H":
            show_history()
        else:
            if value in ['+', '-', '*', '/']:
                entry.insert(tk.END, f" {value} ")
            else:
                entry.insert(tk.END, value)


    #add button using loops
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", " .", "%", "+"],
        ["H", "C", "=", "D"]
        
    ]
 
    #create frame
    button_frame = tk.Frame(root)
    button_frame.pack(fill="both", expand=True)


   


    for row in buttons:
        row_frame = tk.Frame(button_frame)
        row_frame.pack(expand=True, fill="both")
        for btn_text in row:
            btn = tk.Button(row_frame, text=btn_text, font=("Helvetica", 16), command= lambda val=btn_text: button_click(val))
            btn.pack(side="left", expand=True, fill="both")

    root.bind("<Key>", on_key_press) # connect the function with button click function

    root.mainloop()


if __name__ == "__main__":
    launch()