import numpy as np

# Create a numpy array with 1000 elements (0 to 999)
end_loop = np.arange(1_000_000_000)

def main():
    # Loop through the numpy array
    last_number: int
    for i in end_loop:
        # Your code goes here
        last_number = i

    print(last_number)

main()