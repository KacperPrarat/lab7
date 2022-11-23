def find_max(dict):
    max=0
    for number in dict:
        if number > max:
            max = number
    return max

def merge_dictionaries(dict1,dict2):
    dict3 =dict1.copy()
    dict3.update(dict2)
    return dict3


def main():
    dict1 = {1: 10, 2: 7, 3: 8, 4: 15, 5: 14, 6: 3, 7: 2}
    dict2 = {8: 10, 9: 40, 10: 34, 11: 100}
    dict3 = merge_dictionaries(dict1,dict2)
    print(dict1,dict2,dict3)
