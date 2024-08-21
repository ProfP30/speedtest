import numpy as np

# Create a numpy array as list (faster?)
end_loop = np.arange(1_000_000_000).tolist()

def main():
    # Loop through the numpy array
    for i in end_loop:
        last_number = i

    print(last_number)

main()