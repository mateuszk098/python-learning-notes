"""
See description at https://www.hackerrank.com/challenges/capitalize

You are asked to ensure that the first and last names of people begin with 
a capital letter in their passports. For example, alison heck should be 
capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.
"""

# Complete the solve function below.


def solve(s):
    return " ".join([word.capitalize() for word in s.split(" ")])


if __name__ == "__main__":
    s = input()
    print(solve(s))
