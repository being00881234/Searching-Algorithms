def binary_search(arr, key):
        
    def binopr():
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    result=binopr()
    if result != -1:
        return(f"Element {key} is found at index {result+1}")
    else:
        return(f"Element {key} is not found in the array")



arr =list()
for _ in range(int(input("No Of element you need to add to the list: "))):
    arr.append(int(input()))


key =int(input("The thing to search for: ")) 

print(arr)
print(key)
print(binary_search(arr,key))
