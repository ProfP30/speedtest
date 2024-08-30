<?php
define('END_LOOP', 1000000000); // 1 Mrd.

function main() {
    $last_number = 0;
    for ($i = 0; $i < END_LOOP; $i++) {
        $last_number += 1;
    }

    echo "PHP:last_number=$last_number\n--";
}

main();
?>

