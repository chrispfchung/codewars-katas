import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = list(string.ascii_lowercase)
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        combo = dict(zip(alpha,codes))
        # all code above to create key code values

        # all code below ciphers the words and adds it to a final code list
        all_encrypted = []
        for word in words:
            encrypted_word = []
            for char in word:
                encrypted_word.append(combo[char])
                #code above ciphers each individual letter

                #once function finishes ciphering one word, combine them together
                if len(encrypted_word) == len(word):
                    encrypted_word = ''.join(encrypted_word)
                    all_encrypted.append(encrypted_word)

        #return number of unique transformations
        return len(set(all_encrypted))
