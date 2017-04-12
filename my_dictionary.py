class MyDictionary:
    def __init__(self):
        self.keys = []
        self.values = []

    def insert_element(self, key, value):
        #Insert the element into the dictionary.
        self.keys.append(key)
        self.values.append(value)

    def find_element(self, key):
        # finds the element associated with the keyself.
        # returns none if key doesn't exist
        for x in range (len(self.key)):
            if self.key[i] == key:
                return self.values[i]
                break
            # look through all our keys. once found the key will stop looking after loop

            return None

    def remove_element(self, key):
        # finds element associated with key
        # removes element if element is found
        for x in range(len(self.keys)):
            if self.keys[i] == key:
                del self.values[i]
                del self.keys[i]



    def get_keys(self):
        # returns all keys
        return self.keys
    def elements(self):
        #returns all elements
        return self.values
    def isEmpty(self):
        #returns if the element list is empty
        if self.size() == 0:
            return True
        else:
            return False

    def size(self):
        #returns the size of the elements list
        return len(self.values)

dictionary = MyDictionary()
dictionary.insert_element('email','hamburger@gmail.com')
dictionary.insert_element('password','spaghetti')
dictionary.insert_element('phone','770-555-5555')


# child_dictionary = MyDictionary()
# child_dictionary.insert_element('another_value', 'test')
# dictionary.insert_element('child', dictionary)
# if dictionary.find_element('email') == 'tamby@hirewire.com':
#     print('yay')

for key in dictionary.get_keys():
    print(key + "\t\t" + dictionary.find_element(key))

# dictionary.remove_element('phone')

print("=======\n\n")
for key in dictionary.get_keys():
    print(key + "\t\t" + dictionary.find_element(key))
