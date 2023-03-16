nascimento = 1997
nome = 'Caio'
nascimentoJovem = 2006
anoAtual = 2023

def calculoIdade(nascimento, anoAtual):
    idade = anoAtual - nascimento
    idadejovem = anoAtual - nascimentoJovem 
    return idade
idade = calculoIdade(nascimento, anoAtual)
idadeJovem = calculoIdade(nascimentoJovem, anoAtual)

print ('A idade do Caio é '  +  str(idade))
print ('A idade da Mari é '  +  str(idadeJovem))