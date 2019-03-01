import anagrammer as an
import datetime

filepath = 'data/lemmad.txt'
#filepath = 'data/google-10000-english.txt'
word = 'test'

print('Multi-word anagram solver algorithms - running time in microseconds')

# cached anagrams    
start = datetime.datetime.now()
anagram_words = an.anagrammer(filepath, word)
stop = datetime.datetime.now()
delta = stop - start
print('1. Cached anagrams:', delta.microseconds)


# no cached anagrams    
start = datetime.datetime.now()
contents = an.read_dictionary_file(filepath)
dict_encoded_anagram = an.encode_anagrams(contents)
anagram_words = an.find_anacrams(word, dict_encoded_anagram)
stop = datetime.datetime.now()
delta = stop - start
print('2. No cached anagrams:', delta.microseconds)


# no cached inversed dictionary anagrams    
start = datetime.datetime.now()
contents = an.read_dictionary_file(filepath)
dict_encoded_anagram = an.encode_anagrams_inverted(contents)
anagram_words = an.find_anacrams_inverted(word, dict_encoded_anagram)
stop = datetime.datetime.now()
delta = stop - start
print('3. No cached inversed dictionary anagrams:', delta.microseconds)

print('Anagrams for', word ,'is:', ', '.join(anagram_words))

