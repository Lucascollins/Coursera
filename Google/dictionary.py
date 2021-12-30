file_counts = {"jpg":10, "txt":14,"csv":2,"py":23}
print(file_counts["txt"])
"jpg" in file_counts
"html" in file_counts
file_counts["cfg"] = 8
print(file_counts)
file_counts["csv"] = 12 #quando vc tenta colocar o mesmo nome de uma "variavel" é substituindo o valor
print(file_counts)
del file_counts["cfg"]
print(file_counts)





#O dicionário "toc" representa o índice de um livro. Preencha os espaços em branco para fazer o seguinte: 
#1) Adicione uma entrada para Epílogo na página 39. 
#2) Altere o número da página do Capítulo 3 para 24. 
#3) Exiba o novo conteúdo do dicionário. 
#4) Exibir True se houver Capítulo 5, False se não houver.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
if "Chapter 5" in toc:
    print(True)
else:
    print(False) # Is there a Chapter 5?