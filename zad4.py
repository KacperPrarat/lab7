def find_max(dict):
    max=0
    for number in dict:
        if number > max:
            max = number
    return max



dict1 = {1:10,2:7,3:8,4:15,5:14,6:3,7:2}
print(find_max(dict1))