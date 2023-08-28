#!/usr/bin/python3
def magic_calculation(a, b):
    magic_calc = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                magic_calc += (a**b)/i
        except Exception:
            magic_calc = b + a
            break
    return magic_calc
