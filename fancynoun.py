from random import randint
from string import strip
import linecache

"""
Recursive Transition Network (RTN) for constructing "fancy nouns"
Modification of the RTN on page 132 of the Twentieth-anniversary Edition of
"Godel, Escher, Bach" by Douglas R. Hofstadter
Features an unbounded adverb loop before a given verb: the ORNATE_VERB structure

                                              -> ORNATE_VERB -> FANCY_NOUN -> end
                          -> RELATIVE_PRONOUN -> FANCY_NOUN -> ORNATE_VERB -> end
FANCY_NOUN -> ORNATE_NOUN -> end
                          -> PREPOSITION -> FANCY_NOUN -> end

            -> NOUN -> end
ORNATE_NOUN -> ADJECTIVE (unbounded loop) -> NOUN -> end
            -> ARTICLE -> ADJECTIVE (unbounded loop) -> NOUN -> end
                       -> NOUN -> end

ORNATE_VERB -> VERB -> end
            -> ADVERB (unbounded loop) -> VERB -> end

"""



def article():
    return "the"

def adjective():
    return strip(linecache.getline("adjective.txt", randint(1,1133)))

def adjective_loop():
    adj = adjective()
    choice = randint(1,2)
    while choice == 1:
        adj += " " + adjective()
        choice = randint(1,2)
    return adj

def noun():
    return strip(linecache.getline("noun.txt", randint(1,982)))

def relative_pronoun():
    return strip(linecache.getline("pronoun.txt", randint(1,76)))

def preposition():
    return strip(linecache.getline("preposition.txt", randint(1,59)))

def adverb():
    return strip(linecache.getline("adverb.txt", randint(1,331)))

def adverb_loop():
    adv = adverb()
    choice = randint(1,2)
    while choice == 1:
        adv += " " + adverb()
        choice = randint(1,2)
    return adv


def verb():
    return strip(linecache.getline("verb.txt", randint(1,161)))

def ornate_verb():
    choice = randint(1,2)
    if choice == 1:
        ver = adverb_loop() + " " + verb()
    elif choice == 2:
        ver = verb()
    return ver


def ornate_noun():
    choice = randint(1,3)

    if choice == 1:
        return noun()
    elif choice == 2:
        return adjective_loop() + " " + noun()
    elif choice == 3:
        ornate = article()
        choice = randint(1,2)
        if choice == 1:
            ornate += " " + adjective_loop() + " " + noun()
        elif choice == 2:
            ornate += " " + noun()
        return ornate


def fancy_noun():
    fancy = ornate_noun() 
    choice = randint(1,3)

    if choice == 1:
        fancy += " " + relative_pronoun()
        choice = randint(1,2)
        if choice == 1:
            fancy += " " + ornate_verb() + " " + fancy_noun()
        elif choice == 2:
            fancy += " " + fancy_noun() + " " + ornate_verb()
    elif choice == 2:
        return fancy
    elif choice == 3:
        fancy += " " + preposition() + " " + fancy_noun()
    return fancy



print fancy_noun()

    
