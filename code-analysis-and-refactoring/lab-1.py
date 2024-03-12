from itertools import permutations


# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
def permutations_without_duplicates(s):
    unique_permutations = {''.join(p) for p in permutations(s)}
    result = list(unique_permutations)
    return result

print(permutations_without_duplicates('a'))    
print(permutations_without_duplicates('ab'))  
print(permutations_without_duplicates('abc')) 
print(permutations_without_duplicates('aabb'))

