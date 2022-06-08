class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        maintain a list of lf_bigger
        """
        answer = []
        num_nextbig = {} 
        lf_bigger={}
        
	for n2 in nums2:        
            
            for lf in lf_bigger.keys():
                if n2 > lf:
                    num_nextbig[lf] = n2
                    lf_bigger.pop(lf)
                    
            lf_bigger[n2] = 1
                    
        
        for n1 in nums1:
            exists = num_nextbig[n1] if n1 in num_nextbig else -1
            answer.append(exists)
            
        return answer
