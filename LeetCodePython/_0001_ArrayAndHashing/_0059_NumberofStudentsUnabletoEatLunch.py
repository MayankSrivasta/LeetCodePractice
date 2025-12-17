from typing import List
from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        res = len(students)             # start with all students unable to eat
        cnt = Counter(students)         # count how many want 0 and 1

        for s in sandwiches:            # go through sandwiches in order
            if cnt[s] > 0:              # if there’s at least one student who wants this sandwich
                res -= 1                # one less student unable to eat
                cnt[s] -= 1             # reduce demand for this sandwich type
            else:                       # no student wants this sandwich
                break                   # stop the process
        
        return res
    
# my understanding-> since sandwiches is fixed but students are not fixed so counter of students is taken, & then the
# values of sandwiches is putted in counter of students, because we already know students will rotate so anyone would
# eat the sandwiches. But in-case if there are we have '0' sandwiches at the top, but the rest of the students wants
# only 1 sandwiches then nothing can be done & we return the result.