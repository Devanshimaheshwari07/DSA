class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote)>len(magazine):
            return False
        
        magazine_count={}

        for ch in magazine:
            magazine_count[ch]=magazine_count.get(ch,0)+1

        for i in ransomNote:
            if i not in magazine_count or magazine_count[i]==0:
                return False
            if i in magazine_count and magazine_count[i]>0:
                magazine_count[i]-=1
        return True