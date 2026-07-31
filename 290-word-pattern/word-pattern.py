class Solution(object):
    def wordPattern(self, pattern, s):
        word=s.split()
        if len(pattern)!=len(word):
            return False

        map1={}
        map2={}

        for i in range(len(pattern)):
            if pattern[i] in map1:
                if map1[pattern[i]]!=word[i]:
                    return False

            if word[i] in map2:
                if map2[word[i]]!=pattern[i]:
                    return False
            
            map1[pattern[i]]=word[i]
            map2[word[i]]=pattern[i]
        return True





        