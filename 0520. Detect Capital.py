class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        if word[0].isupper() and word[1].isupper():
            if not word[2:] or word[2:].isupper():
                return True
            else:
                return False
        elif (word[0].isupper() and word[1].islower()) or (word[0].islower() and word[1].islower()):
            if not word[2:] or word[2:].islower():
                return True
            else:
                return False
        else:
            return False