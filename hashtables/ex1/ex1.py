#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    solution = None
    if ht.capacity < length:
        ht = hash_table_resize(ht)
    
    #inserting the weights in a hash table
    for index,weight in enumerate(weights):
        hash_table_insert(ht,weight,index)

    #checking for items which statisfy the limit criteria    
    for index,weight in enumerate(weights):
        balance_weight = limit - weight
        found_item = hash_table_retrieve(ht,balance_weight)
        if (found_item):
            if (found_item != index):
                if found_item > index:
                    
                    solution = (found_item,index)
                    
                else:
                    solution = (index,found_item)
                    
    return solution 
 

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
