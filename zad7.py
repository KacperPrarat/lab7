dicta = {1: 10,2: 20,3: 30,4: 40}
dictb = {1:11,3:33,5:55}
def sum_dictionaries(dict1,dict2):
    newdict={}
    for i in range(list(dict1.keys())[-1]):
        if not i in dict1.keys():
            continue
        if not i in dict2.keys():
            continue
        x = (dict1[i])
        z = (dict2[i])
        wynik = x + z
        newdict.update([[i, wynik]])
    return newdict


print(sum_dictionaries(dicta,dictb))
