class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substring_set = set()
        max_len = 0
        left = 0
        for right in range(len(s)):
            if s[right] in substring_set:
                # move left until we delete the already conflicting character
                while(s[right] in substring_set):
                    substring_set.remove(s[left])
                    left += 1
                substring_set.add(s[right])
            else:# we keep expanding unique sequence
                substring_set.add(s[right])
                max_len = max(max_len, len(substring_set))

            
        return max_len
                