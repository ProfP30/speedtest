import numpy as np

END_LOOP = 1_000_000_000 # 1 Mrd.

def main():
    # make sure to size the index variable big enough; python crashes elsewise
    i = END_LOOP
    last_number = 0
    # Loop through the numpy array as list, 2nd variation
    for i in list(np.arange(END_LOOP)):
        last_number += 1

    print(f"Python(Numpy #3):{last_number=}")

main()