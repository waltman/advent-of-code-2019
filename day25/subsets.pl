#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.30);
use experimental qw(signatures);
use Algorithm::Combinatorics qw(subsets);

my @a = qw( hologram cake space_law_space_brochure loom mutex easter_egg manifold );
#my @a = qw( dog cat rat bat );

my $iter = subsets(\@a);
$" = ", ";
while (my $p = $iter->next) {
    next if @$p < 3;
    next if @$p > 5;
    say "@$p";
}

