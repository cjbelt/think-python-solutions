import os

for root, dirs, files in os.walk('/home/caique/Documents/Engenharia da Computacao'):
    print(root, dirs, files)
