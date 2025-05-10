#instalar  PRIMEIRO  (usando o terminal)  pip install art
# roda o trecho de codigo animar_cobra()

from art import *  # faz a animação da escrita ONCODE
import time  # Trabalha com tempo.
import json  # Manipula arquivos JSON.
import os  # Interage com o sistema operacional.
import hashlib  # Criptografa dados.



# Função para limpar a tela (dependendo do sistema operacional)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir a animação da escrita "ONCode"
def animar_projeto():
    limpar_tela()
    print(text2art("ONCode ", font="block"))  # Exibe "ONCode" com a arte    
    time.sleep(4)  # Exibe por 4 segundos
    limpar_tela()
    
    

# # Boas-vindas e descrição do projeto
def exibir_boas_vindas():
    print("\n=== Bem-vindo galera ! Você esta no  ONCode! ===")
    print("ONCode é uma plataforma educacional em Python, desenvolvida para ensinar lógica de programação básica, segurança digital e operações matemáticas de forma interativa a crianças e pré-adolescentes.\n")




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





# Coleta de informações do usuário (nome e idade)
def cadastrar_usuario():
    print("Primeiro, vamos conhecer você melhor!")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    # Solicita consentimento de acordo com a idade
    if idade < 12:
        print("\nVocê tem menos de 12 anos. Para continuar, precisamos do consentimento de seus pais ou responsável.")
        consent = input("Seu responsável deu consentimento? (sim/não): ").strip().lower()
        if consent != "sim":
            print("Sem consentimento, não podemos prosseguir com o cadastro. Encerrando.")
            return None  # Encerra sem salvar
    else:
        print("\nVocê tem 12 anos ou mais. Por favor, leia os termos de uso: De acordo com a Lei Geral de Proteção de Dados Pessoais (LGPD),precisamos do seu consentimento para processar seus dados.")
        print('\nSe você concordar, seus dados serão utilizados exclusivamente para melhorar a experiência na plataforma e para análise de desempenho.')
        print('\nSe não concordar, seus dados não serão armazenados e não poderemos oferecer os serviços completos da plataforma.')
        consent = input("\nVocê aceita os termos e condições? (sim/não): ").strip().lower()
      
                
        if consent != "sim":
            print("Sem consentimento, não podemos prosseguir com o cadastro. Encerrando.")
            return None  # Encerra sem salvar
        
         # Se o usuário tem mais de 12 anos, vamos coletar o e-mail
        email = input("Digite seu e-mail: ").strip()

    # Se chegou aqui, há consentimento válido
    usuario = {"nome": nome, "idade": idade}    
    if idade >= 12:
        usuario["email"] = email  # Adiciona o e-mail ao usuário se tiver mais de 12 anos  
        usuario['email_criptografado'] = criptografar_dados(usuario['email'])     # Criptografando email por motivos de segurança
    
    
    # Salvar em JSON
    usuarios = carregar_dados()
    usuarios.append(usuario)
    salvar_dados(usuarios)
    

    print(f"\nCadastro realizado com sucesso! Bem-vindo(a), {nome}! Vamos começar: \n")
    time.sleep(4)  # Exibe por 4 segundos 
    return usuario





# Menu principal adaptado
def exibir_menu():
    print("MENU PRINCIPAL:")
    print("1. Informática Básica")    
    print("2. Programação em Python")  
    print("3. Matemática e Python ")    
    print("4. Estatísticas de Desempenho")      
    print("5. Dicas de Segurança Digital")
    print("6. Dicas sobre Sustentabilidade Digital")
    print("7. Sair")






# Funções de exemplo para cada opção
def informatica_basica():
    print("\n-- Módulo: Informática Básica --")
    print("Aqui, vamos aprender o básico sobre o uso de computadores, infraestrutura, TICs e boas práticas de segurança digital.")
    time.sleep(4)
    
    print("\nEscolha um tópico:")
    print("1. TICs ")
    print("2. infraestrutura básica de TI?")
    print("3. Sistema operacional?")
    print("4. Programas de edição de texto e planilhas?")    
    time.sleep(4)
        
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
    else:
        print("\nOpção inválida! Tente novamente.")
        
#    # Retorna ao menu principal após terminar
    input("\nPressione Enter para voltar ao menu principal.")
    time.sleep(4)  # Exibe por 4 segundos 




def python_basico():
    print("\n-- Módulo: Programação em Python --")
    print("Aprenda a escrever seus primeiros comandos em Python!\n")
    time.sleep(4)
    
    print("\n1. O que são variáveis em Python?")
    print("Uma variável é um local na memória do computador onde você pode armazenar um valor. Em Python, você pode criar uma variável simplesmente atribuindo um valor a um nome.")
    print("Exemplo:")
    print("   a = 5  # A variável 'a' armazena o valor 5")
    time.sleep(5)

    print("\n2. Tipos de dados em Python")
    print("Em Python, temos tipos de dados como inteiros (int), números de ponto flutuante (float), e strings (str).")
    print("Exemplo:")
    print("   x = 10  # int")
    print("   y = 3.14  # float")
    print("   nome = 'Maria'  # string")
    time.sleep(5)

    print("\n3. Operadores Matemáticos")
    print("Python oferece operadores para realizar operações matemáticas como soma, subtração, multiplicação e divisão.")
    print("Exemplo:")
    print("   soma = 5 + 3  # soma é 8")
    print("   subtracao = 10 - 3  # subtração é 7")
    print("   multiplicacao = 4 * 2  # multiplicação é 8")
    print("   divisao = 9 / 3  # divisão é 3.0")
    print("   modulo = 7 % 3  # módulo é 1 (resto da divisão)")
    time.sleep(5)

    print("\n4. Utilizando variáveis em cálculos")
    print("Você pode usar variáveis para realizar cálculos. Por exemplo, se você quiser calcular a área de um círculo (A = πr²), você pode fazer o seguinte:")
    print("   import math  # Importando o módulo math para acessar o valor de pi")
    print("   raio = 5")
    print("   area = math.pi * raio ** 2  # área do círculo")
    time.sleep(5)
    
    
    #    # Retorna ao menu principal após terminar
    input("\nPressione Enter para voltar ao menu principal.")
    time.sleep(4)  # Exibe por 4 segundos 






def matematicas(usuario):
    # Permite apenas conteúdos compatíveis com a idade
    if usuario['idade'] < 12 or "email" not in usuario:
        print("\n::::::Este módulo é para maiores de 12 anos. Você ainda não tem essa idade!::::.\n")
        return
    
    print("\n-- Módulo: Matemática --")
    print("Neste tópico, vamos aprender conceitos básicos de media, moda e mediana. ")
    print('Muito utilizado na programação afim de se obter dados sobre diversos assuntos para depois tomar uma decisão sobre o que fazer com esses numeros obtidos')
    time.sleep(4)
    
    print("\n1. Média aritmética = É a soma de todos os valores dividida pelo número de elementos. Ex: 1,2,2,2,3 = 10/5 = 2 ")
    print("\n2. Moda = É o valor que mais se repete em um conjunto de dados. Ex: 2")
    print("\n3. Mediana= É o valor que esta no meio, no centro de um conjunto de dados ordenados. Ex: 2 ")
    escolha = input("\nEscolha o que vamos fazer, digite opção 1,2 ou 3: ")
    if escolha == '1':
        calcular_media()
    elif escolha == '2':
        calcular_moda()
    elif escolha == '3':
        calcular_mediana()
    else:
        print("Opção inválida.\n")
        


# Funções matemáticas
def calcular_media():
    print("\n-- Cálculo de Média --")
    nums = list(map(float, input("Digite números separados por espaço: ").split()))
    media = sum(nums)/len(nums)
    print(f"A média é: {media}\n")


def calcular_moda():
    print("\n-- Cálculo de Moda --")
    nums = list(map(int, input("Digite números separados por espaço: ").split()))
    frequencia = {n: nums.count(n) for n in nums}
    moda = [k for k, v in frequencia.items() if v == max(frequencia.values())]
    print(f"A(s) moda(s) é/são: {moda}\n")


def calcular_mediana():
    print("\n-- Cálculo de Mediana --")
    nums = sorted(map(float, input("Digite números separados por espaço: ").split()))
    n = len(nums)
    meio = n // 2
    if n % 2 == 0:
        mediana = (nums[meio - 1] + nums[meio]) / 2
    else:
        mediana = nums[meio]
    print(f"A mediana é: {mediana}\n")


 #    # Retorna ao menu principal após terminar
    input("\nPressione Enter para voltar ao menu principal.")
    time.sleep(4)  # Exibe por 4 segundos 






def estatisticas():
    print("\n-- Módulo: Estatísticas de Desempenho --")
    print("Acompanhe seu progresso e veja como você está se saindo!\n")
    
    print( 'EM BREVE, novos dados sobre seu desempenho, como :')
    print('\nTempo de estudo na plataforma')
    print('\nAcessos - Presença nas Aulas')
    print('\nSuas notas')
    print('\nFeedBacks')
    print('\ne muito mais!')
    time.sleep(5)
    
       # Retorna ao menu principal após terminar
    input("\nPressione Enter para voltar ao menu principal.")
    time.sleep(4)  # Exibe por 4 segundos

    
    

def seguranca_digital():
    print("\n-- Módulo: Dicas de Segurança Digital --")
    print("Conheça boas práticas para navegar seguro na internet.\n")
    time.sleep(4)
    
    print("1. Importância de senhas seguras e como criar senhas fortes?")
    print("Use uma combinação de letras, números e caracteres especiais, e evite palavras comuns.")
    print("Exemplo: 'Senha123!@'")
    time.sleep(5)
    
    print("\n2.Phishing é uma tentativa de obter informações sensíveis, como senhas, se passando por um site confiável.")
    print("Evite clicar em links desconhecidos ou fornecer informações pessoais sem verificar a autenticidade do site.")
    time.sleep(5)
    
    print("\n3.Realizar backup regularmente é importante para proteger seus dados contra perdas acidentais.")
    time.sleep(5)
    
    print("\n4.Cuidado com links suspeitos.")
    time.sleep(5)
    
        
    #    # Retorna ao menu principal após terminar
    input("\nPressione Enter para voltar ao menu principal.")
    time.sleep(4)  # Exibe por 4 segundos 
    
    
        
    
    
def otimizar_consumo_energia():   
    print("\n--- Otimização de Consumo de Energia ---")
    print("Aqui, vamos aprender como otimizar o consumo de energia elétrica dos equipamentos.")
    time.sleep(4)
    print("Dicas para otimizar o consumo de energia:")
    print("1. Desligue os computadores quando não estiverem em uso.")
    print("2. Utilize modos de economia de energia quando disponíveis.")
    print("3. Desconecte dispositivos periféricos desnecessários.")
    print("4. Evite deixar os computadores em modo de espera por longos períodos.")
    print('\nLixo Eletronico é todo tipo de aparelho que vai na energia ou usa pilha e bateria. Por isso, ficou velho, procure pontos de coleta e descarte de forma correta')
    time.sleep(5)
    
    #    # Retorna ao menu principal após terminar
    input("\nPressione Enter para voltar ao menu principal.")
    time.sleep(4)  # Exibe por 4 segundos 
    






# Loop principal sequencia das ocorrencias: animação, cadastro e menu principal
def main():
    animar_projeto()
    exibir_boas_vindas()
    usuario = cadastrar_usuario()
    if not usuario:
        return  # encerra, pois não houve consentimento
    

    # idade = usuario["idade"]
    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            informatica_basica()            
        elif opcao == '2':
            python_basico()
        elif opcao == '3':
            matematicas(usuario)
        elif opcao == '4':
            estatisticas()
        elif opcao == '5':
            seguranca_digital()
        elif opcao == '6':
            otimizar_consumo_energia()            
        elif opcao == '7':
            print("Obrigado por usar o ONCode! Até a próxima aula.")
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Tente novamente.\n")




# Roda a aplicação - Chamando a função principal para iniciar o programa
if __name__ == "__main__":
    main()    