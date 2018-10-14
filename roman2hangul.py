# -*- coding: utf-8 -*-

import sys
import json

def main():
    text = sys.argv[1].upper()
    hangul = []

    with open('hangul_trie.json') as f:
        trie = json.load(f)

    node = trie

    print(text)

    for i in reversed(range(len(text))):
        roman = text[i]

        if roman == '-':
            hangul.append(node['$'])
            node = trie
            continue
        """
        if roman == ' ':
            hangul.append(node['$'])
            hangul.append(' ')
            node = trie
            continue
        """

        if not node.get(roman) and roman != '-':
            hangul.append(node['$'])
            hangul.append(roman)
            node = trie
            continue

        node = node[roman]

    if node.get(roman):
        hangul.append(node['$'])
    else:
        hangul.append(roman)

    hangul.reverse()

    print(''.join(hangul));

if __name__ == '__main__':
    main()
