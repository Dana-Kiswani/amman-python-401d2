
def binarySearch(arr, key):
    """
    This program search for the index of a given nubmer inside an array*

    """
    left = 0
    right = len(arr)-1
 
    while left <= right:
 
        mid = (left + right) // 2
        if key == arr[mid]:
            return mid

        elif key < arr[mid]:
            right = mid - 1

        else:
            left = mid + 1
 
    return -1

 
if __name__ == '__main__':
 
    arr = [11,22,33,44,55,66,77]
    key = 90

    idx = binarySearch(arr, key)
    if idx != -1:
        print("The index of the element is ..", idx)
    else:
        print("The element does not exists in the list")
