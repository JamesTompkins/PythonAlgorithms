import random
import matplotlib.pyplot as plot
import time

numberAmount = 1000

def main():
    print("Creating {} random numbers.".format(numberAmount))
    numbers = [random.randrange(100) for i in range(numberAmount)]
    
    plotgraph(numbers, "Start")
    
    testspeed(bubblesort, numbers)
    testspeed(sorted, numbers)


###This takes a sorting function and tests how fast it works
def testspeed(function, array):
    starttime = int(round(time.time() * 1000))
    function(array)
    endtime = int(round(time.time() * 1000))
    print("{}: {} ms".format(function.__name__, endtime - starttime))
    
    
    
def plotgraph(arr, name):
    plot.stem(range(len(arr)), arr, '-', use_line_collection=True)
    plot.savefig('{0}.png'.format(name))
    plot.show()
 
    
##SORTING ALGORITHMS###

def bubblesort(arr):
    length = len(arr) - 1
    
    while (length > 0):
        for i in range (length):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        length -= 1
    return arr

    
main()