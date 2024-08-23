import numpy as np

END_LOOP = 1_000_000_000

def main():
    # make sure to size the index variable big enough; python crashes elsewise
    i = END_LOOP
    # Loop through the numpy array
    for i in np.arange(END_LOOP):
        last_number = i

    print(f"{last_number=}")

main()