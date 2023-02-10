"""
Author: Oscar Jose Rodriguez Alfaro
CSE 111 | Programming with Functions
File name: test_sentences.py

Purpose
Prove that you can write a Python program and write and run test functions to help you find and fix mistakes.
"""

from sentences import get_determiner, get_noun, get_verb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single noun.

    single_nouns = [
        "bird",
        "boy",
        "car",
        "cat",
        "child",
        "dog",
        "girl",
        "man",
        "rabbit",
        "woman",
    ]

    # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):
        # Call the get_noun function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = [
        "birds",
        "boys",
        "cars",
        "cats",
        "children",
        "dogs",
        "girls",
        "men",
        "rabbits",
        "women",
    ]

    # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):
        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns


def test_get_verb():
    # 1. Test the past tense verb.
    past_tense = [
        "drank",
        "ate",
        "grew",
        "laughed",
        "thought",
        "ran",
        "slept",
        "talked",
        "walked",
        "wrote",
    ]

    # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):
        # Call the get_verb function which
        # should return a plural determiner.
        tense = "past"
        quantity = 1
        word = get_verb(quantity, tense)

        # Verify that the word returned from get_verb
        # is one of the words in the past_tense list.
        assert word in past_tense

    # 2. Test the singular present tense.
    singular_present_tense = [
        "drinks",
        "eats",
        "grows",
        "laughs",
        "thinks",
        "runs",
        "sleeps",
        "talks",
        "walks",
        "writes",
    ]

    # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):
        # Call the get_verb function which
        # should return a singular present tense verb.
        tense = "present"
        quantity = 1
        word = get_verb(quantity, tense)

        # Verify that the word returned from get_verb
        # is one of the words in the singular_present_tense list.
        assert word in singular_present_tense

    # 3. Test the plural present tense.
    plural_present_tense = [
        "drink",
        "eat",
        "grow",
        "laugh",
        "think",
        "run",
        "sleep",
        "talk",
        "walk",
        "write",
    ]

    # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):
        # Call the get_verb function which
        # should return a plural present tense verb.
        tense = "present"
        quantity = 2
        word = get_verb(quantity, tense)

        # Verify that the word returned from get_verb
        # is one of the words in the plural_present_tense list.
        assert word in plural_present_tense

    # 4. Test the future tense.
    future_tense = [
        "will drink",
        "will eat",
        "will grow",
        "will laugh",
        "will think",
        "will run",
        "will sleep",
        "will talk",
        "will walk",
        "will write",
    ]

    # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):
        # Call the get_verb function which
        # should return a future tense verb.
        tense = "future"
        quantity = 1
        word = get_verb(quantity, tense)

        # Verify that the word returned from get_verb
        # is one of the words in the future_tense list.
        assert word in future_tense


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
