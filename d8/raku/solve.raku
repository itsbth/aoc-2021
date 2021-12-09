sub to-bits($seg) {
    $seg.sort.
}
sub solve-seg(@numbers) {

}
my $sum = 0;
for lines().map(*.split(' | ')>>.split(' ')) {
    my @b = $_[1];
    my @m = @b.grep(so *.chars == 2 | 4 | 3 | 7);
    say @m;
    $sum += +@m;
}

say "Part 1: $sum";
