#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.

"""
__author__ = 'Timothy K Reynoso with help from Mike and Tiree and Kyle'

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    # your code here
    bits = bits.strip('0')
    timing = min([len(element) for element in bits.split('1') + bits.split('0') if element])
    bits_new = bits.replace('0000000' * timing, '   ').replace('111' * timing, '-').replace('1' * timing, '.').replace('000' * timing, ' ').replace('0' * timing, '')
    return bits_new


def decode_morse(morse):
    # your code here
    morse = morse.strip()
    letters = ''
    raw_words = morse.split("   ")
    for word in raw_words:
        chars = word.split(' ')
        for each_word_char in chars:
            letters += MORSE_2_ASCII[each_word_char]
        letters += ' '
    return letters.strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
