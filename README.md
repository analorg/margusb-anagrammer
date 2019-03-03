# Anagrammer

Multi-word anagram solver

## Installing Prerequisites

### linux (Ubuntu 14.04)

You need to have:
 - python3 
 ``` 
 sudo apt install python3
 ```
 - git 
 ```
 sudo apt install git
 ```

Check Python version:
```
$ python3 --version
```
Check Git version:
```
git --version
```



Download latest Anagremmer build

```
$ git clone https://github.com/margusb/anagrammer.git
```

Make script executable
```
$ chmod a+x anagrammer.py
```

## Usage

```
anagrammer {path} {word}
$ python anagrammer /path/to/dictionary/file test
```

The above example would output:
```
duration,list,of,anagrams,found
86744,sett,test,tste
```
