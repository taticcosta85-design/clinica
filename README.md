# Nome do aluno: Tatiana Christina Costa de Oliveira

# Descrição da atividade (retirado do enunciado do professor):
Uma clínica médica precisa de um sistema em Python para gerenciar seus pacientes. Existem dois tipos: pacientes particulares (pagam diretamente pelo atendimento) e pacientes por convênio (atendidos via plano de saúde). Cada tipo tem características e comportamentos distintos, mas compartilham uma base comum.

# Objetivo da atividade:
- Criar um sistema de uma Clínica Médica para gerenciar pacientes
- Existem dois tipos de pacientes com características espécificas: 

# Pacientes Particulares: 
- Pagam diretamente pelo atendimento 

# Pacientes Por Convênio:
- Atendidos via Plano de Saúde

# SuperClasse "Paciente"
É a classe geral. Guarda as características básicas de todo mundo. A Classe de onde os filhos vão herdar todos os atributos.  

# Atributos OBRIGATÓRIOS: 
- Nome
- Data de Nascimento
- CPF (** Deve ser um atributo privado**)
- Telefone
- Tipo Sanguíneo
- Número do Prontuário

# Subclasse "Paciente Particular:  
Herda as características da classe mãe "Paciente" c/ seus métodos e adiciona suas próprias características.

# Atributos OBRIGATÓRIOS:
- Todas as características do "Paciente" 
+
- Forma de Pagamento
- Desconto Fidelidade

# Subclasse "Paciente de Convênio":  
Herda as características da classe mãe "Paciente" c/ seus métodos e adiciona suas próprias características.

# Atributos OBRIGATÓRIOS: 
- Todos os atributos e métodos herdados da classe "Paciente"
+
- Nome do Convenio
- Numero da Carteirinha 

# Passo 1 - Trabalhando na SuperClasse Paciente: 

1.1 - Colocar todos os atributos do Paciente

1.2 - Utilizar o Método Constructor para montar a função: 
Recebe as características (atributos) e deixa salvo nas caixinhas. 


1.3 - Método (1) para Mostrar detalhes na tela
Exibe os dados do paciente na tela. 

Uso do "if" 
Se for True: mostrar a Ficha Completa
Se for False: mostrar os dados de forma resumida

1.4 - Método (2) para Registrar atendimento
Exibe as informações de que o paciente passou por um atendimento com um: 
- tipo
- custo (valor em reais)


# Passo 2 - Trabalhando na SubClasse "Paciente Particular":  

2.1 - Importar os dados da classe "Paciente" 
Importar do arquivo "paciente.py" a classe "Paciente" 

2.2 - Nomear a função mencionando que ela esta herdando dados da classe
"Paciente"

2.3 - Método (1) para construir os atributos do paciente + informações adicionais (método constructor)

2.4 - Método (2) para calcular taxa e desconto

2.5- Método (3) para exibir informações na tela

# Passo 3 - Trabalhando na SubClasse "Paciente de Convenio"

3.1 - Importar os dados da classe "Paciente" 
Importar do arquivo "paciente.py" a classe "Paciente" 

3.2 - Nomear a função mencionando que ela esta herdando dados da classe
"Paciente"

3.3 - Método (1) para construir os atriutos do paciente + informações adicionais (método constructor)

3.4 - Método (2) para registrar autorização de procedimento e calcular quanto vai ser o valor da glosa

3.5- Método (3) para exibir informações na tela 


# Passo 4- Finalizar escrevendo o arquivo "main" que deve conter: 

- os arquivos de onde foram importados os dados
- exemplos dos pacientes 
- informações que você deseja exibir na tela (usando a função "print")
- informar a porta de entrada 

# Exemplo de execução com saída no Terminal:

# Paciente Particular



        




