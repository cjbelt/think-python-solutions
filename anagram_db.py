import anagram_sets
import dbm
import pickle

def store_anagrams(d, db_name):
    db = dbm.open(db_name, 'c')
    for letters in d:
        db[letters] = pickle.dumps(d[letters])

    db.close()

def read_anagrams(word, db):
    t = list(word)
    t.sort()
    letters = ''.join(t)

    try:
        db_file = dbm.open(db)
    except:
        print("File %s doesn't exist." % db)
        return

    anagram_list = pickle.loads(db_file[letters])
    db_file.close()
    return anagram_list

# anagrams_d = anagram_sets.all_anagrams('words.txt')
# store_anagrams(anagrams_d, 'anagrams.db')
# print(read_anagrams("post", 'anagramz.db'))
