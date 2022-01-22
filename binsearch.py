fout = open("binsearch.out", "w")

with open("binsearch.in", "r") as f:
    useless = f.readline()
    arr = list(int(i) for i in f.readline().split())
    n = int(f.readline())
    req = list(int(i) for i in f.readline().split())

def searchFirst(arr, key):
    l = -1  
    r = len(arr)

    if (arr[0] > key or arr[r - 1] < key): return -1

    while (r - l > 1):
        c = (l + r) // 2
        if (arr[c] < key): l = c
        else: r = c
    
    if (arr[r] == key): return r + 1

    return -1

def searchLast(arr, key):
    l = -1  
    r = len(arr)

    if (arr[0] > key or arr[r - 1] < key): return -1

    while (r - l > 1):
        c = (l + r) // 2
        if (arr[c] <= key): l = c
        else: r = c
    
    if (arr[r - 1] == key): return r

    return -1

for i in range(n):
    n = req[i]
    print(str(searchFirst(arr, n)) + ' ' + str(searchLast(arr, n)), file=fout)