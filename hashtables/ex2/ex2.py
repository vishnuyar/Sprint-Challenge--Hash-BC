#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    if hashtable.capacity < length:
        hash_table_resize(hashtable)
    #print("i am hre",len(route))
    #Insert tickets into hashtable
    for ticket in tickets:
        #print('t',ticket.source,ticket.destination)
        if ticket.source == 'NONE':
            route[0] = ticket.destination
            #print('s',ticket.destination)
        elif ticket.destination == 'NONE':
            route[-1] = ticket.source
            #print('d',ticket.source)
        else:
            hash_table_insert(hashtable,ticket.source,ticket.destination)
        

    #Get the trip details:
    for index,trip in enumerate(route[:-1]):
        if index != 0:
            route[index] = hash_table_retrieve(hashtable,route[index-1])
            #print(route[index])
            
    return route[:-1]        



