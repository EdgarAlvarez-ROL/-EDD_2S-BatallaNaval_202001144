def display_hash(hashTable): 
      
    for i in range(len(hashTable)): 
        print(i, end = " ") 
          
        for j in hashTable[i]: 
            print("-->", end = " ") 
            print(j, end = " ") 
              
        print() 
  
HashTable = [[] for _ in range(13)]

  
def Hashing(keyvalue): 
    return keyvalue % len(HashTable) 
  
  
def insert(Hashtable, keyvalue, value): 
    
    hash_key = Hashing(keyvalue) 
    Hashtable[hash_key].append(value) 

def delete_in_hash(hashTable, x):
    for i in range(len(hashTable)): 
        for j in hashTable[i]: 
            if j == x:
                # print(x)
                hashTable[i].remove(x)
            


insert(HashTable, 10, 'Allahabad') 
insert(HashTable, 25, 'Mumbai') 
insert(HashTable, 20, 'Mathura') 
insert(HashTable, 9, 'Delhi') 
insert(HashTable, 21, 'Punjab') 
insert(HashTable, 21, 'Noida') 
  
display_hash(HashTable) 

delete_in_hash(HashTable, "Noida")

display_hash(HashTable) 