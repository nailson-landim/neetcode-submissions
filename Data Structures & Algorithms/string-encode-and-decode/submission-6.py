class Solution:
    def encode(self, strs: List[str]) -> str:
        # Just add the word length and its terminator
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter to identify the length
            j = s.find('#', i)
            length = int(s[i:j])
            
            # Extract the exact substring based on the length
            word = s[j + 1 : j + 1 + length]
            decoded.append(word)
            
            # Move the pointer to the start of the next metadata block
            i = j + 1 + length
        return decoded

