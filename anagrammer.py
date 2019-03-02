#!/usr/bin/env python

import datetime
import sys
import pickle
import os
from collections import defaultdict



def read_dictionary_file(filepath):
    try:
        with open(filepath,'rb') as f:
            contents = f.read()
        contents = contents.decode('utf-8', errors = 'ignore')    
        contents = contents.replace(' ', '|').splitlines()
    except:
        contents = []
    return contents


def encode_anagrams(word_list):
    enc = dict((w,''.join(sorted(w.lower().replace('|','')))) for w in word_list)
    return enc


def encode_anagrams_inverted(word_list):
    enc_rev = defaultdict(list)
    
    enc = dict((w,''.join(sorted(w.lower().replace('|','')))) for w in word_list)
 
    for k, v in enc.items():
        enc_rev[v].append(k) 
    return enc_rev


def get_cache_filename(filename):
    return os.path.splitext(os.path.basename(filename))[0]


def get_cache_loc(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache', filename+'.pkl') 


def encode_anagrams_cache(word_list, cache_file, recache = False):
    cache = os.path.isfile(cache_file)   

    if not cache or recache:
        enc = encode_anagrams(word_list)
        try:
            with open(cache_file,'wb') as f:
                pickle.dump(enc, f)
            return enc
        except:
            print('Error creating cache file:', cache_file)

    try:
        with open(cache_file,'rb') as f:
            enc = pickle.load(f)
    except:    
           enc = encode_anagrams(word_list)
    return enc


def find_anacrams(word, encoded_dict):
    try:
        word_encoded = ''.join(sorted(word.lower().replace(' ','')))
        anagrams = [k.replace('|',' ') for k, v in encoded_dict.items() if v == word_encoded]
        return anagrams
    except KeyError:
        return []

def find_anacrams_inverted(word, encoded_dict):
    try:
        word_encoded = ''.join(sorted(word.lower().replace(' ','')))
        return encoded_dict[word_encoded]
    except KeyError:
        return []


def anagrammer(filepath, word):
    contents = read_dictionary_file(filepath)
    
    cache_filename = get_cache_filename(filepath)
    cache_file = get_cache_loc(cache_filename)
    dict_encoded_anagram = encode_anagrams_cache(contents, cache_file, recache = False)
    anagrams = find_anacrams(word, dict_encoded_anagram)
     
    if word in anagrams:
        anagrams.remove(word)
    return anagrams
    

def main(argv=None):
    res = ''
    start = datetime.datetime.now()
    
    if len(argv) >= 2:
        filepath = argv[0] or ''
        word = argv[1] or '' 
    
    anagrams = anagrammer(filepath, word)

    stop = datetime.datetime.now()
    delta = stop - start
 
    if len(anagrams)>0:
        res = str(delta.microseconds) + ',' + ','.join(anagrams)
 
    print(res)

if __name__ == "__main__": 
    main(sys.argv[1:])
