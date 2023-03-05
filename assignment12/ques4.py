#4. Write a Python program to convert key-values list to flat dictionary?

def key_values_to_dict(key_values_list):
    """
    Converts a list of key-value pairs into a flat dictionary.
    """
    flat_dict = {}
    for key, value in key_values_list:
        flat_dict[key] = value
    return flat_dict

# Example usage
key_values_list = [('a', 1), ('b', 2), ('c', 3)]
flat_dict = key_values_to_dict(key_values_list)
print(flat_dict)  

