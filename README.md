> [!CAUTION]
> This repository is for viewing only. Do not work on the assignment using this repository -- the actual course assignments will be provided to you via Pawtograder.

# Homework 8

## Overview

In this assignment, students will interactively download and parse webpages from Wikipedia.org.

Students will get practice with:
- Comparable
- Equality and hashing
- Recursion on Trees (DFS)
- Scraping websites

## Part 1: Download and parse a single webpage using `requests` and `BeautifulSoup`

You may need to `pip3 install requests types-requests beautifulsoup4 types-beautifulsoup4` to install both, along with their type stubs. Because we are limited in the packages we can install on the Pawtograder servers, you must use these two libraries to download the webpage. You may use Claude or a similar LLM to learn about the syntax needed to do this.

This page about the Wikimedia Foundation's User Agent policy may help: https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy

Once you have found how to download a webpage in a few lines of code, encapsulate it in a class called `WikipediaPage` (in `wikipedia_page.py`). The constructor should take a keyword as the argument, and if there exists a Wikipedia page with that title, it should request and save as attributes:
1. The keyword
2. The text of the webpage
3. A list of all unique Wikipedia links found on the webpage, sorted alphabetically

For example, if the keyword is `"effervescence"`, it should:
1. Check and make sure there is a webpage at `https://en.wikipedia.org/wiki/Effervescence`. (Note the case insensitivity.) If there is not, raise an appropriate error.
3. Store the keyword `"effervescence"` as an appropritately named attribute.
4. Store the text of the webpage as an appropritately named attribute.
5. From the list of all links on the webpage, store the ones for Wikipedia pages as an appropriately named attribute (as a sorted list of unique words).

Overwrite the `__eq__()` and `__hash__()` methods so that two `WikipediaPage`s are equal if they have the same keyword (title in the URL).

Overwrite the `__repr__()` method to return the keyword (title in the URL).

## Part 2: Make `WikipediaPage` `Comparable`

Choose a word, such as "effervescence". Make a class attribute that stores this word as a `target_word`.

Overwrite the `__str__()` method to return an appropriate message containing the keyword and the number of times the `target_word` appears in the text of the webpage.

When two `WikipediaPage`s are compared, the one with more instances of the `target_word` is considered "bigger".

## Part 3: Add the ability to interactively traverse the Wikipedia webpage graph

We will now treat the `WikipediaPage` class as a node in a graph (or tree). It has a list of options for what
its children could be (the Wikipedia links available on the page). Those link options are not yet children, because they are
of type `str` and not `WikipediaPage`. Add another attribute to `WikipediaPage` called `children` which starts
as an empty list of `WikipediaPage`. We will add pages to it as we interactively surf Wikipedia.org.

In `main.py`, implement the `WikipediaSurfer` constructor and methods as described in the comments.
You will need to add documentation. You may remove the "TODO" comments after implementing them.

It may be useful to `pip3 install sortedcontainers sortedcontainers-stubs`.

As usual, you should test all funtions that you write. There is an example test in `test_wikipedia_surfer.py` that
shows how to write tests for a function that requires user input.

You are not required to test printed output.

## Part 4: Try it out

In `main.py`, create an instance of `WikipediaSurfer` and interact with your application. Try to find a webpage
with a high number of instances of the target word. After quitting, copy the list of keywords outputted into 
the appropriate question in `Summary.md`.

Common confusion: The `keyword` is the title of each individual page. The `target_word` is the overall word
which we are counting in each page.

Also answer the other questions in `Summary.md`.
