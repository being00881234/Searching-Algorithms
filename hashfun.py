#hash function

def hashfuns(hashtbl,key):
     if  hashtable[key%10]==key:
             return ((key%10)+1)
     else:
             return None
   


#h table has 10 element(none)

hashtable=list()
for _ in range(10):
    hashtable.append(None)


array=[34,16,2,93,80,77,51]
#for _ in range(10):
#    array.append(int(input("the element: ")))

for elem in range(0,len(array)):
    hashtable[array[elem]%10]=array[elem]

if hashfuns()==None:
    print("Key not found in the array.")
else:
    print(f"Key is found in {((key%10)+1)}")

print(hashtable)
print(hashfuns(hashtable,51))










print(hashtable)