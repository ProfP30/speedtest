import numpy as np

END_LOOP: int = 1_000_000_000

def main():
    # Loop through the numpy array as list, 2nd variation
    for i in list(np.arange(END_LOOP)):
        pass

    print(f"last number:{i}")

main()