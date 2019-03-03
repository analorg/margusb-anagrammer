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
<br>

## Download latest Anagrammer build
```
$ git clone https://github.com/margusb/anagrammer.git
```
<br>
<br>

## Make script executable
```
$ cd anagrammer/
$ chmod a+x anagrammer.py
```
<br>
<br>

## Download Datasets
```
$ wget -P data https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt 
```
<br>
<br>

## Usage

```
anagrammer {path} {word}
$ python3 anagrammer.py data/google-10000-english.txt add
```

The above example would output:
```
duration,list,of,anagrams,found
10279,add,dad
```
