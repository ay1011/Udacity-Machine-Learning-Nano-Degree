arr = [2,3,5,7,11,13]
tot = 20
def pairwithsum(array,total):
    if len(array) < 2:
        print("require at leat 2 number to sum")
    firstpoint = 0
    finalpoint = len(array)-1

    while finalpoint - firstpoint  > 1:
        s = array[firstpoint] + array[finalpoint]
        if s == total:
            return str(array[firstpoint])+' + '+ str(array[finalpoint]) + ' = '+ str(total) + "  " + str(s == total)
        elif s > total:
            finalpoint -=1             #print('finalpoint',finalpoint)
        elif s < total:
            firstpoint +=1             #print('firstpoint',firstpoint)

    return str(array[firstpoint])+' + '+ str(array[finalpoint]) + ' != '+ str(total) + \
           "  " + str(array[firstpoint] + array[finalpoint] == total)

for tot in range(1,26,1):
    print(pairwithsum(arr,tot))

