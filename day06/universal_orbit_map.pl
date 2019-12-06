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

my $sptg = $g->SPT_Dijkstra("COM");
{
    no warnings 'uninitialized';
    say 'Part 1: ', sum map {$sptg->get_vertex_attribute($_, 'weight')} $sptg->vertices;
}

my @path = $g->SP_Dijkstra("YOU", "SAN");
say "Part 2: ", @path - 3;
