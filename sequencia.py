import random
import copy

def criaPop(pop, chromoSize):
    chromo = []
    
    for i in range(len(pop)):
        for j in range(0, chromoSize):
            chromo.append(random.randint(0,1))
            vetor = copy.deepcopy(chromo)
        pop[i] = vetor
        chromo.clear()

    return pop

def mutação(chromo = []):
    i = random.randint(0,7)
    
    if(chromo[i] == 0):
        chromo[i] = 1
    else:
        chromo[i] = 0

    return chromo

def cruzamento(pai, mae, filho1, filho2):

    filho1[0] = pai[0]
    filho1[1] = pai[1]
    filho1[2] = pai[2]
    filho1[3] = pai[3]
    filho1[4] = mae[4]
    filho1[5] = mae[5]
    filho1[6] = mae[6]
    filho1[7] = mae[7]

    filho2[0] = mae[0]
    filho2[1] = mae[1]
    filho2[2] = mae[2]
    filho2[3] = mae[3]
    filho2[4] = pai[4]
    filho2[5] = pai[5]
    filho2[6] = pai[6]
    filho2[7] = pai[7]

    return filho1, filho2

def selecao(pop, filhos):
    for k in range(0, len(pop)-2, 2):
        
        i, j = 0, 0
        while i == j:
            i = random.randint(0,7)
            j = random.randint(0,7)

        filhos[k], filhos[k+1] = cruzamento(pop[i], pop[j], filhos[k], filhos[k+1])

    return filhos

def adaptacao(pop):
    popAdapt = []

    for i in range(len(pop)):
        popAdapt.append(0)
        for j in range(len(pop[0])-1):
            if(pop[i][j] == 0 and pop[i][j+1] == 1):
                popAdapt[i] = popAdapt[i] + 1
                j = j + 1

    return popAdapt

def ordenacaoPAIA(pop, adaptacao):
    popOrdenado = []
    adaptOrdenada = []

    i = 0
    j = 1

    while len(popOrdenado) != len(pop)-1:
        if(i == j and j+1 < len(pop)-3):
            j = j + 1
        if(i > 6 or j > 6):
            print("opa")
            print(len(popOrdenado))
            print(len(pop))
            break
        
        if(adaptacao[i] < adaptacao[j]):
            popOrdenado.append(pop[j])
            adaptOrdenada.append(adaptacao[j])
            j = j + 1

        else:
            popOrdenado.append(pop[i])
            adaptOrdenada.append(adaptacao[i])
            i = i + 1

def ordenacao(pop, adaptacao):
    for i in range(len(pop)):
        for j in range(len(pop)):
            if adaptacao[i] < adaptacao[j]:
                tempChromo = pop[i]
                tempAdapt = adaptacao[i]

                pop[i] = pop[j]
                adaptacao[i] = adaptacao[j]

                pop[j] = tempChromo
                adaptacao[j] = tempAdapt
                
    return pop, adaptacao

def substituicao(pop, filhos, popAdapt, filhosAdapt):
    novaPop = []
    novaAdapt = []

    i = 0
    j = 0

    while len(novaPop) != len(pop):
        if popAdapt[i] > filhosAdapt[j]:
            novaPop.append(pop[i])
            novaAdapt.append(popAdapt[i])
            i = i + 1
        else:
            novaPop.append(filhos[j])
            novaAdapt.append(filhosAdapt[j])
            j = j + 1
    
    return novaPop, novaAdapt

def printaPop(pop, popSize, chromoSize):
    for i in range(0, popSize):
        for j in range(0, chromoSize):
            print(pop[i][j])
        print("\n")

def printAdaptacao(adaptacao, popSize):
    for i in range(popSize):
        print(adaptacao[i])

if __name__ == "__main__":
    pop = []
    for i in range(0,8):
        pop.append(0)
    
    pop = criaPop(pop,8)
    adapt = []
    
    filhos = []
    for i in range(0,8):
        filhos.append(0)
        
    filhos = criaPop(filhos, 8)
    filhosAdapt = []

    adapt = adaptacao(pop)
    filhosAdapt = adaptacao(filhos)

    i = 0

    while adapt[0] != 4:
        adapt = adaptacao(pop)
    
        j, k = 0, 0 

        while j == k:
            j = random.randint(0, 7)
            k = random.randint(0, 7)


        mutação(pop[j])
        mutação(pop[k])

        pop, adapt = ordenacao(pop, adapt)

        filhos = selecao(pop, filhos)
        filhosAdapt = adaptacao(filhos)

        filhos, filhosAdapt = ordenacao(filhos, filhosAdapt)

        pop, adapt = substituicao(pop, filhos, adapt, filhosAdapt)

        adapt = adaptacao(pop)
                
        i = i + 1


    print(f"Solução encontrada apos {i+1} gerações:")
    
    print(f'{pop[0]} e adaptação = {adapt[0]}')