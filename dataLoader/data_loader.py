class DataLoader:

    def __init__(self, dataset, window_size=100, left=0):
        self.dataset = dataset
        self.window_size = window_size
        self.left = left
        self.right = self.left + self.window_size
    
    def current_data_window(self):
        return self.dataset.iloc[self.left:self.right]

    def next_window(self):
        try:    
            usr_input = int(input("How many steps want to move the window?\n"))
            if usr_input<0:
                if self.left<(-usr_input):
                    return IndexError
            elif usr_input>=0:
                self.right = self.right + usr_input
                self.left = usr_input + self.left
                return self.dataset.iloc[self.left:self.right]
        except Exception as e:
            return f"Error {e}"