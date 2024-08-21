const END_LOOP = 1_000_000_000

function main() {
	let last_number = 0

	for (let i = 0; i < END_LOOP; i++) {
		last_number = i
	}
	
    console.log("last_number=" + last_number)
}

main()
