class choices_made():
    """
    choices_madeはインスタンス化して使う．
    choices_made = choices_made()のようにする．
    save_choiceを使うときは，
    choices_made.save_choices(key, value)という形で使う．
    selfは引数ではないので，特別何かを指定する必要はない．
    """
    def __init__(self):
        self.choices_dict = {}
    
    def save_choice(self, key, value):
        self.choices_dict[key] = value

    def return_choices(self):
        return self.choices_dict