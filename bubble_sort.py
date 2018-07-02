for i in range(int(input("How many numbers do you want to be in your list?"))):
    nums= [input("What list of numbers do you want to sort using the power of BUBBLES? Here's a number:")]
to_sort=[nums]

for i in range(0, len(to_sort)):
    for j in range (i+1, len(to_sort)):
        if to_sort[i]> to_sort[j]:
            val=to_sort[i]
            to_sort[i]=to_sort[j]
            to_sort[j]=val

print(to_sort)