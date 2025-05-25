class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []
        for i, word in enumerate(words):
            if x in word:
                out.append(i)
        return out
        
