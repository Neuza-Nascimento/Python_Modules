def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive_days(i):
        if i <= days:
            print(f"Day {i}")
            recursive_days(i + 1)
        else:
            return
    recursive_days(1)
    print("Harvest time!")
