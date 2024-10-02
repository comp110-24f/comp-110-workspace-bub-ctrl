"""Practicing with lists"""

__author__ = "730695410"

# my_numbers: list[float] = []  # with a literal
# my_numbers: list[float] = list()  # with a constructor

# my_numbers.append(1.5)
# my_numbers.append(2.3)

# print(my_numbers)

# string analogy
# my_name: str = "" #literal
# my_name: str = str() #constructor
# my_numbers.append(1.5)

# grocery_list: list[str] = list()
# grocery_list.append("bananas")


# creating an already populated list
# game_points: list[int] = [102, 86, 94]

# subscription notation/indexing
# print(game_points[2])
# last_game: int = game_points[2]

# modifying by index
# game_points[1] = 72
# print(game_points)


# class_num: str = "110"
# class_num[0] = "2"
# type error, str object does not support item assignment
# this is because lists are mutable, strings are an immutable type

# length of a list
# print(len(game_points))

# remove an item fom a list
# game_points.pop(1)
# print(game_points)

# function writing practice
# function name: display
# return value: none
# print every element in input list
# call display on game_points


# def display(int_list: list[int]) -> None:
# """displays all elements of int_list"""
# index: int = 0
# while index < len(int_list):
# print(int_list[index])
# index += 1


# display(int_list=game_points)


# list1: list[float] = [2.1, 2.2, 2.3]
# list1.append(2.2)
# print(list1)
# print(list1[len(list1)]) = index error in repl


# a function that takes a list as an argument


# def display(vals: list[int]) -> None:
# idx: int = 0
# while idx < len(vals):
# print(vals[idx])
# idx += 1


# display([1, 2, 3])


x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0

print(y)
