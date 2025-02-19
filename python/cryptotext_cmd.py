from cryptotext import CryptoText

ct = CryptoText()

while True:
  print("Hola, vamos a cifrar o descifrar mensajes.\nElegí el modo:\n1. Cifrar César\n2. Descifrar César\n3. Espejo\n4. Descifrar espejo\n5. Super espejo\n6. Descifrar super espejo", end="\n\n")
  mode = input()
  if mode == "1":
    while True:
      print("Necesito un número del 1 al 26", end="\n\n")
      n = input()
      try:
        n = int(n)
      except:
        break
      print("Ok. Vamos con " + str(n) + ". Mandame el mensaje ahora.", end="\n\n")
      m = input()
      c = ct.caesar_cypher(n, 27, m, 0)
      print(c, end="\n\n")
  elif mode == "2":
    while True:
      print("Necesito un número del 1 al 26", end="\n\n")
      n = input()
      try:
        n = int(n)
      except:
        break
      print("Ok. Vamos con " + str(n) + ". Mandame el mensaje ahora.", end="\n\n")
      m = input()
      c = ct.caesar_decypher(n, 27, m, 0)
      print(c, end="\n\n")
  elif mode == "3":
    while True:
      print("Necesito una cadena de texto clave", end="\n\n")
      n = input()
      if n == "  ":
        break
      print("Ok. Vamos con <" + n + ">. Mandame el mensaje ahora.", end="\n\n")
      m = input()
      c = ct.mirror_cypher(n, m)
      print(c, end="\n\n")
  elif mode == "4":
    while True:
      print("Necesito una cadena de texto clave", end="\n\n")
      n = input()
      if n == "  ":
        break
      print("Ok. Vamos con <" + n + ">. Mandame el mensaje ahora.", end="\n\n")
      m = input()
      c = ct.mirror_decypher(n, m)
      print(c, end="\n\n")
  elif mode == "5":
    while True:
      print("Necesito una lista de cadenas de texto clave separadas por &", end="\n\n")
      n = input()
      if n == "  ":
        break
      print("Ok. Vamos con <" + n + ">. Mandame el mensaje ahora.", end="\n\n")
      m = input()
      c = ct.mirror_super_cypher(n.split("&"), m)
      print(c, end="\n\n")
  elif mode == "6":
    while True:
      print("Necesito una lista de cadenas de texto clave separadas por &", end="\n\n")
      n = input()
      if n == "  ":
        break
      print("Ok. Vamos con <" + n + ">. Mandame el mensaje ahora.", end="\n\n")
      m = input()
      c = ct.mirror_super_decypher(n.split("&"), m)
      print(c, end="\n\n")
  else:
    print("No te entiendo. Repito...", end="\n\n")
    break

