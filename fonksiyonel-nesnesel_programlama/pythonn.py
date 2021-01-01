#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 03:15:39 2020

@author: enesmercan
"""

# _______________________________________________________________

print("\n")
print("_" * 70)
print("\nnesnesel programlama")  # nesnesel programlama


class lineCounter():
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)


lc = lineCounter('deneme.txt')

print("\nlc.lines\n", lc.lines)
print("lc.count()\n", lc.count())

lc.read()
print("\nlc.read()")

print("\nlc.lines\n", lc.lines)
print("lc.count()\n", lc.count())

# _______________________________________________________________

print("\n")
print("_" * 70)
print("\nfonksiyonel programlama")  # fonksiyonel programlama


def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]


def count(lines):
    return len(lines)


example_lines = read('deneme.txt')
lines_count = count(example_lines)
print("number of words :\t", lines_count)