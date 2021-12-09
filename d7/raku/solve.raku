my @ns = slurp().split(',')>>.Int;

sub move-cost(@ns, $pos) {
    return @ns.map(* - $pos)>>.abs.map(-> $n { Range.new(1, $n).sum }).sum
}

# my $pos = (@ns.sum / +@ns).round;
# say $pos;
my $mc = Inf;
for @ns.minmax {
    my $nc = move-cost(@ns, $_);
    if $nc < $mc {
        say $_, ' ', $nc;
        $mc = $nc
    }
}

say "Part 1: ", $mc;
