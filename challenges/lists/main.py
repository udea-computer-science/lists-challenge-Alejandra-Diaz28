if __name__ == '__main__':
n = int(input())
lista=[]
for i in range(0,n):
  comando=input("inserta tu comando_ejemplo: insert 0 5")
  comando=comando.split(" ")
  if comando[0]=="insert":
    lista.insert(int(comando[1]),int(comando[2]))
  elif comando[0]=="append":
    lista.append(int(comando[1]))
  elif comando[0]=="remove":
    lista.remove(int(comando[1]))
  elif comando[0]=="reverse":
    lista.reverse()
  elif comando[0]=="pop":
    lista.pop()
  elif comando[0]=="sort":
    lista.sort()
  elif comando[0]=="print":
    print(lista)
    N = int(input())
    
    