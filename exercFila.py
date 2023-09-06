
# -*- coding: utf-8 -*-

#from array_queue import ArrayQueue  # array_queue.py eh o nome do arquivo(modulo) e ArrayQueue eh a classe
from array_queue_new import ArrayQueue  # array_queue.py eh o nome do arquivo(modulo) e ArrayQueue eh a classe
from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import *
#from listaSimplesmenteEncadeadaComIteradorFinal_Solucao import SinglyLinkedListIterator



if __name__ == "__main__":

    

    def printFila(q): #queue fila
        copia = ArrayQueue()  # instaciou fila auxiliar
        # loop na fila q
        while not q.is_empty():
            print(q.first())
            copia.enqueue(q.dequeue())
        # loop na  copia
        while not copia.is_empty():
            q.enqueue(copia.dequeue())

        

    """1) Fila copiarFila( Fila f ) 
Fazer uma cópia de uma Fila, usando como apoio uma lista. Também é 
possível usar como apoio uma fila. A Fila original deve ser restaurada."""

    def copiarFila(f):
        copia = ArrayQueue() # copia a ser retornada
        restaura = ArrayQueue()  # fila para restaurar a fila original
        # loop na fila f para remover e adicionar na fila restaura
        while not f.is_empty():
            elem = f.dequeue()
            copia.enqueue(elem)
            restaura.enqueue(elem)

        #restaura a fila original
        while not restaura.is_empty():
            f.enqueue(restaura.dequeue())

        restaura = None
        return copia


    def copiarFila_2(f):
        copia = ArrayQueue() # copia a ser retornada
        restaura = ArrayQueue()  # fila para restaurar a fila original
       
        return copia



    def copiarFilaUsandoLista(f):
        copia = ArrayQueue() # copia a ser retornada
        lst = SinglyLinkedListIterator() # copia para restaurar a fila f
        while not f.is_empty():
            lst.addnode(f.dequeue())
            copia.enqueue(lst.iterator.data)
        lst.iterator = lst.iterator.firstNode
        while lst.iterator:
            f.enqueue(lst.iterator.data)
            lst.elimNode()
        return copia

    """3) void concatFilas(Fila f1, Fila f2) 
    Concatenar duas filas, deixando o resultado na primeira(f1). A fila f2 deve 
ser restaurada. Sugestão: usar como apoio outra fila."""
    def concatFilas(f1, f2):
        #se fila f2 NAO NAO NAO for vazia:

        if not f2.is_empty():
            copia_f2 = copiarFila(f2)
            while not f2.is_empty():
                f1.enqueue(copia_f2.dequeue())
            
        

    # Dever de casa: fazer esta funcao !!!!!!! <<<------
    # concatenar f2 no final de f1. Usar como apoio uma lista.
    # def concatFilasInteligente(f1, f2):
    #
    #     # ... completar
    #


    # def concatFilas2(f1, f2):
    #     copia = copiarFila(f2)
    #     # ... completar


    """10) primeiroDaFila( Fila f, TipoF elem) 
Coloca o elemento elem na primeira posição da fila. """
    def primeiroDaFila(fila, elem):
        filaApoio = ArrayQueue() # crio uma nova fila para guardar
        



    def elimina_elemento_novo(fila, elem):
        if not fila.is_empty():
            # instanciar uma fila de apoio
            fila_apoio = ArrayQueue()
            



    # adicionar o elmento elem numa posicao pos dada.
    def adicionaNaPosicaoPos(fila, elem, posicao):
      pass  

    """5) int existeElemento( Fila f, TipoF elem) 
Retorna true(1) se o elemento elem está presente na fila e false(0) caso 
contrário. """

    # def existeElemento(fila, elem):
  



    def printLista(lista):
        lista.first_Node() # por o iterador sobre o primeiro elemento
        while not lista.isUndefinedIterator():
            print(lista.iterator.data)
            lista.nextNode() # avanca iterador para proximo noh
            #lista.iterator = lista.iterador.nextNode
        print('\n')

    Q = ArrayQueue() # cria uma fila vazia
    Q.enqueue(5) # adiciona no fim da fila o 5
    printFila(Q) # [5 ]
    Q.enqueue(3) # adiciona no fim da fila o 3
    printFila(Q) # [5 3 ]
    Q.enqueue(8)  # adiciona no fim da fila o 8 # [5 3 ]
    print('tamanho da fila = {}'.format(len(Q))) # tamanho da fila = 2
    print("===============================")
    print("=========Copirar Fila======================")
    copia_1 = copiarFila(Q)
    copia_2 = copiarFila_2(Q)
    print("=========Print Fila copiada copia_1======================")
    printFila(copia_1)
    print("=========Print Fila copiada copia_2======================")
    printFila(copia_2)
    print("=================Por 1000 como Primeiro elemento=========================")
    primeiroDaFila(Q,1000)
    printFila(Q)
    print("============Na posicao 2 vou por o elem 300=============")
    adicionaNaPosicaoPos(Q,300, 2)
    printFila(Q)
    print("=================Remover o elem 300 ==========================")
    elimina_elemento_novo(Q, 300)
    printFila(Q)
    print("============concatenar f2 no final de f1===============================")
    concatFilas(Q, copia_1)
    printFila(Q)
    print("=============== FIMFIMFIMFIMFIMFIM============================")
    copiarFilaUsandoLista(Q)


    # testando a lista
    # lst = SinglyLinkedListIterator()
    # for i in range(30):
    #     lst.addNode(i)
    # printLista(lst)


