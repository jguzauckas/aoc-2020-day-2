# Advent of Code 2020 Day 2 Practice

Today you will be working on Advent of Code 2020 Day 2. (both parts!) I have provided you with a similar set-up to your Advent of Code project to simplify the process. The file `input-transform.py` when run, will convert the pasted information from Advent of Code in `input.txt` into an easy to use format in `input.json`. You should make a solution file that reads in the input from `input.json` and solves both parts 1 and 2. Your final solution should print a sentence for each part with the relevant information.

---

## The format of the `input.json` file:

This is a list of lists. That means that there is a large list that holds all of the password information. Inside, there are smaller lists for each password that always contains 4 elements: the starting index (int), the ending index (int), the character to search for (str), and the password itself (str).

When you use a loop to go through the larger list, each element given to you is a list where the first index holds the starting number, the second index holds the ending number, etc.
