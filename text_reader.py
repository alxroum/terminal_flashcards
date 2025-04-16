import sys
import os
import program


def read_from_txt(filename):

    lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())

    except FileNotFoundError:
        print("File Not Found!")

    terms = []
    defs = []
    print("p1")
    for line in lines:
        temp = line.split('\u2013')
        print(temp)
        t1temp = temp[0].rstrip()
        t1temp = t1temp.strip("0123456789.\t")
        terms.append(t1temp)
        if(len(temp) > 1):
            defs.append(temp[1].strip())
            

    data = dict(zip(terms, defs))
    print(data)
    return data

def main():

    lines = read_from_txt("input.txt")

    program.save_json("exam_4_terms.json", lines)

main()