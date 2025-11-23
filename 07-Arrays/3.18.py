def seclar(array):
    a=array[:]
    a.remove(max(a))
    return max(a)
def dif(array):
    return(max(array)-min(array))
def med(array):
    return array[len(array)//2]
def smlg(array):
    ar=[min(array),max(array)]
    return ar
def minus(array):
    res=''
    for i in array:
        res+=str(i)+'-'
    return res[:-1]
arr=[7,3,8,5,2]
print('Numbers: ',*arr)
print('Second largest number: ', seclar(arr))
print('Diference between the largest and smallest numbers: ', dif(arr))
print('Median: ', med(arr))
print('Smallest and largest number: ', *smlg(arr))
print('Numbers as a string: ', minus(arr))