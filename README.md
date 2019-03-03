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



Download latest Anagremmer build

```
$ git clone https://github.com/margusb/anagrammer.git
```

Make script executable
```
$ cd anagrammer/
$ chmod a+x anagrammer.py
```

## Download Datasets
```
$ wget -P data https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt 
```

## Usage

```
anagrammer {path} {word}
$ python3 anagrammer.py data/google-10000-english.txt test
```

The above example would output:
```
duration,list,of,anagrams,found
86744,sett,test,tste
```
