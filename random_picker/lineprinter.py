#!/usr/bin/env python3
from time import sleep
import sys
import random


DELAY = 0.005  # s


def lprint(text):
    codes = [ord(c) for c in text if c != ' ']
    start = ord('A')
    last = max(codes)
    stop = min(last, 255) + 1
    chars = set(text)
    seen = {' '}
    for code in range(start, stop):
        current = chr(code)
        seen.add(current)
        for char in text:
            if char in seen:
                out = char
                chars.discard(char)
            else:
                out = current
            print(out, end='', flush=True)
            if not chars:
                break
            if out != ' ':
                sleep(DELAY)
        print('\r', end='', flush=True)
    print('\r' + text)


def demo():
    names = [
        'Alan Turing',
        'Grace Hopper',
        'Barbara Liskov',
        'Alan Kay',
        'Edsger Dijkstra',
        'John Backus',
    ]
    random.shuffle(names)
    for name in names:
        lprint(name)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        lprint(' '.join(sys.argv[1:]))
    else:
       demo()
