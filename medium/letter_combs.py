class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle empty input
        if not digits:
            return []
            
        n_to_letter = [
            [], [],
            ["a","b","c"], #2
            ["d","e","f"],
            ["g","h","i"],
            ["j","k","l"],
            ["m","n","o"],
            ["p","q","r","s"],
            ["t","u","v"],
            ["w","x","y","z"] #9
        ]

        results = []
        
        def explore_combinations(ix, curr_string_lst):
            for letter in n_to_letter[int(digits[ix])]:
                curr_string_lst.append(letter)
                
                if ix == len(digits)-1:
                    results.append("".join(curr_string_lst))
                else:
                    explore_combinations(ix+1, curr_string_lst)
                    
                curr_string_lst.pop()  # backtrack by removing the letter

        explore_combinations(0, [])
        return results