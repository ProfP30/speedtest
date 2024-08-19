package main

import "fmt"

const end_loop int = 1_000_000_000

func main() {
	var last_number int

	for i := 0; i < end_loop; i++ {
		last_number = i
	}
	fmt.Printf("%d\n", last_number)
}
