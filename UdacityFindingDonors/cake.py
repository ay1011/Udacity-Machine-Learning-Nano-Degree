# [1, 7, 3, 4]    => [84, 12, 28, 21]
# [2, 3, 4, 5, 6] => [360, 240, 180, 144, 120]
from time import time

def getProductsOfAllIntsExceptAtIndex(List):
    if len(List) < 2:
        raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')

    products_of_all_ints_except_at_index = [None] * len(List)

    # for each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(List)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= List[i]

    # print products_of_all_ints_except_at_index

    # for each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    for i in range(len(List)-1,-1,-1): #4,3,2,1,0
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= List[i]

    return products_of_all_ints_except_at_index

def slow(List):
    if len(List) < 2:
        raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')

    res = [reduce(lambda x, y: x * y, List[0:j]+List[j+1:]) for j in range(len(List))]
    return res


N=601
start = time()
#print getProductsOfAllIntsExceptAtIndex(list(range(1,N,1)))
getProductsOfAllIntsExceptAtIndex(list(range(1,N,1)))
end = time()
print "time taken:", end - start

start2 = time()
#print slow(list(range(1,N,1)))
slow(list(range(1,N,1)))
end2 = time()
print "time taken:", end2 - start2



