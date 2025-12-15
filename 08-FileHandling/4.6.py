import re

file_name=input('Enter file name: ')

def read_file():
    with open(file_name,'r',encoding='utf-8') as file:
        return file.read()

def lines():
    content=read_file()
    content=content.splitlines()
    return len(content)

def words():
    content=read_file()
    content=content.split()
    return len(content)

def characters():
    content=read_file()
    return len(content)




try:
    print(f"In file <{file_name}> {lines()} lines")
    print(f"In file <{file_name}> {words()} words")
    print(f"In file <{file_name}> {characters()} characters")
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found!")

