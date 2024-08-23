import numpy as np

END_LOOP: int = 1_000_000_000

def main():
    # Loop through the numpy array as list
    for i in np.arange(END_LOOP).tolist():
        last_number = i

    print(f"{last_number=}")

main()