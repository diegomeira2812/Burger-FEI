# Sistema de Pedidos do Burguer FEI

Este é um sistema simples para gerenciar pedidos em uma lanchonete fictícia chamada Burguer FEI. Ele permite que os clientes façam novos pedidos, cancelem pedidos existentes, adicionem produtos aos pedidos, cancelem produtos específicos dentro de um pedido, visualizem o valor total de seus pedidos e obtenham um extrato detalhado de cada pedido.

## Funcionalidades

### 1. Novo Pedido
Os clientes podem fazer novos pedidos, fornecendo seu nome, CPF e senha. Se um cliente já tiver um pedido em aberto, será notificado e não poderá fazer um novo pedido até que o pedido atual seja cancelado.

### 2. Cancela Pedido
Os clientes podem cancelar seus pedidos existentes, fornecendo seu CPF e senha.

### 3. Insere Produto
Os clientes podem adicionar produtos aos seus pedidos existentes. Eles podem escolher entre uma lista de produtos disponíveis e especificar a quantidade desejada.

### 4. Cancela Produto
Os clientes podem cancelar produtos específicos dentro de seus pedidos existentes, fornecendo o código do produto e a quantidade a ser cancelada.

### 5. Valor do Pedido
Os clientes podem verificar o valor total de seus pedidos existentes, fornecendo seu CPF e senha.

### 6. Extrato do Pedido
Os clientes podem obter um extrato detalhado de seus pedidos existentes, incluindo informações sobre cada produto, quantidade, preço unitário e valor total.

## Utilização

1. Execute o script Python `burguer_fei.py`.
2. Siga as instruções do menu para realizar as operações desejadas.

## Pré-requisitos

- Python 3.x

## Observações

- Certifique-se de que os arquivos de texto necessários (um por cliente) estejam no mesmo diretório do script Python.
