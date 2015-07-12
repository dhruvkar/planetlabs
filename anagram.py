from __future__ import print_function
from collections import defaultdict


# Open file and add >=4 letter words to a set while stripping newline chars and making lowercase
with open("words.txt") as f:
	words = {line.rstrip('\n').lower() for line in f if len(line.rstrip('\n')) >=4}
	# Created a unique, sorted ('aba' -> 'aab') words set
	sorted_words = {"".join(sorted(word)) for word in words}

d = defaultdict(list)

# Create a dict with the sorted word as key and all its anagrams as the values
[d["".join(sorted(word))].append(word) for word in words if "".join(sorted(word)) in sorted_words]
	

# Cleanly print out anagrams on each line based on problem criteria
[print(', '.join(v)) for k,v in d.iteritems() if len(k) <= len(v)]


