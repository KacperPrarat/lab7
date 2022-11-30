dict1= {1:10,2:7,3:8,4:15,5:14,6:3,7:2}
def find_max(dict1):
    naj = 0
    for klucz in dict1:
        if dict1[klucz] > naj:
            naj = dict1[klucz]
    return naj

print(find_max(dict1))
