input_list = eval(input())
for i in range(len(input_list)):
    for j in range(i+1, len(input_list)):
        ij = int(str(input_list[i]) + str(input_list[j]))
        ji = int(str(input_list[j]) + str(input_list[i]))
        if ji > ij:
            input_list[i], input_list[j] = input_list[j], input_list[i]
input__list = [str(i) for i in input_list]
input__list = ''.join(input__list)
print(input__list)
