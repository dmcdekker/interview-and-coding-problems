'''Counting words'''

from operator import itemgetter

input_file = open('./test.txt')

word_dict = {}

for line in input_file:
    # strip white space
    line = line.rstrip()
    #split on space
    words = line.split()

    for word in words:
        # strip punctuation
        word = word.strip("'\",.!?-#$%^&();:_")
        #lowercase
        word = word.lower()
        # add words to dict
        word_dict[word] = word_dict.get(word, 0) + 1


print('_____sorted by key (word) ascending_____')
for word, count in sorted(word_dict.items()):
    print(word, count)

print('')
print('_____sorted by key (word) descending_____')
for word, count in sorted(word_dict.items(), reverse=True):
    print(word, count)

print('')
print('_____sorted by value (count) ascending_____')
for word, count in sorted(word_dict.items(), key=itemgetter(1)):
    print(count, word)

print('')
print('_____sorted by value (count) descending_____')
for word, count in sorted(word_dict.items(), key=itemgetter(1), reverse=True):
    print(count, word)

print('')
print('_____get last key value pair in sorted dict_____')
sorted_word_dict = sorted(word_dict.items())[-1]
print(sorted_word_dict)

print('')
print('_____get largest value in dict_____')
sorted_word_dict = sorted(word_dict.items(), key=itemgetter(1))[-1][1]
print(sorted_word_dict)

print('')
print('_____get largest key in dict_____')
sorted_word_dict = sorted(word_dict.items())[-1][0]
print(sorted_word_dict)


