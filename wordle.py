#!/usr/bin/env python3
import argparse
import os


def file_to_list(file:str) -> list[str]:
    if os.path.exists(file):
        f = open(file, 'r', encoding="utf-8")
        return (f.read()).split()
    else:
        print(f"File '{file}' was not found.")
        exit()


def word_filter(word: str,
                containing_letters: str = '',
                excluding_letters: str = '',
                precise_position_letters: str = '',
                word_size: str = 5) -> bool:

    # word size check
    if len(word) != word_size:
        return False

    # containing letters check
    for letter in containing_letters:
        if letter not in word:
            return False

    # deny letters check
    for letter in excluding_letters:
        if letter in word:
            return False

    # mask check
    if precise_position_letters:
        if len(precise_position_letters) == len(word):
            for i in range(len(precise_position_letters)):
                if (precise_position_letters[i] != "@" and
                    precise_position_letters[i] != word[i]):
                    return False
        else:
            return False
    return True


def wordle(dict_file: str,
           containing_letters: str = '',
           excluding_letters: str = '',
           mask: str = '',
           word_size: str = 5) -> None:

    # Load provided file
    word_list = file_to_list(dict_file)

    # Show command line parameters
    if containing_letters or excluding_letters or mask:
        print("Active filters:")
    if containing_letters:
        print("  -> Accept only words that contain the letter(s): " +
             f"{list(containing_letters)}")
    if excluding_letters:
        print(f"  -> Deny words with the letter(s): {list(excluding_letters)}")
    if mask:
        print(f"  -> Mask: {mask}")

    word_count = 0
    found_words = []
    for word in word_list:
        if word_filter(word, containing_letters, excluding_letters, mask, word_size):
            found_words.append(word)
    if found_words:
        print()
        print(f"Found word(s): {found_words}")
    print()
    print(f"Total found word(s): {len(found_words)}")


def get_args():
    parser = argparse.ArgumentParser(
    description='Find words in the provided dictionary file that matches ' +
                'your filters. Very useful to find words in the Wordle game.'
    )
    parser.add_argument(
        'dict_file',
        type=str,
        help="the name of a plain-text dictionary file, one word per line " +
             "(ie: 'dict_en-us.txt')"
    )
    parser.add_argument(
        '-c',
        '--containing_letters',
        type=str,
        help="filter words that contain all the letters in the provided " +
             "string (ie: 'abe' will match 'cable', 'bears', 'zebra', etc)",
        default=''
    )
    parser.add_argument(
        '-x',
        '--excluding_letters',
        type=str,
        help="filter words that DO NOT contain any letters in the provided " +
             "string (ie: 'abe' will NOT match 'cable', 'bears', 'zebra', etc)",
        default=''
    )
    parser.add_argument(
        '-m',
        '--mask',
        type=str,
        help="filter words by the provide mask (ie: 'ze@@@' will match " +
             "'zebra', 'zebus', etc)",
        default=''
    )
    parser.add_argument(
      '-s',
      '--size',
      type=int,
      help="word size (if not provided the default will be 5, " +
           "Wordle's default)",
      default=5
    )

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    wordle(
        args.dict_file,
        args.containing_letters,
        args.excluding_letters,
        args.mask,
        args.size
    )
