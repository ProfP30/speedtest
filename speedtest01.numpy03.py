import numpy as np

END_LOOP: int = 1_000_000_000

def main():
    # Loop through the numpy array as list, 2nd variation
    for i in list(np.arange(END_LOOP)):
        last_number = i

    print(f"{last_number=}")

main()