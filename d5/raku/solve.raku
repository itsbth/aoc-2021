my @lines = lines().map: {
    when /(<[0..9]>+)','(<[0..9]>+) ' -> ' (<[0..9]>+)','(<[0..9]>+)/ {
        ($0.Int, $1.Int) => ($2.Int, $3.Int);
    }
};

my %count is default(0);

for @lines -> $line {
    my ($x1, $y1) = $line.kv[0];
    my ($x2, $y2) = $line.kv[1];
    if $x1 != $x2 && $y1 != $y2 {
        # skip diagonals
        # next; # toggle comment to switch between part 1 and 2
        my @xr = $x1 < $x2 ?? ($x1..$x2).List !! ($x2..$x1).reverse;
        my @yr = $y1 < $y2 ?? ($y1..$y2).List !! ($y2..$y1).reverse;
        for @xr Z @yr -> ($x, $y) {
            %count{"$x,$y"} += 1;
        }
        next;
    }
    for ($x1 minmax $x2) X ($y1 minmax $y2) -> ($x, $y) {
        # index by string as I don't remember/can't figure out how to index by list
        %count{"$x,$y"} += 1;
    }
}

for 0..10 -> $y {
    for 0..10 -> $x {
        if %count{"$x,$y"}:exists {
            print %count{"$x,$y"};
        } else {
            print ".";
        }
    }
    say "";
}

say +%count.values.grep(*>1);
