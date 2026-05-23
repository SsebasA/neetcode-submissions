class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_words = []
        for word in strs:
            length = len(word)
            encoded_word = f"{length}#{word}"
            encoded_words.append(encoded_word)
        
        return "".join(encoded_words)

    def decode(self, s: str) -> List[str]:
        decoded_words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            decoded_words.append(word)
            i = j + 1 + length
        
        return decoded_words
