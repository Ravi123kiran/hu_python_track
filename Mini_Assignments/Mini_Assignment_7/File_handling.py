def lengthy (file):
    with open(file, 'r') as infile:
              wrd = infile.read().split()
    max_len = len(max(wrd, key=len))
    return [word for word in wrd if len(word) == max_len]

print(lengthy('ravikiran.txt'))
