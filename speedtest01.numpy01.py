import numpy as np

END_LOOP = np.arange(1_000_000_000)

def main():
    # Loop through the numpy array
    for i in END_LOOP:
        last_number = i

    print(f"{last_number=}")

main()