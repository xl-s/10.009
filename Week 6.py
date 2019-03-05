# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:21:49 2019

@author: Xu Liang

Week 6 Problem Set
"""

import re # For Exercise 2

class Coordinate: # For Cohort sessions 4
    pass

# Cohort Sessions 1
def reverse(string):
    return ''.join([char for char in reversed(string)])


# Cohort Sessions 2
def check_password(string):
    allowed = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digits = set('1234567890')
    return False if set(string) - (allowed | digits) or len(string) < 8 or \
        sum(char in digits for char in string) < 2 else True


# Cohort Sessions 3
def longest_common_prefix(str1, str2):
    prefix = []
    for char1, char2 in zip(str1, str2):
        if char1 == char2:
            prefix.append(char1)
        else:
            break
    return ''.join(prefix)


# Cohort Sessions 4
def get_maxmin_mag(file):
    coords = []
    mag = []
    for line in list(file):
        coords.append([float(num) for num in line.replace('\n', '').split('\t')])
    for coord in coords:
        mag.append((coord[0]**2 + coord[1]**2)**0.5)
    kmax = max(range(len(mag)), key=mag.__getitem__)
    kmin = min(range(len(mag)), key=mag.__getitem__)
    cmax = Coordinate()
    cmin = Coordinate()
    cmax.x, cmax.y = coords[kmax][0], coords[kmax][1]
    cmin.x, cmin.y = coords[kmin][0], coords[kmin][1]
    return cmax, cmin


# Homework 1
def binary_to_decimal(binary):
    return sum((int(char)) * 2**(int(indx)) for indx, char in enumerate(reversed(binary)))


# Homework 2
def uncompressed(string):
    chars = []
    for indx, char in enumerate(string):
        if indx % 2:
            chars.append(char * int(string[indx - 1]))
    return ''.join(chars)
            

# Homework 3
def get_base_counts2(string):
    base = {'A':0, 'C':0, 'G':0, 'T':0}
    allowed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in string:
        if char not in allowed:
            return 'The input DNA string is invalid'
        if char in base.keys():
            base[char] += 1
    return base


# Homework 4
def get_fundamental_constants(file):
    constants = {}
    for line in file:
        try:
            constants[line.split()[0]] = float(line.split()[1])
        except:
            continue
    return constants
        
        
# Homework 5
def process_scores(file):
    scores = [line for line in file][0].split()
    total = sum([float(score) for score in scores])
    return total, total/len(scores)
    

# Exercise 1
def find_anagrams(file):
    words = [line.split()[0] for line in file]
    occurences = {}
    anagrams = []
    # Break down all the words
    for word in words:
        occurences[word] = {}
        for char in word:
            if char in occurences[word].keys():
                occurences[word][char] += 1
            else:
                occurences[word][char] = 1
    # Compute all the anagrams
    for word in words:
        words.remove(word)
        anlist = [word]
        for other in words:
            if occurences[word] == occurences[other]:
                anlist.append(other)
                words.remove(other)
        if len(anlist)>1:
            anagrams.append(anlist)
    # Find the most common anagrams
    maxlist = []
    maximum = 2
    for anagram in anagrams:
        if len(anagram) > maximum:
            maximum = len(anagram)
            maxlist = [anagram]
            continue
        if len(anagram) == maximum:
            maxlist.append(anagram)
    return maxlist
    
    
# Exercise 2
def split_sentences(file):
    out = re.split('(?<!(Mr.|Dr.))(?<!(Mrs.))(?<=[\.?!]) (?=[A-Z])', file.readline().strip())
    return [elm for elm in out if elm]

