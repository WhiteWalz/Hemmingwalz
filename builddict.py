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
    cur.execute('''CREATE TABLE probabilities (primary text, secondary text, length real, probability real)''')
    con.commit()
    con.close()

def addToProbdict(ngram, fname):
    if not fname in os.listdir(): createProbDict(fname)
    con = sqlite3.connect(fname)
    cur = con.cursor()
    cur.execute('''SELECT length FROM probabilities WHERE length=? AND primary=? AND secondary=?''', (len(ngram), ngram[:-1], ngram[-1]))
    existingEntry = cur.fetchone()
    if not existingEntry:
        #create new entry for ngram in db

        return
    #increment current entry in database
    
    return

def run():
    return

if __name__ == "main":
    run()