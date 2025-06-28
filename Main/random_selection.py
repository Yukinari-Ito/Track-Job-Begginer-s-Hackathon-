from selection import selection_values
import random

def shuffled_selection_values(): 
    selection_dict = selection_values()
    shuffled_selection_dict = {}

    keys = list(selection_dict.keys())

    # Shuffle the list of keys
    random.shuffle(keys)

    # Iterate through the dictionary using the shuffled keys
    for key in keys:
        shuffled_selection_dict[key] = selection_dict[key]

    return shuffled_selection_dict