import sqlite3
from tracemalloc import start

def addPadding(ngram, line):
    startarr = []
    endarr = ["<END>"]
    if ngram <= 1: return line
    for i in range(ngram) - 1: startarr.append("<START>")
    return (startarr.extend(line)).extend(endarr)




def run():
    return

if __name__ == "main":
    run()