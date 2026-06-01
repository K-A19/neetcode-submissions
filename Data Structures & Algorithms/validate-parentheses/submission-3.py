class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(', ']' : '[', '}' : '{'}
        sequence = []

        if len(s) % 2 == 1:
            return False

        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                sequence.append(bracket)
            elif not sequence or brackets[bracket] != sequence[-1] :
                return False;
            else:
                sequence.pop()

        if sequence:
            return False
        else:
            return True



        
        