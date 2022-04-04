import sqlite3
import os

def addPadding(ngram, line):
    startarr = []
    endarr = ["<END>"]
    if ngram <= 1: return line
    for i in range(ngram) - 1: startarr.append("<START>")
    return (startarr.extend(line)).extend(endarr)

def createNGrams(length, paddedline):
    ngrams = []
    for i in range(len(paddedline) - (length + 1)):
        ngrams.append(paddedline[i:i+length])
    return ngrams

def createProbDict(fname):
    if fname in os.listdir():
        return
    con = sqlite3.connect(fname)
    cur = con.cursor()
    cur.execute('''CREATE TABLE probabilities (primary text, secondary text, probability real)''')
    con.commit()
    con.close()

def run():
    return

if __name__ == "main":
    run()