def sed(pattern, replacement, fileRead, fileWrite):
    try:
        fin = open(fileRead)
        fout = open(fileWrite, 'w')

        for line in fin:
            line.replace(pattern, replacement)
            fout.write(line)

        fin.close()
        fout.close()
    except:
        print("Something went wrong")
