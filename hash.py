# HashT able class using chaining.
class PackageHashTable:

    '''
     Constructor with 10 buckets
    Assigns all buckets with an empty list.
    Time Complexity: O(1)
    Space Complexity: O(N)
    '''
    def __init__(self, initial_capacity=10):
        # initialize the hash table with 10 empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    '''
      Inserts a new item into the hash table.
      Does both insert and update to the hash table
      Get the bucket list where this item will go by using the key % 10 as key
      Time Complexity: O(N)
      Space Complexity: O(N)
      '''

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)  # key % 10
        bucket_list = self.table[bucket]  # add to appropriate bucket list

        # update key if it is already in the bucket
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = item
                return True

        # if the key is not already there, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    '''
    Searches for an item with matching key in the hash table.
    Returns the item if found.
    Time Complexity: O(N)
    Space Complexity: O(N)
    '''
    def search(self, key):
        # get the bucket and then the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]


        # search for the key within the bucket list
        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                return key_value[1]  # value
        return None

    '''
     Removes an item with the matching key from the hash table.
     Time Complexity: O(N)
     Space Complexity: O(N)
    '''
    def remove(self, key):
        #get the bucket list
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # if the item exists in the bucket list, remove the item
        for key_value in bucket_list:

            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
