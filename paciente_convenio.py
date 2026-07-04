# Subclasse Paciente Convênio

# Todos os tributos do paciente   
# + Nome do Convênio
# + Número da Carteirinha

# Método 1: Adicionar taxa caso atendimento seja de urgencia (se houver)
# Metodo 2: Aplicar desconto sobre o valor (se houver) 
# Método 3: Mostrar os dados na tela 

from paciente import Paciente


# Passo 1: Preencher a ficha do Paciente Convênio (método constructor) + atributos adicionais: 

class PacienteConvenio(Paciente):
    def __init__(self, nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario, nome_convenio, numero_carteirinha):
        super().__init__(nome, data_nascimento, cpf, telefone, tipo_sanguineo, numero_prontuario)
        self.nome_convenio = nome_convenio
        self.numero_carteirinha = numero_carteirinha        
        

# Passo 2: Registrar autorização do procedimnento pelo plano (se houver) e calcular quanto o paciente vai pagar pelo atendimento:
    def registrar_autorizacao(self, procedimento, valor_glosa):
        print(f"✅ Procedimento [{procedimento}] AUTORIZADO pelo convênio {self.nome_convenio}.")
        # Se houver algum valor de glosa (rejeitado), a gente avisa na tela
        if valor_glosa > 0:
            print(f"⚠️ Atenção: Valor de glosa identificado: R${valor_glosa}")



# Passo 3: Mostrar os dados na tela:

    def exibir_informacoes(self, detalhado):    
        super().exibir_informacoes(detalhado)
        print(f"Convênio: {self.nome_convenio}")
        print(f"Nº Carteirinha: {self.numero_carteirinha}")


