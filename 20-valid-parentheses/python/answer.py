class Solution:
    def isValid(self, s: str) -> bool:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
        if '(]' in s or '(}' in s or '[)' in s or '[}' in s or '{)' in s or '{]' in s:
            return False
        s = list(s)
        a = 0
        b = 0
        c = 0
        for item in s:
            if item == '(':
                a += 1
            elif item == ')':
                a -= 1
            elif item == '{':
                b += 1
            elif item == '}':
                b -= 1
            elif item == '[':
                c += 1
            elif item == ']':
                c -= 1
            if a < 0 or b < 0 or c < 0:
                return False
        if a == 0 and b == 0 and c == 0:
            return True
        else:
            return False

        # if '(]' in s or '(}' in s or '[)' in s or '[}' in s or '{)' in s or '{]' in s:
        #     return False
        # mapping = {')': 0,'(': 0,'}': 0,'{': 0,']': 0,'[': 0}
        # mapping['('] = s.count('(')
        # mapping[')'] = s.count(')')
        # mapping['{'] = s.count('{')
        # mapping['}'] = s.count('}')
        # mapping['['] = s.count('[')
        # mapping[']'] = s.count(']')
        # if mapping['('] == mapping[')'] and mapping['{'] == mapping['}'] and mapping['['] == mapping[']']:
        #     return True
        # else:
        #     return False
