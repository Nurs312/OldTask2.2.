first_list = input("Enter any list: ").split()
second_list = input('Enter second list: ').split()
new_list = []
for item in first_list:
    if item not in second_list:
        new_list.append(item)
        print(new_list)
