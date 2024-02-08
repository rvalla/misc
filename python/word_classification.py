files = ["borges_funes.txt", "borges_biblioteca.txt", "borges_jardin.txt"]

word_sets = [set() for i in range(15)]

for i in range(3):
    lines = open("data/" + files[i]).readlines()
    for l in lines:
        cleaned = l.replace("\n", "")
        for word in cleaned.split(" "):
            position = len(word) - 2
            if position >= 0 and position < 15:
                word_sets[position].add(word)
    
    output = open("output/words_" + files[i], "w")
    for s in word_sets:
        line = ""
        for word in s:
            line += word.lower()
            line += ","
        line += "\n"
        output.write(line)
    
    for s in word_sets:
        s.clear()