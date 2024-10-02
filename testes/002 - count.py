txt = input("Digite um texto: ")

if 'a' in txt:
    letters_in_txt = txt.lower().count('a')
    print("Existem " + str(letters_in_txt) + " letras A no texto.")

else:
    print("Não existem letras a no texto.")
