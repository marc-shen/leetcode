class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return len(haystack.split(needle)[0])
'''
史上最快答题，看完题直接就get到了题目的意思，然后直接用python的split函数解决了问题
'''
