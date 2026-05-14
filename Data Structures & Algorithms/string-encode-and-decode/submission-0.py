class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for item in strs:
            encoded += str(len(item))+ '@' + item 
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            # move j until we find the separator
            while s[j] != "@":
                j += 1
            # length is everything before @
            length = int(s[i:j])
            # word starts after @
            word_start = j + 1
            word_end = word_start + length
            decoded.append(s[word_start:word_end])
            # move i to start of next encoded word
            i = word_end
        return decoded
