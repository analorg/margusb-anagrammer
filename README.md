# Anagrammer

Multi-word anagram solver

## Installing Prerequisites

### linux (Ubuntu 14.04)

You need to have:
 - python3 
 ``` 
 $ sudo apt install python3
 ```
 - git 
 ```
 $ sudo apt install git
 ```
 - wget 
 ```
 $ sudo apt install wget
 ```
 <br>
 
Check Python version:
```
$ python3 --version
```
Check Git version:
```
$ git --version
```
Check Wget version:
```
$ wget --version
```
<br>

## Download latest Anagrammer build
```
$ git clone https://github.com/margusb/anagrammer.git
```
<br>

## Make script executable
```
$ cd anagrammer/
$ chmod a+x anagrammer.py
```
<br>

## Download Datasets
```
$ wget -P data https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt 
```
<br>

## Usage by shell
```
anagrammer.py {path} {word}
$ python3 anagrammer.py data/google-10000-english.txt add
or
$ ./anagrammer.py data/google-10000-english.txt add
```

The above example would output:
```
duration,list,of,anagrams,found
10279,add,dad
```
<br>

## Usage by import

1. Import reference to anagrammer
```
import anagrammer as an
```
2. Set main variables
```
filepath = 'data/google-10000-english.txt'
word = 'test'
```
3. Find anagrams

  - Cached anagrams:    
```
anagram_words = an.anagrammer(filepath, word)
print('Anagrams for', word ,'is:', ', '.join(anagram_words))
```
  - Not cached anagrams:    
```
contents = an.read_dictionary_file(filepath)
dict_encoded_anagram = an.encode_anagrams(contents)
anagram_words = an.find_anacrams(word, dict_encoded_anagram)
print('Anagrams for', word ,'is:', ', '.join(anagram_words))
```
  - Not cached inversed dictionary anagrams:    
```
contents = an.read_dictionary_file(filepath)
dict_encoded_anagram = an.encode_anagrams_inverted(contents)
anagram_words = an.find_anacrams_inverted(word, dict_encoded_anagram)
print('Anagrams for', word ,'is:', ', '.join(anagram_words))
```

