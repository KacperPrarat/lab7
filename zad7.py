dicta = {1: 10,2: 20,3: 30,4: 40}
dictb = {1:11,3:33,5:55}
def sum_dictionaries(dict1,dict2):
    newdict={}
    for i in dict1:

        x = (dict1[i])
        z = (dict2[i])
        wynik = x + z
        newdict[i] = wynik
    return newdict


print(sum_dictionaries(dicta,dictb))
