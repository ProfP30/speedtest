const END_LOOP = 1_000_000_000 // 1 Mrd.

function main() {
	let last_number = 0

	for (let i = 0; i < END_LOOP; i++) {
		last_number++
	}
	
    console.log("JavaScript:last_number=" + last_number + "\n--")
}

main()
