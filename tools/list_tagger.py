# OBJECTIVE: Decrease O notation for searching through a list of dictionary
# WHAT: This script tags each dict in the list by these condition \
#                   1. its kanji(hiragana for hiragana only words) which is in utf-8 will be turned to hex
#                   2. the list will be ordered
# WHY: Increase search speed
# HOW: Turn each words to its hex repr
# EFFECT: Can use binary search
# PROBLEM:
#       1. What if an element have the same word
#       2. How to get to the wanted index(utf-8 to hex will give a large value)