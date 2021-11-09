from Hamster import Hamster


def get_total_consumption(hamsters, number_of_hamsters):
    total_consumption_array = []
    for hamster in hamsters:
        total_consumption_array.append(hamster.get_hamster_total_consumption(number_of_hamsters))
    total_consumption_array.sort()
    return sum(total_consumption_array[:number_of_hamsters])


def buy_hamsters(hamsters, food_package_number, number_of_hamsters):
    start = 0
    end = number_of_hamsters
    while end > start + 1:
        middle = start + (end - start) // 2
        if get_total_consumption(hamsters, middle) > food_package_number:
            end = middle
        else:
            start = middle
    if get_total_consumption(hamsters, end) <= food_package_number:
        return end
    else:
        return start


def main():
    try:
        hamsters_input = open("hamsters.in")
        food_package_number = int(hamsters_input.readline())
        number_of_hamsters = int(hamsters_input.readline())
        hamsters = []
        line = hamsters_input.readline()
        while line:
            hamster_info = line.split()
            hamsters.append(Hamster(int(hamster_info[0]), int(hamster_info[1])))
            line = hamsters_input.readline()
        hamsters_output = open("hamsters.out", "w")
        hamsters_output.write(f'You can buy {buy_hamsters(hamsters, food_package_number, number_of_hamsters)} hamsters')
        hamsters_input.close()
        hamsters_output.close()
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()
