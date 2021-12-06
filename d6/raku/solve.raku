my @fish = slurp.split(',')>>.Int;

my @days = 0 xx 7;
for @fish {
    @days[$_] += 1;
}

my @pending = (0, 0);

for 0..255 {
    # say @days, " = {@days.sum + @pending.sum}";
    # say " " x (1 + (2*($_%7))), "^";
    @pending.append(@days[$_ % 7]);
    @days[$_ % 7] += @pending.shift;
    if $_ == 79 {
        say "Part 1: ", @days.sum + @pending.sum;
    }
}

say "Part 2: ", @days.sum + @pending.sum;
