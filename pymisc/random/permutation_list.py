if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    il = [ i for i in range(x + 1)]
    jl = [ j for j in range(y + 1)]
    kl = [ k for k in range(z + 1)]
    lol = [ [i,j,k] for i in il for j in jl for k in kl if i + j + k != n ]
    print (lol)
    print (sorted(lol, key = lambda i: (len(i), i)))
