
def dist_total(pontos_entrega,perm):

    r=pontos_entrega['R']
    linha_r=r[0]
    coluna_r=r[1]
    soma=0
    for x in range(len(perm)):
        y=pontos_entrega[perm[x]]
        linha_y=y[0]
        coluna_y=y[1]
        soma+=abs(linha_r-linha_y)
        soma+=abs(coluna_r-coluna_y)
        if x==len(perm):
            linha_r=r[0]
            coluna_r=r[1]
        else:
            linha_r=linha_y
            coluna_r=coluna_y
    return soma        
def permutacao(lista,result=[]):
    
    if len(lista)==0:
        permuta.append(result)
          
    else:
        for x in range(len(lista)):
            permutacao(lista[:x] + lista[x+1:],result + lista[x:x+1])
            



def main():
    l ,c=list(map(int,input().split()))
    matrix=[]
    for x in range(l):
        linha=input().split()
        matrix.append(linha)
    pontos_entrega=dict()
    lista=[]
    for x in range(l):
        for y in range(c):
            if matrix[x][y]!='0':
                pontos_entrega[matrix[x][y]]=(x, y)
            if matrix[x][y]!='0' and matrix[x][y]!='R':
                lista.append(matrix[x][y])
    
    menor=1000000000000000000000000000000000000000000000
    resultado=[]
    global permuta
    permuta=[]
    permutacao(lista)
    for y in permuta:
        dist=dist_total(pontos_entrega,y)
        if dist<menor:
            menor=dist
            resultado=y
   
        
       
    print(' '.join(resultado))
    
           



if __name__ == '__main__':
    main()    
            



