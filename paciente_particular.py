# Subclasse Paciente Particular

# Todos os atributos da classe Paciente   
# + Forma de Pagamento
# + Desconto Fidelidade

# Método 1: Preencher a ficha do paciente particular (método constructor) + atributos adicionais:
# Método 2: Calculo de valores sobre o atendimento do paciente particular para 3 situações: a) Atendimento normal, b) Atendimento com urgência, c) Atendimento com desconto de fidelidade  
# Método 3: Exibir informações do paciente particular

from paciente import Paciente


# Passo 1: Preencher a ficha do paciente particular (método constructor) + atributos adicionais: 

class PacienteParticular(Paciente):
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario, forma_pagamento, desconto_fidelidade):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.forma_pagamento = forma_pagamento
        self.desconto_fidelidade = desconto_fidelidade  

# Passo 2: Calcular quanto o paciente vai pagar pelo atendimento:
    def calcular_valor_final(self, valor_consulta, taxa_urgencia):
        # 1. Se for um atendimento de urgência, soma a taxa de urgência
        
        valor_com_urgencia = valor_consulta + taxa_urgencia
        
        # 2. Se tiver desconto baseado na fidelidade
        
        valor_do_desconto = valor_consulta * self.desconto_fidelidade
        
        # 3. Valor com desconto aplicado (se houver) e taxa de urgência (se houver) 
        valor_final = valor_com_urgencia - valor_do_desconto
        
        # Retorna o valor final para ser exibido na tela
        return valor_final


# Passo 3: Mostrar os dados na tela:

    def exibir_informacoes(self, detalhado):    
        super().exibir_informacoes(detalhado)
        print(f"Forma de Pagamento: {self.forma_pagamento}")
        print(f"Desconto Fidelidade: {self.desconto_fidelidade}%")




    