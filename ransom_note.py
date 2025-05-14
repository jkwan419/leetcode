class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = {}
        for c in magazine:
            magazine_letters[c] = magazine_letters.get(c, 0) + 1

        for c in ransomNote:
            if not c in magazine_letters or magazine_letters[c] == 0:
                return False
            magazine_letters[c] -= 1
        return True
