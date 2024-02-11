files = ["borges_biblioteca.txt", "borges_funes.txt", "borges_jardin.txt", "borges_ruinas.txt",
        "cortazar_casa.txt", "cortazar_escalera.txt", "cortazar_reloj.txt"]

word_sets = [set() for i in range(15)]

for i in range(len(files)):
    lines = open("data/" + files[i]).readlines()
    for l in lines:
        cleaned = l.replace("\n", "")
        for word in cleaned.split(" "):
            position = len(word) - 2
            if position >= 0 and position < 15:
                word_sets[position].add(word.lower())
    
    output = open("output/words_" + files[i], "w")
    for s in word_sets:
        line = ""
        for word in s:
            line += word
            line += " "
        line += "\n"
        line = line.replace(".", "")
        line = line.replace(",", "")
        line = line.replace(";", "")
        line = line.replace(":", "")
        line = line.replace("-", "")
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace("¿", "")
        line = line.replace("?", "")
        line = line.replace("!", "")
        line = line.replace("¡", "")
        output.write(line)
    output.close()
    
    for s in word_sets:
        s.clear()