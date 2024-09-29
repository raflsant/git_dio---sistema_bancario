
# sistema_bancario

    Projeto apresentado para o bootcamp "NTT DATA - Engenharia de Dados com Python", uma parceria da NTT DATA com a Dio.






# Instalação

Não é necessário baixar ou importar nenhuma biblioteca.
No git:

```bash
  https://github.com/raflsant/git_dio.git
```
Isso dará acesso não só a esse proojeto, mas também aos outros projetos do curso.

# v1

# Funcionamento

Nesse desafio, terei que seguir algumas premissas básicas:

    # Menu de opções deve ter 3 opções: depósito, saque e extrato.
    # Deve conter apenas um usuário nessa primeira versão.
    
    # DEPÓSITOS:
        # Apenas valores inteiros.
        # Armazenados em uma variável para serem exibidos em extrato.
    # SAQUES:
        # Apenas 3 saques diários.
        # Limite de R$500.00 por saque.
        # Caso não tenha saldo, exibir mensagem de erro.
        # Armazenados em uma variável para serem exibidos em extrato.
    # EXTRATOS:
        # Lista todos os depósitos e saques realizados.
        #Valores tem que ser exibidos no formato "R$xxxx.xx"
    # Obs: nesse exemplo, essa conta bancária terá um saldo incial de R$1000.00.
## Bugs

#### Inserção de valores tipo string

Ao inserir valores do tipo string nas opções de depósito ou saque, o código para. Por enquanto, na sua versão v1, ainda não tenho a solução para esse bug.

# v2:

# Funcionamento

Mudanças da versão 2 do código:

    # As três opções básicas (saque, depósito e extrato) foram transformadas em funções.
    # Foram criadas também as opções de criar usuário e criar conta (ambas também são funções).
    # Foi criada uma função chamada main() para organizar o código.
    # Foi criada uma função chamada filtrar_usuario() para buscar usuários pelo CPF.
    # Foi criada uma função lista_contas() para exibir todas a contas cadastradas.

    # DEPÓSITOS:
        # A função deposito utiliza somente argumentos posicionais.
    # SAQUES:
        # A função saque utiliza somente argumentos nomeados.
    # EXTRATOS:
        # A função exibir_extrato usa argumentos posicionais e nomeados.
        # Agora cada transação mostra a data e hora em que foi realizada (usando datetime).
    # CRIAR USUÁRIO:
        # Armazena dos usuários em uma lista, com nome, data de nascimento (usando datetime), CPF e endereço.
            # O endereço é uma string composta por logradouro, número, bairro e cidade/UF.
            # O CPF aceita apenas números.
            # Não é possível cadastrar mais de um usuário com o mesmo CPF.
    # CRIAR CONTA:
        # A função criar_conta armazena as contas em uma lista
            # A conta contém agência, número de conta e usuário.
            # A agência é 0001 por padrão.
            # O número da conta é sequencial, começando em 1.
            # Um usuário pode ter mais de uma conta, mas cada conta em apenas um usuário.
