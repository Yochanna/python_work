for n in range(1, 10):
    if n == 1:
        suffix = "st"
    elif n == 2:
        suffix = "nd"
    elif n == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{n}{suffix}")
