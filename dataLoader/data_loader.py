class DataLoader:

    def __init__(self, dataset, window_size=100, left=0):
        self.dataset = dataset
        self.window_size = window_size
        self.left = left
        self.right = self.left + self.window_size
        self.end = False
    
    def current_data_window(self):
        return self.dataset.iloc[self.left:self.right]

    def forward_window(self):
        try:
            usr_input = int(input("How many steps want to move forward the window?\n"))

            if usr_input<0:
                return "Only positive integer allowed."

            elif usr_input == 0:
                return self.current_data_window()
            else:
                if self.end == False:
                    self.left += usr_input

                    if self.left >= len(self.dataset):
                        self.left-=usr_input
                        return "Out of dataset"
                        
                    self.right = min(self.left + self.window_size, len(self.dataset))

                    if self.right == len(self.dataset):
                        self.end=True

                    return self.dataset.iloc[self.left:self.right]

                if self.end == True:
                    return "Already Visited"

        except Exception as e:
            return f"Error {e}, Try Again"


    def backward_window(self):
        try:
            usr_input = int(input("How many steps want to move backward the window?\n"))

            if usr_input<0:
                return "Only positive integer allowed."

            self.end = False
            self.left -= usr_input
            if self.left<=0:
                self.left = 0
                self.right = min(self.left + self.window_size, len(self.dataset))
                return self.dataset.iloc[self.left:self.right]
            else:
                self.right = min(self.left + self.window_size, len(self.dataset))
                return self.dataset.iloc[self.left:self.right]

        except ValueError as e:
            return f"Error {e}"


if __name__ == "__main__":
    import pandas as pd

    df = pd.DataFrame({
        "value": list(range(1, 13))
    })

    loader = DataLoader(df, window_size=5)
    print(loader.current_data_window())
    print(loader.forward_window())
    print(loader.forward_window())
    print(loader.forward_window())
    print(loader.forward_window())
    print(loader.backward_window())
    print(loader.backward_window())