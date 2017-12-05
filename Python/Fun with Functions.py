def odd_even():
    for i in range(1, 2000):
        if i % 2 == 0:
            print i, "this is an even number"
        else:
            print i, "this is an odd number"
odd_even()

def multiply(arr, num):
    for i in range(0, len(arr)):
        arr[i] *= num
    return arr
numbers_array = [2, 4, 9, 15, 75]
print multiply(numbers_array, 5)

def layered_multiples(arr):
    print arr
    new_array = []
    for i in arr:
        val_arr = []
        for i in range(0,i):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array
i = layered_multiples(multiply([2,4,5],3))
print i