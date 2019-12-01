#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.30);
use experimental qw(signatures);

my ($total, $total2);
while (<>) {
    chomp;
    $total += fuel_req($_);
    $total2 += fuel_req_tot($_);
}

say "part 1: $total";
say "part 2: $total2";

sub fuel_req($n) {
    return int($n/3) - 2;
}

sub fuel_req_tot($n) {
    my $res = fuel_req($n);
    return $res <= 0 ? 0 : $res + fuel_req_tot($res);
}
