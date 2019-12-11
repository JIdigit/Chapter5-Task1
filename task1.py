




def main():

    number_of_tries = int(input('Enter number of tries: '))
    string_list = [[ord(j) for j in input("Input a string up to 10 characters:")] for _ in range(number_of_tries) ]
    reverse_list = []
    normal_funny = []
    reverse_funny = []

    for i  in string_list:
        reverse_list.append([i[-j] for j in range(1, len(i)+1)])

    for i in string_list:
        normal_funny.append([abs(i[j]-i[j+1]) for j in range(len(i)) if j != i.index(i[-1])])
    
    for i in reverse_list:
        reverse_funny.append([abs(i[j]-i[j+1]) for j in range(len(i)) if j != i.index(i[-1])])
    for i in range(number_of_tries):
        if reverse_funny[i] == normal_funny[i]:
            print("Funny")
        else:
            print('Not Funny')




    # print(normal_funny)
    # normal_funny = [abs(i[j]-i[j+1]) for i in string_list for j in range(len(stsring_list)) if j != string_list.index(i[-1])]
    # reverse_string = [string_list[-i] for i in range(1,len(string_list)+1) for _ in range(number_of_tries)]
    # print (string_list)
    # normal_funny = [abs(string_list[i]-string_list[i+1]) for i in range(len(string_list))if i != string_list.index(string_list[-1])]
    # reverse_funny = [abs(reverse_string[i]-reverse_string[i+1]) for i in range(len(reverse_string))if i != reverse_string.index(reverse_string[-1])]
    # if normal_funny == reverse_funny:
    #     print('Funny')
    # else:
    #     print('Not Funny')












if __name__ == "__main__":
    main()