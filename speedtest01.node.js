const end_loop = 1_000_000_000

function main() {
	let last_number

	for (let i = 0; i < end_loop; i++) {
		last_number = i
	}
	
    console.log(last_number)
}

main()
