# import my_function as m
# m.Command('dir')

from my_function import Command,hello,hello1

Command('dir')

from os import system
system('dir')
system('cd')
hello()
hello1('alex')