#split string into characters
#check list: if letters in S are also in J, add to [same list]
#return len of [same list]


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        same = []
        for char in S:
            for charj in J:
                if char in charj:
                    same.append(char)
        return len(same)
