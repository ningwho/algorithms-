class MyHashTable:
    def __init__(self):
        #Nothing
        self.stuff = [None] * 26

    def my_hash(self, value):
        #Assume value is a string
        #Return hashed value

        my_first_letter = self.value[0]
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        return alphabet.index(my_first_letter)
    def hash_one(self, value):

        return self.value[:3]

    def hash_two(self, value):
        # alphabet = "abcdefghijklmnopqrstuvwxyz"
        #
        # words = value.split()
        # first_letters = []
        #
        # for word in words:
        #     first_letter = word[0]
        #     first_letters.append(first_letter.lower())
        # alphabet_indices = []
        #
        # for letter in first_letters:
        #     alphabet_indices.append(alphabet.index(letter))
        #
        #     product = alphabet_indices[0]
        # for i in range(1, len(alphabet_indices))
        #     product *= alphabet_indices[i]
        # return product


        words = value.split()
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_indices =[]
        product = 1
        for word in words:
            first_letter = word[0]
            index = alphabet.index(first_letter.lower())
            product *= index

        return product


thisObject = MyHashTable()
thisObject.hash_two = letters_in_name('tamby')

# "bob ann jon"
# ["bob", "ann", "jon"] 1.<=split by string with space " "
# ["b", "a", "c"] 2. loop through through words, store first letter in array
# ['1', '0', '2'] 3. get index of letter in alphabet
# []4. loop through and multiply
#
#
# product = array[0]
# for(init = 1; i < len(array); i++):
#     product *= array[i]








# example: phonebook. looking up cynthia first you have to go first letter which starts with C. hash stores everything like c. for hashes which tab do you go to. so you take the first letter and search for it.
