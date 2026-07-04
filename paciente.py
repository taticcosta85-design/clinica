# Classe Mãe

# nome
# data_nascimento
# cpf
# telefone
# tipo_sanguineo
# numero_prontuario

#Passo 1:  Preencher a ficha do paciente (método constructor)

class Paciente:
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario): 
        self.nome = nome    
        self.data_nascimento = data_nascimento
        self._cpf = cpf #Atributo privado (recebe_ antes do atributo)
        self.telefone = telefone
        self.tipo_sanguineo = tipo_sanguineo
        self.numero_prontuario = numero_prontuario

#Passo 2: Mostrar os dados na tela: 

    def exibir_informacoes(self, detalhado):
        if detalhado:
# Se for True, mostra TUDO (os 6 dados)
            print("--- FICHA DETALHADA DO PACIENTE ---")
            print(f"Nome: {self.nome}")
            print(f"Nascimento: {self.data_nascimento}")
            print(f"CPF: {self._cpf}")
            print(f"Telefone: {self.telefone}")
            print(f"Tipo Sanguíneo: {self.tipo_sanguineo}")
            print(f"Nº Prontuário: {self.numero_prontuario}")
            print("-----------------------------------")
        else:
# Se for False, exibe apenas Nome, Número Prontuário e Tipo Sanguíneo
            print(f"📋 Paciente: {self.nome} | Prontuário: {self.numero_prontuario} | Sangue: {self.tipo_sanguineo}")

# Passo 3: Registrar atendimento do paciente

    def registrar_atendimento(self, tipo, custo):
        print(f"🏥 Atendimento [{tipo}] registrado para {self.nome}. Custo: R${custo}")            


