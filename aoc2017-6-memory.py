#
# Advent of Code, 2017 - Day 6
#

#
# Data
#
data = "4\t10\t4\t1\t8\t4\t9\t14\t5\t1\t14\t15\t0\t15\t3\t5"


#
# PART 1
#
def memory1(puzzle_input):
    banks = puzzle_input.split("\t")
    for i in range(len(banks)):
        banks[i] = int(banks[i])

    states = []
    cycles = 0

    print(banks)
    print()

    while ' '.join(map(str, banks)) not in states:
        cycles += 1
        states.append(' '.join(map(str, banks)))

        print("***********", cycles, "*************")
        bank = 0

        for i in range(len(banks)):
            if banks[i] > banks[bank]:
                bank = i

        pool = banks[bank]

        pointer = "   " * bank + " V "
        print("\t", pointer, bank)
        print("\t", banks)
        banks[bank] = 0

        while pool > 0:
            bank += 1
            bank = bank % len(banks)

            line = "   " * bank + " " + str(pool)
            print("\t", line)
            line = "   " * bank + " V"
            print("\t", line)
            print("\t", banks)

            banks[bank] += 1
            pool -= 1

            print("\t", banks)
            print()

        print("\t", banks)
        print()

    print("Total Cycles:", cycles)
    return


memory1(data)


#
# PART 2
#
def memory2(puzzle_input):
    banks = puzzle_input.split("\t")
    for i in range(len(banks)):
        banks[i] = int(banks[i])

    states = []
    cycles = 0

    print(banks)
    print()

    while ' '.join(map(str, banks)) not in states:
        cycles += 1
        states.append(' '.join(map(str, banks)))

        # print("***********", cycles, "*************")
        bank = 0

        for i in range(len(banks)):
            if banks[i] > banks[bank]:
                bank = i

        pool = banks[bank]

        # pointer = "   " * bank + " V "
        # print("\t", pointer, bank)
        # print("\t", banks)
        banks[bank] = 0

        while pool > 0:
            bank += 1
            bank = bank % len(banks)

            # line = "   " * bank + " " + str(pool)
            # print("\t", line)
            # line = "   " * bank + " V"
            # print("\t", line)
            # print("\t", banks)
            #
            banks[bank] += 1
            pool -= 1

        #     print("\t", banks)
        #     print()
        #
        # print("\t", banks)
        # print()

    length = len(states) - states.index(' '.join(map(str, banks)))
    print("Total Cycles:", cycles)
    print("Loop length:", length)

    return


memory2(data)
