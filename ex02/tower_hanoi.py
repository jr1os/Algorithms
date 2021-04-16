num_recursive = 0


def _tower_hanoi_recursive(num_disk, beg, end, aux):
    global num_recursive
    num_recursive += 1
    if num_disk == 1:
        print(f'{beg}->{end}: {num_disk}')
        return
    _tower_hanoi_recursive(num_disk-1, beg, aux, end)
    print(f'{beg}->{end}: {num_disk}')
#    __import__("ipdb").set_trace()
    _tower_hanoi_recursive(num_disk-1, aux, end, beg)


def hanoi(num_disk):
    global num_recursive
    num_recursive = 0
    _tower_hanoi_recursive(num_disk, beg="A", end="B", aux="C")


if __name__ == "__main__":
    for i in range(1, 5):
        print(f"#### hanoi {i} disk ")
        hanoi(i)
        print(f"**** {num_recursive} recursive call")
