# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
def move_zeros(lst):
    count = lst.count(0)
    lst2 = []
    for i in lst:
        if i!= 0:
            lst2.append(i)

    for i in range(count):
        lst2.append(0)
    lst = lst2
    return lst
