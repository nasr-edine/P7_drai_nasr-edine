# your_list = 'abcdefghijklmnopqrstuvwxyz'
your_list = 'abc'
complete_list = []

for current in range(3):
    a = [i for i in your_list]
    # print("a: ", a)
    # print("current: ", current)

    for y in range(current):
        # print("y: ", y)
        # print("current: ", current)
        # print("y: ", y)
        # print("before a: ", a)

        a = [x+i for i in your_list for x in a if i not in x]
        # matrix = [[k+l for l in your_list] for k in a]

        # print("after matrix: ", matrix)
        print()
        print("after a: ", a)
    complete_list = complete_list+a


# for x in complete_list:
#     print(x)
