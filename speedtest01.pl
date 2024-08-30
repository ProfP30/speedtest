#!/usr/bin/env perl
use strict;
use warnings;

use constant END_LOOP => 1_000_000_000; # 1 Mrd.

my $last_number = 0;

for (my $i = 0; $i < END_LOOP; $i++) {
    $last_number++;
}

print "Perl:last_number=$last_number\n--\n";