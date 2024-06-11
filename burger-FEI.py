from datetime import datetime
from os import remove

#Menu inicial de opções 
def menu_opcoes():
  
  print("1 - Novo Pedido")
  print("2 - Cancela Pedido")
  print("3 - Insere produto")
  print("4 - Cancela produto")
  print("5 - Valor do pedido")
  print("6 - Extrato do pedido\n")
  print("0 - Sair") 

menu_opcoes()

#Função para inserir "cpf" e "senha"
def dados():
  #Variavéis (cpf, senha) globais
  global cpf
  global senha
  
  cpf = (input("Insira seu cpf: "))
  senha = (input("Insira sua senha: "))
  print()

#Funão para verificar contas
def verificacao():

  #O arquivo será lido e transformado e lista.
  with open("%s.txt"% str(cpf), "r") as conta:
    a = conta.read()
    b = a.split()
    #Caso os índices "1" e "2" sejam iguais ao cpf e a senha a verificação estará concluida
    if b[1] == cpf and b[2] == senha:
      return True
    #Caso contrário será informado um erro
    else:
      print("CPF ou senha inválidos!")
      print()
      

#Opção "1" Novo Pedido
def novo_pedido():  
  
  #Inserção de dados (Nome, cpf, senha)
  nome = input("Digite seu nome: ")
  dados()

  #Caso o usuário crie uma senha com um tamanho diferente de "8" ou digite o cpf errado
  if len(senha) != 8 or len(cpf) != 11:
    print("Senha curta ou longa demais ou cpf incorreto! Tente novamente.") 
    dados()
  
  #Caso exista um pedido com o cpf escrito aberto o cliente será notificado
  try:
    with open("%s.txt"% str(cpf), "r") as conta:
      print("Você já tem um pedido em aberto!")
      print()
      conta.close()
      menu_opcoes()
  
  #Caso não exista um pedido com o cpf escrito será criado um pedido
  except:
    with open("%s.txt"% str(cpf), "w") as conta:
      conta.write("%s %s %s\n" % (nome, cpf, senha))
      conta.close()
      menu_produtos()
      
      
#Opção "2" Cancela Pedido
def cancela_pedido():
  
  #Verificação e inserção de dados (Caso os dados estejam correto o pedido do usuário será cancelado)
  dados()
  if verificacao() == True:
    remove("%s.txt"% str(cpf))
    print("Pedido cancelado!")
    print()

  menu_opcoes()
  

#Opção "3" Insere um produto no pedido do cliente
def insere_produto():  
  
  #Variáveis do código e da quantidade do produto que o cliente irá adicionar ao seu pedido
  codigo_produto = int(input("Digite o código do produto: "))
  quantidade = int(input("Digite a quantidade deseje adicionar: "))

  #Lista dos preços dos produtos
  preço_un = [10, 10, 7.5, 8, 5.5, 4.5, 6.25]  
  
  
  #Passar elementos do arquivo para uma matriz
  matriz = []
  with open("%s.txt" % str(cpf),"r") as ler_conta:
    a = ler_conta.readlines()
    for linha in a:
      b = linha.split()
      matriz.append(b)

    
    contador = 0
    for i in range(len(matriz)):
    
      #Caso já exista um produto dentro do pedido e o cliente queira adicionar mais, a quantidade será atualizada
      if codigo_produto == int(matriz[i][1]):
        matriz[i][0] = quantidade + int(matriz[i][0])
        contador += 1
        
        #Aqui o arquivo será reescrito com a nova quantidade
        with open("%s.txt" % str(cpf),"w") as escrever_conta:
          
          for i in matriz:
            for elemento in i:
              escrever_conta.write("%s "% elemento)
            escrever_conta.write("\n")
            
        #Pergunta ao cliente se ele gostaria de adicionar outro produto a seu pedido
        print("Você gostaria de adicionar outro produto? ")
        print()
        print("0 = não")
        print("1 = sim")
        resp = int(input("R: "))
        print()
        
        #Se a resposta for "nao" o cliente voltará para o Menu de opções
        if resp == 0:
          menu_opcoes()
          
        #Se a resposta for "sim" o cliente será encaminhado para o Menu de produtos
        elif resp == 1:
          menu_produtos()
          print()
        
        #Caso há erro de digitação
        else:
          print("Resposta inválida")
          menu_opcoes()
          

    with open("%s.txt"% str(cpf), "a") as conta:

      #Se o número digitado for válido, ele será armazenado final do pedido do cliente
      if (0 < codigo_produto < 7) and quantidade > 0 and contador == 0:
        conta.write("%s %s %.2f\n" % (quantidade, codigo_produto, preço_un[codigo_produto-1]))
        print()
        conta.close()
        print()
      
        #Pergunta ao cliente se ele gostaria de adicionar outro produto a seu pedido
        print("Você gostaria de adicionar outro produto? ")
        print()
        print("0 = não")
        print("1 = sim")
        resp = int(input("R: "))
        print()
        
        #Se a resposta for "nao" o cliente voltará para o Menu de opções
        if resp == 0:
          menu_opcoes()
          
        #Se a resposta for "sim" o cliente será encaminhado para o Menu de produtos
        elif resp == 1:
          menu_produtos()
          print()
        
        #Caso há erro de digitação
        else:
          print("Resposta inválida")
          menu_opcoes()
  
      
#Opção "4" Cancela Produto
def cancela_produto():
  
  #Verificação e inserção de dados
  dados()
  if verificacao() == True:
  
    #Variáveis do código e da quantidade do produto que o cliente irá cancelar do seu pedido
    codigo = int(input("Digite o código do produto que gostaria de cancelar: "))
    quantidade = int(input("Digite a quantidade do produto que deseja cancelar: "))
    print()

    #Passar elementos do arquivo para uma matriz
    matriz = []
    with open("%s.txt" % str(cpf),"r") as ler_conta:
      a = ler_conta.readlines()
      for linha in a:
        b = linha.split()
        matriz.append(b)


      prod_cancel = []
      qnt_nova = []
      contador = 0
      
      #Adicionar no arquivo o produto cancelado e o produto com a quantidade restante
      for i in range(len(matriz)):  
        if str(codigo) == matriz[i][1]:
          nova_quantidade = int(matriz[i][0]) - quantidade
          contador += 1
          for elemento in matriz[i]:
            prod_cancel.append(elemento)
            qnt_nova.append(elemento)
          prod_cancel.append("cancelado")
          matriz.append(prod_cancel)

      #Caso o cliente digitar um código que não tem em seu pedido o contador não mudará e sera mostrada uma mensagem de erro
      if contador == 0:
          print("O produto digitado não está em seu pedido!")
          print()
          menu_opcoes()
      
      #Caso a quantidade nova não seja menor ou igual a zero, ela será adicionada no lugar da quantidade antiga no final do pedido
      elif nova_quantidade > 0:
        matriz.append(qnt_nova)
        matriz[-1][0] = nova_quantidade
        menu_opcoes()

        #Reescrever código
        with open("%s.txt" % str(cpf), "w") as conta:
          for i in matriz:
            for elemento in i:
              conta.write("%s "% elemento)
            conta.write("\n")
    

      #Caso a quantidade nova seja igual a zero, não será adicionada uma nova quantidade no final do pedido
      elif nova_quantidade == 0:
        pass

      else:
        print("Quantidade inválida!")
        print()
        menu_opcoes()
    

#Opção "5" Valor do Pedido
def valor_pedido():

  #Adiciona os elementos do arquivo em uma lista
  lista = []
  with open("%s.txt" % str(cpf), "r") as conta:
    a = conta.readlines()
    for i in a:
      b = i.split()
      lista.append(b)
      
    #É criado uma variável global para reutiliza-lá no "extrato_pedido"
    global valor_total
    valor_total = 0


    for i in range(len(lista)):
        
        #Caso o elemento da lista NÃO seja um produto cancelado, o valor do produto será somado ao valor anterior
        if i > 0 and lista[i][-1] != "cancelado":
          valor_total = valor_total + (int(lista[i][0])*float(lista[i][2]))
        
        #Caso o elemento da lista SEJA um produto cancelado, o valor do produto será subtraído ao valor anterior
        elif lista[i][-1] == "cancelado":
          valor_total = valor_total - (int(lista[i][0])*float(lista[i][2]))
      

#Opção "6" Extrato do Pedido
def extrato_pedido():
  
  dados()
  valor_pedido()
  
  
  
  #Lista do produtos 
  produto = ["X-salada", "X-burguer", "Cachorro Quente", "Misto Quente", "Salada de Frutas", "Refrigerante", "Suco natural"]

  #Adicionando elementos do arquivo em uma lista
  lista = []
  with open("%s.txt" % str(cpf), "r") as conta:
    a = conta.readlines()
    for i in a:
      b = i.split()
      lista.append(b)

    print("Nome:", lista[0][0])
    print("CPF:", cpf)
    print("Total: R$ %.2f"% valor_total)
    print("Data:", datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("Itens do pedido:")

    for i in range(len(lista)):
      
      #Caso o produto não esteja cancelado, será mostrado na tela a quantidade, nome do produto, preço unitário e valor total do produto
      if i > 0 and lista[i][-1] != "cancelado":
        print("%s - %16s - Preço unitário: %5s  Valor: + %.2f" % (lista[i][0], produto[int(lista[i][1]) - 1], lista[i][2], int(lista[i][0])*(float(lista[i][2]))))


      #Caso o produto esteja cancelado, será mostrado na tela a quantidade, nome do produto, preço unitário, valor total do produto e um "cancelado no final"
      elif lista[i][-1] == "cancelado":
        print("%s - %16s - Preço unitário: %5s  Valor: - %.2f - Cancelado" % (lista[i][0], produto[int(lista[i][1]) - 1], lista[i][2], int(lista[i][0])*(float(lista[i][2]))))
    

  
#Menu do Burguer FEI
def menu_produtos():
  
  print("%10s %10s %15s"% ("Código", "Produto", "Preço"))
  print()
  print("%5s %16s %17s"% ("1", "X-salada", "R$ 10,00"))
  print("%5s %16s %17s"% ("2", "X-burger", "R$ 10,00"))
  print("%5s %23s %9s"% ("3", "Cachorro quente", "R$ 7,50"))
  print("%5s %20s %12s"% ("4", "Misto quente", "R$ 8,00"))
  print("%5s %24s %8s"% ("5", "Salada de frutas", "R$ 5,50"))
  print("%5s %20s %12s"% ("6", "Refrigerante", "R$ 4,50"))
  print("%5s %20s %12s"% ("7", "Suco natural", "R$ 6,25"))
  print()
  
  #Move para a funçao de inserir produtos
  insere_produto()
  
#Escolha de opção do menu
while True:
  print()
  opçao_escolhida = int(input("Digite uma das opções acima: "))
  print()

  #Caso o cliente digite o número "1", ele será direcionado para a opção "Novo Pedido"
  if opçao_escolhida == 1:
    novo_pedido()

  #Caso o cliente digite o número "2", ele será direcionado para a opção "Cancela Pedido"
  elif opçao_escolhida == 2:
    cancela_pedido()
  
  #Caso o cliente digite o número "3", ele será direcionado para a opção "Insere Produto"
  elif opçao_escolhida == 3:
    dados()
    #Verificação de conta
    if verificacao() == True:
      menu_produtos() 
    else:
      menu_opcoes()
  
  #Caso o cliente digite o número "4", ele será direcionado para a opção "Cancela Produto"
  elif opçao_escolhida == 4:
    cancela_produto()

  #Caso o cliente digite o número "5", ele será direcionado para a opção "Valor do Pedido"
  elif opçao_escolhida == 5:
    
    #Caso o usuário passe pela verificação de seus dados o valor de seu pedido será mostrado
    dados()
    if verificacao() == True:
      valor_pedido()
      print("Valor do Pedido: R$ %.2f"% valor_total)
      print()
      menu_opcoes()
  
  #Caso o cliente digite o número "6", ele será direcionado para a opção "Extrato do Pedido"
  elif opçao_escolhida == 6:
    extrato_pedido()
    print()
    menu_opcoes()
  
#Encerrar programa  
  elif opçao_escolhida == 0:
    print("Obrigado! Volte sempre")
    break