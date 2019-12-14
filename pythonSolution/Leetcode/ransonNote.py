class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rasonNoteSet =  ''.join(ransomNote.split(" "))
        magazineSet = ''.join(magazine.split(" "))
        return all(item in magazineSet for item in ransomNote)

