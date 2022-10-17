# Wordle
A simple Wordle word finder in Python.

# Usage

`wordle.py [-h] [-c CONTAINING_LETTERS] [-x EXCLUDING_LETTERS] [-m MASK] [-s SIZE] dict_file`

## Description
Find words in the provided dictionary file that matches your filters. Very useful to find words in the Wordle game.

## Arguments
|argument|description|
|-|-|
|`dict_file`|the name of a plain-text dictionary file, one word per line (ie: 'dict_en-us.txt')|
|`-h, --help`|show a help message and exit|
|`-c CONTAINING_LETTERS, --containing_letters CONTAINING_LETTERS`|filter words that contain all the letters in the provided string (ie: 'abe' will match 'cable', 'bears', 'zebra', etc)
|`-x EXCLUDING_LETTERS, --excluding_letters EXCLUDING_LETTERS`|filter words that DO NOT contain any letters in the provided string (ie: 'abe' will NOT match 'cable', 'bears', 'zebra', etc)
|`-m MASK, --mask MASK`|filter words by the provide mask (ie: 'ze@@@' will match 'zebra', 'zebus', etc)
|`-s SIZE, --size SIZE`|word size (if not provided the default will be 5, Wordle's default)

# Setup
Make wordle.py executable:

```sh
$ chmod +x wordle.py
```

# Examples
## Example 1 (containing letters and excluding letters filter)
Let's say we want to find all 5-letter words in english that must have the letters `a`, `b`, `c`, and `e` in English:
```bash
$ wordle ./wordle.py -c abce dict_en-us.txt
Active filters:
  -> Accept only words that contain the letter(s): ['a', 'b', 'c', 'e']

Found word(s): ['beach', 'brace', 'cable']

Total found word(s): 3

```
Now we want the same thing, but excluding the words with the letters `r` and/or `l`:
```bash
$ wordle ./wordle.py -c abce -x rl dict_en-us.txt
Active filters:
  -> Accept only words that contain the letter(s): ['a', 'b', 'c', 'e']
  -> Deny words with the letter(s): ['r', 'l']

Found word(s): ['beach']

Total found word(s): 1
```

## Example 2 (mask filter)
Let's say we want to find all 5-letter words in english that must have the letters `e`, `f` and `g`:
```bash
$ wordle ./wordle.py -c efg dict_en-us.txt
Active filters:
  -> Accept only words that contain the letter(s): ['e', 'f', 'g']

Found word(s): ['befog', 'feign', 'fogey', 'forge', 'fudge', 'fugue', 'gaffe', 'gofer', 'grief']

Total found word(s): 9
```
Now we want to grab only words that begin with `f` and ends with `e`. We can accomplish that using a mask: `f@@@e`. When using masks the `@` symbol means a single-char wildcard:
```bash
$  wordle ./wordle.py -c efg -m f@@@e dict_en-us.txt
Active filters:
  -> Accept only words that contain the letter(s): ['e', 'f', 'g']
  -> Mask: f@@@e

Found word(s): ['forge', 'fudge', 'fugue']

Total found word(s): 3

```


# License
MIT License.
Very, very permisive licensing.
