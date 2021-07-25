class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        invalid_close = 0
        balance = 0
        for char in s:
            if char == '(':
                balance+=1
            elif char == ')' and balance == 0:
                invalid_close += 1
            elif char == ')':
                balance -= 1
        invalid_open = balance
        output = set()
        n = len(s)
        def backtrack(i, rem_open, rem_close, balance, formed):
            if i == n:
                if balance == 0:
                    output.add(formed)
                return 
            if s[i] != '(' and s[i] != ')':
                backtrack(i+1, rem_open, rem_close, balance, formed+s[i])
            if s[i] == '(':
                backtrack(i+1, rem_open, rem_close, balance+1, formed+s[i])
            elif s[i] ==')' and balance > 0:
                backtrack(i+1, rem_open, rem_close, balance-1, formed+s[i])
            if s[i] == '(' and rem_open > 0:
                backtrack(i+1, rem_open-1, rem_close, balance, formed)
            if s[i] == ')' and rem_close > 0:
                backtrack(i+1, rem_open, rem_close-1, balance, formed)
        backtrack(0, invalid_open, invalid_close, 0, '')
        return output
                
                
                
            
        
