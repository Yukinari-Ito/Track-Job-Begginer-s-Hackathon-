from .selection import selection_values
import random

def shuffled_selection_values():
    selection_dict = selection_values()
    keys = list(selection_dict.keys())
    random.shuffle(keys)
    return {key: selection_dict[key] for key in keys}