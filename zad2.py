import math

def find_hypotenuse(cathetus1,cathetus2):
    """the function computes a hypotenuse
     of a triangle based on the given two catheti
    """
    hypotenus = math.sqrt(cathetus1**2 + cathetus2**2)
    return  hypotenus

def main():
    a = 3
    b = 4
    c = find_hypotenuse(a,b)
    print(a,b,c)

if __name__ == "__main__":
    main()