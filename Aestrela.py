from re import S
import math
import matplotlib.pyplot as plt

#src e end  uma class 
# def heuristic calcula a distancia
def heuristic(src, end):
    # formula heuristica utilizada para calcular a distancia entre dois pontos
    # neste caso, distancia euclidiana
    #print(src , end)q
  
  #  print("src",src ,"end",end ,">",+1)
   # print ("raiz",math.sqrt((src[0] - end[0])**2 + (src[1] - end[1])**2))
    return math.sqrt((src[0] - end[0])**2 + (src[1] - end[1])**2)

#função que criar os pontos 

def graphPlot(grafo, comeco, objetivo, rota):
    arestas = []
    #separar info
    for num in grafo:
        for i in grafo[num][1]:
            if (i, num) not in arestas:
                arestas.append((num, i))
    # plotar(coloca as aresta no grafo) arestas
    for a, b in arestas:
        plt.plot((grafo[a][0][0], grafo[b][0][0]), (grafo[a][0][1], grafo[b][0][1]), c = 'yellow')
    # plotar nos
    plt.plot([grafo[num][0][0] for num in grafo], [grafo[num][0][1] for num in grafo], 'd') # aqui eu estou definindo o simbolo da coodernada 
    # plotar rota, inicio e fim
    plt.plot([grafo[i][0][0] for i in rota], [grafo[i][0][1] for i in rota], ls='--', c= 'red',label='caminho mais rapido')        #ls e  a rota que ele percorrer 
    plt.plot(grafo[comeco][0][0], grafo[comeco][0][1], marker = 's', c = 'green', label='começo')                                  # esse s  e  de squard o algoritmo vai coloca um quadrado
    plt.plot(grafo[objetivo][0][0], grafo[objetivo][0][1], marker = "X", c = 'red', label='objetivo')                              # x  e de  x o algoritmo vai colocar um x 
    plt.grid()
    plt.legend()
    plt.show()

def AStar(grafo, comeco, objetivo):
    G = {} # distancia desde o no inicial para o proximo
    F = {} # distancia estimada ate o destino
    H = {} # distancia heuristica do no N ate o destino
    G[comeco] = 0
    F[comeco] = H[comeco] = heuristic(grafo[comeco][0], grafo[objetivo][0]) # F = G + H, como G = 0, entao F = H 
    previous = {}
    visited = set()
    queue = set([comeco])

    
    while len(queue) > 0:

        esseNo = comeco   
        
        esseFinito = float('infinity')  #     usamos float(inf ) como um inteiro para representa uma infinidade
       
        
        for i in queue: # percorre a fila atras do menor F
           
            # print("Dentro do for que ta dentro do while thisF",thisF,)
            if F[i] < esseFinito or esseNo == comeco:
                esseFinito = F[i]
                esseNo = i
               
        # testa se o atual eh o destino
        if esseNo == objetivo:
        
            rota = [esseNo]
            
            while esseNo in previous:
                esseNo = previous[esseNo] # se sim, refaz o percurso para registrar a rota e plota o grafico
              
                rota.append(esseNo) # adicionar esseNo em rota
            rota.reverse()  # reveter a ordenação da lista
            print("rota",rota,"\nF: ", F[objetivo])
            graphPlot(grafo, comeco, objetivo, rota)
            return
 
       
        queue.remove(esseNo)
        visited.add(esseNo)
        
        for adj in grafo[esseNo][1]: # checa os nos adjacentes
            # print("grafo[esseNo][1]",grafo[esseNo][1])
            if adj in visited: # se ja tiver passado por ele, continua
            
                continue
            # senao, calcula o G
            adjG = G[esseNo] + heuristic(grafo[esseNo][0], grafo[adj][0])
          
            # se adjacente nao estiver na fila, o adiciona
            if adj not in queue:
               
                queue.add(adj)
                
            # testa se o G atual eh maior que o ja salvo. Se sim, ignora
            elif adjG >= G[adj]:
                
                continue
            # se nao, atualiza os dados
            previous[adj] = esseNo
            G[adj] = adjG
            # calcula H se ja nao tiver sido calculado antes
            
            if adj not in H:
                
                H[adj] = heuristic(grafo[adj][0], grafo[objetivo][0])
                
            F[adj] = G[adj] + H[adj] # calcula e armazena F
            


# Grafo
# Formato: { no : [(coordenadas), (conexoes)] }
Grafo_no = {
    'A': [(2, 1), ('B','C')],
    'B': [(2, 3), ('A', 'C','D')],
    'C': [(4, 3), ('A', 'B','E')],
    'D': [(6, 7), ('B', 'F')],
    'E': [(6, 4), ('C', 'F')],
    'F': [(9, 9), ('D', 'E')]
}
comeco = 'A'
objetivo = 'E'
# começo = Grafo_no['A'][0]
# objetivo = Grafo_no['F'][0]

AStar(Grafo_no, comeco, objetivo)
