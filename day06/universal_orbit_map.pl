#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.30);
use experimental qw(signatures);
use Graph::Undirected;
use List::Util qw(sum);

my $g = Graph::Undirected->new;
while (<>) {
    chomp;
    my @a = split /\)/;
    $g->add_edge(split /\)/);
}

my $sum = 0;
for my $v ($g->vertices) {
    my @a = $g->SP_Dijkstra("COM", $v);
    $sum += @a - 1;
}
say "Part 1: $sum";

my @path = $g->SP_Dijkstra("YOU", "SAN");
say "Part 2: ", @path - 3;
