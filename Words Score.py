def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    e_score = 0
    o_score = 0
    total = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            e_score += 2
        else:
            o_score += 1
        total = e_score + o_score
    return total


n = int(input())
words = input().split()
print(score_words(words))

# sl = []
# vl = ['a', 'e', 'i', 'o', 'u', 'y']
# num_vowels = 0
# words = input().split()
#
# for w in words:
#     sl.append(w)
#
# print(sl)
#
# count = 0
# for i in sl:
#     print(i)



