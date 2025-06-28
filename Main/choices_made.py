class choices_made():
    def __init__(self):
        self.choices_dict = {}
    
    def save_choice(self, key, value):
        self.choices_dict[key] = value

    def return_choices(self):
        return self.choices_dict