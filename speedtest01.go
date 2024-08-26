// compile with:
// go run speetest01.go

package main

import "fmt"

const END_LOOP uint = 1_000_000_000

func main() {
	var last_number uint

	for i := uint(0); i < END_LOOP; i++ {
		last_number = i
	}
	fmt.Printf("last_number=%d\n", last_number)
}
