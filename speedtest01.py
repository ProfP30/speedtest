END_LOOP = 1_000_000_000 # 1 Mrd.

def main():
    last_number = 0
    for _ in range(END_LOOP):
        last_number += 1

    print(f"Python:{last_number=}\n")

main()
