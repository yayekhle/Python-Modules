def count_days(current, total):
    if current > total:
        print("Harvest time!")
        return
    print("Day", current)
    count_days(current + 1, total)


def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))
    count_days(1, n)
