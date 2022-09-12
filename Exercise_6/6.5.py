number_list = [1, 2, 3, 4, 5, 6]
new_list = []

def function(new_list):
    for i in number_list:
        if i % 2 == 0:
            x = i
            new_list.append(x)
    return new_list

print(f"The original list is : {number_list}")
print(f"The even list is :{function(new_list)}")
