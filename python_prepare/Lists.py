if __name__ == '__main__':
    N = int(input())
    lista = []
    
    for m in range(N):
        cmd = input().strip()
        cmd = cmd.split(" ")
        if cmd[0]=="insert":
            '''print(cmd[0])
            print(cmd[1])
            print(cmd[2])'''
            lista.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0]=="print":
            print(lista)
        elif cmd[0]=="remove":
            lista.remove(int(cmd[1]))
        elif cmd[0]=="append":
            lista.append(int(cmd[1]))
        elif cmd[0]=="sort":
            lista.sort()
        elif cmd[0]=="pop":
            lista.pop()
        elif cmd[0]=="reverse":
            lista.reverse()
        else:
            print("command not in defined list")