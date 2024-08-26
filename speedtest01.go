// compile with:
// go run speetest01.go

package main

import "fmt"

const END_LOOP = 1_000_000_000 // 1. Mrd.

func main() {
	var last_number uint

	for i := uint(0); i < END_LOOP; i++ {
		last_number++
	}
	fmt.Printf("GO:last_number=%d\n", last_number)
}
