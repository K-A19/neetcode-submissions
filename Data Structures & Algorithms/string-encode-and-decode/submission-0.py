class Solution:

    def encode(self, strs: List[str]) -> str:
        phrase = ""
        for string in strs:
            phrase = phrase + str(len(string)) + "|" + string
        
        return phrase

    def decode(self, s: str) -> List[str]:
        
        strs = []
        phrase = s
        while phrase != "" :
            number = phrase.find("|")
            length = int(phrase[:number])
            strs.append(phrase[number + 1: length + number + 1])
            phrase = phrase[number + length + 1 :]

        return strs

