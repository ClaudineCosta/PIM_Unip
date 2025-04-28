

import json  # Manipula arquivos JSON.
import os  # Interage com o sistema operacional.
import hashlib  # Criptografa dados.
import re  # Manipula expressões regulares.
import time  # Trabalha com tempo.
import statistics  # Realiza cálculos estatísticos.



# Função para carregar os dados dos usuários de um arquivo JSON
def carregar_dados():    
    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as file:
            return json.load(file)
    return []


# Função para salvar os dados dos usuários em um arquivo JSON
def salvar_dados(usuarios):
    with open('usuarios.json', 'w') as file:
        json.dump(usuarios, file, indent=4)
    print("\nDados salvos com sucesso!")
    
    
# Função para criptografar dados (simples exemplo)
def criptografar_dados(dado):
    return hashlib.sha256(dado.encode()).hexdigest()    
    


# Função para registrar um novo usuário
def registrar_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    email = input("Digite seu e-mail: ")
    consentimento = input("Você consente com o tratamento dos seus dados? (sim/não): ").lower()
  
        # Explicação sobre o consentimento
    print("\nAntes de prosseguir, gostaríamos de explicar o motivo da solicitação.")
    print("De acordo com a Lei Geral de Proteção de Dados Pessoais (LGPD), precisamos do seu consentimento para processar seus dados.")
    print("Se você concordar, seus dados serão utilizados exclusivamente para melhorar a experiência na plataforma e para análise de desempenho.")
    print("Se não concordar, seus dados não serão armazenados e não poderemos oferecer os serviços completos da plataforma.")
    
    # Validações de consentimento
    if consentimento != 'sim' and consentimento != 'não':
        print("Por favor, digite 'sim' ou 'não' para o consentimento.")
        return registrar_usuario()  # Chama a função novamente em caso de resposta inválida
    
    # Criação de um dicionário para o usuário
    usuario = {
        'nome': nome,
        'idade': idade,
        'email': email,
        'consentimento': consentimento
    }
    
      # Criptografando email por motivos de segurança
    usuario['email_criptografado'] = criptografar_dados(usuario['email'])    
    
    print(f"Usuário {nome} registrado com sucesso!")
    return usuario






# Função para exibir o menu e capturar a interação do usuário
def menu():
    print("\nBem-vindo à plataforma educacional!")
    print("1. Registrar usuário")
    print("2. Ensinar Informática Básica")
    print("3. Ver estatísticas de desempenho")
    print("4. Garantir conformidade com LGPD")
    print("5. Otimizar consumo de energia")
    print("6. Sair")
    
    
    
    
# Função para ensinar informática básica
def ensinar_informatica_basica():
    print("\nBem-vindo à seção de Ensino de Informática Básica!")
    print("Aqui, vamos aprender o básico sobre o uso de computadores, infraestrutura, TICs e boas práticas de segurança digital.")
    
    print("\nEscolha um tópico para aprender mais:")
    print("1. O que são TICs (Tecnologias da Informação e Comunicação)?")
    print("2. O que é infraestrutura básica de TI?")
    print("3. O que é um sistema operacional?")
    print("4. Como utilizar programas de edição de texto e planilhas?")
    print("5. Importância de senhas seguras e como criar senhas fortes?")
    print("6. Matemática e Python Fundamental (variáveis, operadores, etc.)")
    
    escolha = input("Digite o número da opção: ")
    
    if escolha == '1':
        print("\nTICs (Tecnologias da Informação e Comunicação) são um conjunto de tecnologias que envolvem o uso de computadores, redes de comunicação, sistemas de informação e dispositivos para coletar, armazenar, processar e transmitir dados.")
        print("Exemplos de TICs: internet, dispositivos móveis, computadores, sistemas de gerenciamento de dados, etc.")
    elif escolha == '2':
        print("\nInfraestrutura básica de TI refere-se aos componentes essenciais de tecnologia que permitem o funcionamento de sistemas de computação.")
        print("Isso inclui hardware (como computadores e servidores), software (sistemas operacionais e aplicativos), redes (como internet e intranets) e segurança (firewalls, criptografia, etc.).")
    elif escolha == '3':
        print("\nSistema operacional é o software básico que permite que você interaja com o computador.")
        print("Exemplos: Windows, Linux, macOS. Ele gerencia recursos como memória, arquivos e dispositivos de entrada/saída.")
    elif escolha == '4':
        print("\nProgramas de edição de texto e planilhas são usados para criar documentos e organizar dados.")
        print("Exemplos: Microsoft Word, Excel, Google Docs. São essenciais para tarefas administrativas e educacionais.")
    elif escolha == '5':
        print("\nSenhas seguras são essenciais para proteger seus dados online.")
        print("Dicas para criar uma senha forte: use uma combinação de letras, números e caracteres especiais, e evite palavras comuns.")
    elif escolha == '6':
        ensinar_matematica_python_fundamental()
    else:
        print("\nOpção inválida! Tente novamente.")
        
   # Retorna ao menu principal após terminar
    input("\nPressione Enter para voltar ao menu principal.")
    menu()     




# Função para ensinar Matemática e Python Fundamental
def ensinar_matematica_python_fundamental():
    print("\nMatemática e Python Fundamental!")
    print("Neste tópico, vamos aprender conceitos básicos de Python aplicados à matemática, como variáveis e operadores.")

    print("\n1. O que são variáveis em Python?")
    print("Uma variável é um local na memória do computador onde você pode armazenar um valor. Em Python, você pode criar uma variável simplesmente atribuindo um valor a um nome.")
    print("Exemplo:")
    print("   a = 5  # A variável 'a' armazena o valor 5")

    print("\n2. Tipos de dados em Python")
    print("Em Python, temos tipos de dados como inteiros (int), números de ponto flutuante (float), e strings (str).")
    print("Exemplo:")
    print("   x = 10  # int")
    print("   y = 3.14  # float")
    print("   nome = 'Maria'  # string")

    print("\n3. Operadores Matemáticos")
    print("Python oferece operadores para realizar operações matemáticas como soma, subtração, multiplicação e divisão.")
    print("Exemplo:")
    print("   soma = 5 + 3  # soma é 8")
    print("   subtracao = 10 - 3  # subtração é 7")
    print("   multiplicacao = 4 * 2  # multiplicação é 8")
    print("   divisao = 9 / 3  # divisão é 3.0")
    print("   modulo = 7 % 3  # módulo é 1 (resto da divisão)")

    print("\n4. Utilizando variáveis em cálculos")
    print("Você pode usar variáveis para realizar cálculos. Por exemplo, se você quiser calcular a área de um círculo (A = πr²), você pode fazer o seguinte:")
    print("   import math  # Importando o módulo math para acessar o valor de pi")
    print("   raio = 5")
    print("   area = math.pi * raio ** 2  # área do círculo")
    print(f"   A área do círculo com raio 5 é {'area':.2f}")
    

# Retorna ao menu principal após terminar
    input("\nPressione Enter para voltar ao menu principal.")
    menu()
    
    
    

# Função para simular a análise de desempenho dos usuários
def analisar_desempenho(usuarios):
    # Calcula a média, mediana e moda dos tempos de uso dos usuários
    idade_dos_usuarios = [usuario['idade'] for usuario in usuarios]
    
    # Explicação sobre o que são média, mediana e moda
    print("\nExplicações sobre os conceitos estatísticos:")
    print("1. Média: A média é a soma de todos os valores dividida pelo número de elementos. Em outras palavras, é a média aritmética.")
    print('Exemplo: Se tivermos idades de 25, 30, 35, a média será (25 + 30 + 35) / 3 = 30.')
    
    print('Exemplo: Se tivermos idades de 25, 30, 35, a mediana será 30, pois é o valor do meio. Mas, se tivermos 25, 30, 35, 40, a mediana será a média de 30 e 35, ou seja, (30 + 35) / 2 = 32.5.')
    print("2. Mediana: A mediana é o valor que fica no meio de um conjunto de dados ordenados. Se houver um número ímpar de dados, a mediana é o valor central.")
    
    print("3. Moda: A moda é o valor que mais se repete em um conjunto de dados. Se não houver repetição de valores, diz-se que não há moda.")
    print('Exemplo: Se tivermos idades de 25, 30, 30, 35, a moda será 30, pois é o número que mais se repete.')
    
    media = statistics.mean(idade_dos_usuarios)
    mediana = statistics.median(idade_dos_usuarios)
    try:
        moda = statistics.mode(idade_dos_usuarios)
    except statistics.StatisticsError:
        moda = "Sem moda"

    # Exibindo os resultados
    print(f"\nMédia de idade dos usuários: {media:.2f}")
    print(f"Mediana de idade dos usuários: {mediana:.2f}")
    print(f"Moda de idade dos usuários: {moda}")
    
    # Espera o usuário pressionar Enter para voltar ao menu
    input("\nPressione Enter para voltar ao menu principal.")
    menu()  # Retorna ao menu principal




# Função para verificar conformidade com LGPD //   Verifica se o consentimento do usuario   
def validar_lgpd(usuario):

    if usuario['consentimento'] == 'sim':
        return True, "O usuário está em conformidade com a LGPD."
    else:
        return False, "O usuário não está em conformidade com a LGPD."
    
    
# Solicita ao usuário pressionar Enter para voltar ao menu
input("\nPressione Enter para voltar ao menu principal.")
menu()






# Função para otimizar o consumo de energia
def otimizar_consumo_energia():
   
    print("\n--- Otimização de Consumo de Energia ---")
    print("Aqui, vamos aprender como otimizar o consumo de energia elétrica dos equipamentos.")
    print("Dicas para otimizar o consumo de energia:")
    print("1. Desligue os computadores quando não estiverem em uso.")
    print("2. Utilize modos de economia de energia quando disponíveis.")
    print("3. Desconecte dispositivos periféricos desnecessários.")
    print("4. Evite deixar os computadores em modo de espera por longos períodos.")
    
    # Pergunta se o usuário quer sair ou continuar
    sair = input("Você deseja sair dessa seção? (sim/não): ").lower()
    
    if sair == 'sim':
        print("Saindo da otimização de consumo de energia...")
        return  # Sai da função e retorna ao ao menu principal
    
    # Se o usuário não quiser sair, o código continua a execução normalmente
    print("Continuando com a otimização...")
    time.sleep(2)  # Simula a otimização do consumo de energia
    






# Função principal que coordena as ações do sistema //que executa o programa
def main():
    usuarios = carregar_dados()   # Carrega os dados dos usuários a partir do arquivo JSON
    
    
    # Se não houver usuários registrados, forçar o registro
    if not usuarios:
        print("Nenhum usuário registrado. Você precisa se registrar primeiro.")
        usuario = registrar_usuario()
        usuarios.append(usuario)
        salvar_dados(usuarios)  # Salva os dados do novo usuário
    
    
    
    while True:
        menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            usuario = registrar_usuario()
            usuarios.append(usuario)
            salvar_dados(usuarios)
            
        elif escolha == '2':
            ensinar_informatica_basica()
            
        elif escolha == '3':
            media, mediana, moda = analisar_desempenho(usuarios)
            print(f"\nMédia de tempo de uso: {media:.2f} horas")
            print(f"Mediana de tempo de uso: {mediana:.2f} horas")
            print(f"Moda de tempo de uso: {moda}")
            
        elif escolha == '4':
            for usuario in usuarios:
                valido, mensagem = validar_lgpd(usuario)
                print(f"\nUsuário: {usuario['nome']}")
                print(f"Status da conformidade com a LGPD: {mensagem}")
                
        elif escolha == '5':
            otimizar_consumo_energia()
            
        elif escolha == '6':
            print("Saindo do sistema. Até logo!")
            break  # Sai do loop e encerra o programa
        
        else:
            print("Opção inválida! Tente novamente.")
            
            
            
    # Chamando a função principal para iniciar o programa
if __name__ == "__main__":
    main()        

