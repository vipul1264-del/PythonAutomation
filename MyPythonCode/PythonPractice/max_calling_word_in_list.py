#max_calling_word in list

from collections import Counter

l = ['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john','johnny','jamie','johnny','john']

vote_count = Counter(l)
print(vote_count)
max_vote = max(vote_count)
print(f"{max_vote}{"::"}{max(vote_count.values())}")