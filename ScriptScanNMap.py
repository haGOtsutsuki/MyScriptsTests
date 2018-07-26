print("Scan NMap")

inputip = input("Digite o endereço: ")
    if inputip = string():
        print("Digite o endereço corretamente: ")
    
    elif inputip = float():
        nmap -sn -n (inputip) | cut -d ' ' -f 5
    
    else: inputip = string():
        print("ERRO_\n Endereço Inválido!")
        close.close()
