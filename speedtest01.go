// compile with:
// go run speetest01.go

package main

import "fmt"

const END_LOOP int = 1_000_000_000

func main() {
	var last_number int

	for i := 0; i < END_LOOP; i++ {
		last_number = i
	}
	fmt.Printf("last_number=%d\n", last_number)
}
