END_LOOP = 1_000_000_000 # 1 Mrd.

def main
    last_number = 0
    END_LOOP.times do
        last_number += 1
    end

    puts "Ruby:last_number=#{last_number}\n--"
end

main
