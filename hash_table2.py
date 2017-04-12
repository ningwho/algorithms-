class MyHashTable:
    def __init__(self):
        self.buckets = [None] * 26

    def my_hash(self, value):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        first_letter = value[0]
        return alphabet.index(first_letter.lower())

    def insert(self, value):
        # Inserts value into the correct bucket.
        # get index of bucket
        bucket_index = self.my_hash(value)
        #initialize the bucket as an array, if the bucket is None
        #first time inserts only

        if self.buckets[bucket_index] == None:
            self.buckets[bucket_index] = []

        #actually append the value
        bucket = self.buckets[bucket_index]
        bucket.append(value)


    def exists(self, value):
        # Returns true if the value exists in the bucket.
        #getting the bucket
        bucket_index = self.my_hash(value)
        if self.buckets[bucket_index] == None:
            self.buckets[bucket_index] = []
        elif value in self.buckets[bucket_index]:
            return True
        else:
            return False

        #checking if entire bucket exists
        bucket_index = self.my_hash(value)
        bucket = self.buckets[bucket_index]
        if bucket == None:
            return False
        for v in bucket:
            if v == value:
                return true
        return False


hash_table = MyHashTable()
hash_table.insert('Hello World')
hash_table.insert('Bob')
hash_table.insert('Cathy')
hash_table.insert('Zebra')

print(hash_table.exists('Hello World'))

print(hash_table.buckets)
