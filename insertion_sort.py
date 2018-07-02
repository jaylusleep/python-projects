#INCOMPLETE

to_sort = [230, 6, 3, 234565, 9, 13000]

def ins_sort():
    for i in range(0, len(to_sort)):
        j=i
        for j in range(1, j+1):
            if to_sort[j+1]<to_sort[j]:
                val=to_sort[j+1]
                to_sort[j+1]=to_sort[j]
                to_sort[j]=val

print(to_sort)