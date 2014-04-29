import argparse
import logging
import os
import sys
from gutenberg import ProjectGutenbergText
from ebooks import EbooksQuotes

parser = argparse.ArgumentParser(
    description="Generate pithy _ebooks quotes from PrivateWikiNotebook text.")
parser.add_argument(
    '--path', help="The path to a mounted Project Gutenberg CD or DVD.",
    default=None)
parser.add_argument(
    "keyword", nargs="*", help="Keywords to focus on when making selections.",
    default=["wiki"])

args = parser.parse_args()
ebooks = EbooksQuotes(args.keyword)
texts = [ProjectGutenbergText(open("data/PrivateWikiNotebook.txt").read())]
for text in texts:
    total = 0
    for para in text.paragraphs:
        for quote in ebooks.quotes_in(para):
            print quote.encode("utf8")
            total += 1
    logging.warn("%d quotes found in %s" % (total, text.name))
