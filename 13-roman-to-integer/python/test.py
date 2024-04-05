# I V X  L  C   D   M
# 1 5 10 50 100 500 1000
# IV IX XL XC CD  CM
# 4  9  40 90 400 900

class Solution:
    def romanToInt(self, s: str) -> int:

        num = 0
        r1 = [{'M': 1000}, {'D': 500}, {'C': 100}, {'L': 50}, {'X': 10}, {'V': 5}, {'I': 1}]
        r2 = [{'CM': 900}, {'CD': 400}, {'XC': 90}, {'XL': 40}, {'IX': 9}, {'IV': 4}]

        for i in range(6):
            if [*r2[i]][0] in s:
                num += r2[i][[*r2[i]][0]]
                s = s.split([*r2[i]][0])[0] + s.split([*r2[i]][0])[1]
            a = list(s).count([*r1[i]][0])
            num += r1[i][[*r1[i]][0]] * a

        a = list(s).count([*r1[6]][0])
        num += r1[6][[*r1[6]][0]] * a

        return num
