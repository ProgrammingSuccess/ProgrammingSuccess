# write code to output the star pattern (from one star up to 5 stars, and back down to one star) using an if-else statement in combination with a single for loop
pattern = "*"
for num in range(1, 10):
    #pattern
    to_print = pattern*num
    # set a turn point at 5 stars
    if num > 5:
        count_down = 10 - num
        to_print = pattern*count_down
        # reverse the pattern

    print(to_print)