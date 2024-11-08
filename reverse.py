class class_reverse:
    
    def __init__(self,w):
        self.w =w 
        
    def reverse_word(self):
        return self.w[::-1]
    
word = input("Enter the word to be reversed: ")
rev_ob = class_reverse(word)

result = rev_ob.reverse_word()
print("Reversed String: ", result)