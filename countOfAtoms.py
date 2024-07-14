from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                for atom, count in top.items():
                    stack[-1][atom] += count * multiplicity
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                atom = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                stack[-1][atom] += multiplicity
        
        result = ""
        for atom in sorted(stack[-1]):
            result += atom
            count = stack[-1][atom]
            if count > 1:
                result += str(count)
        
        return result

# Test case
sol = Solution()
print(sol.countOfAtoms("H2O"))  # Output: "H2O"
print(sol.countOfAtoms("Mg(OH)2"))  # Output: "H2MgO2"
print(sol.countOfAtoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"
