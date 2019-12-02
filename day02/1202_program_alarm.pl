#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.30);
use experimental qw(signatures);

my @pgm;
while (<>) {
    @pgm = map { $_ + 0 } split ",";
}

say "Part 1: ", run_intcode(\@pgm, 12, 2);

for my $noun (0..99) {
    for my $verb (0..99) {
        if (run_intcode(\@pgm, $noun, $verb) == 19690720) {
            say "Part 2: ", 100 * $noun + $verb;
        }
    }
}

sub run_intcode($pgm_init, $noun, $verb) {
    my @pgm = @$pgm_init;
    $pgm[1] = $noun;
    $pgm[2] = $verb;
    my $i = 0;

    while (1) {
        if ($pgm[$i] == 1) {
            $pgm[$pgm[$i+3]] = $pgm[$pgm[$i+1]] + $pgm[$pgm[$i+2]];
        } elsif ($pgm[$i] == 2) {
            $pgm[$pgm[$i+3]] = $pgm[$pgm[$i+1]] * $pgm[$pgm[$i+2]];
        } elsif ($pgm[$i] == 99) {
            return $pgm[0];
        } else {
            say "Unknown opcode of $pgm[$i] at position $i";
            say "@pgm";
            last;
        }
        $i += 4;
    }
}
