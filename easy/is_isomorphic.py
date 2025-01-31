class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Construct a translation map char by char
        # If cur_char is not in the map add it
        # If it is it must be the mapped letter
        replacement_map = {}
        used = set() # account for the created mappings and avoid repetitions

        for i,c in enumerate(s):
            if c not in replacement_map:
                if t[i] not in used:
                    replacement_map[c] = t[i]
                    used.add(t[i])
                else:
                    return False
            else:
                if replacement_map[c] != t[i]:
                    return False
        
        return Trueclass Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Construct a translation map char by char
        # If cur_char is not in the map add it
        # If it is it must be the mapped letter
        replacement_map = {}
        used = set() # account for the created mappings and avoid repetitions

        for i,c in enumerate(s):
            if c not in replacement_map:
                if t[i] not in used:
                    replacement_map[c] = t[i]
                    used.add(t[i])
                else:
                    return False
            else:
                if replacement_map[c] != t[i]:
                    return False
        
        return True