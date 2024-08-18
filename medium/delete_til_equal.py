class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        
        
        """
        steps = 0
        
        while (word1 != word2):
            if (len(word1)<len(word2)):
                word1, word2 = word2, word1
            
            inc=1
            

            # Deal when they r equal (searching for longest substr)
            # Count number of chars until a different one is found, if this count is less than len(word)-count
            xeq=2
            while(word1[:xeq] == word2[:xeq]):
                xeq+=1
            
            if xeq > len(word1)//2:
                inc=len(word1)-xeq-1
                word1=word1[:xeq]
            else:
                inc=xeq-1
                word1=word1[xeq-1:]
                    
            steps+=inc

        return steps

s = Solution()
print(s.minDistance("mart","karma"))