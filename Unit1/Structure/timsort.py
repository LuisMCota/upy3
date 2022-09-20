def names_sort(l, nl=0, nr=None):
    if nr is None:
        nr = len(l) - 1

    for i in range(nl+1, nr+1):
        key = l[i]
        j = i-1
        while j>= nl and l[j] > key:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l

def order_data(l):
    run = 32
    a = len(l)

    for i in range(0,a,run):
        list_sort(l,i,min((i+run-1), (a-1)))

        size = run
        while size < a:
            for x in range(0,a, size2):
                mid_length = x+ size-1
                end_length = min((x+size2-1), (a-1))

                join = merge(nl=l[x:mid_length+1], nr=l[mid_length+1:end_length+1])

                l[x:x+len(join)] = join

        size *= 2
    return l

arr1 = ["Guicho", "Jorge", "Myke", "Jordan", "Carlos", "Celeste", "Abraham", "Abigail", "Barry", "Bryant", "Bad Bunny", "La Maravilla", "Pepe", "Jose", "Mariana", "Hector", "Luis", "Pedro", "Zamira", "Yuumi"]
arr_answer = names_sort(arr1)
print(arr_answer)