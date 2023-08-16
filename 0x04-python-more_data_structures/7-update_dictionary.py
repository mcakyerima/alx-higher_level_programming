#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        updater = {key: value}
        a_dictionary.update(updater)
        return(a_dictionary)
    else:
        return None
