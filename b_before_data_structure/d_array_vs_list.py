# in C array
# int a[4] = {2,4,0,5}
# int 4 byte
# a[0] memory address 100
# a[2] memory address 100 + 4 + 4

# in python list
# a = [2,4,0,5]

# very important d_list.png
# a[2] = a[1] + 1
# it does not delete a[0] it redirects to new object

# capacity in C manually allocate the memory using malloc

# capacity in python dynamic array
# python does it for us
# if capacity is not enogh
# double the size of current array
# copy the values
# delete the past array
import sys
a = []
print(sys.getsizeof(a))
a.append(10)
print(sys.getsizeof(a))
a.append(12)
print(sys.getsizeof(a))


# sequetial data structure d_sequential_data_structure.png
# array, list
# stack, queue,dequeue
# stack: LIFO Last In First Out
# queue: FIFO First In First Out
# dequeue: stack + queue
# linked list: link the not connected node
# can search the item using index
