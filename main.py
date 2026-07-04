#Buscar os arquivos criados das subclasses "Paciente Particular" e "Paciente Convênio"

from paciente_particular import PacienteParticular
from paciente_convenio import PacienteConvenio

print("==============================================")
print("🏥   SISTEMA DA CLÍNICA MÉDICA SAUDE_COM_AMOR   🏥")
print("==============================================\n")


print("--- [ Criando Paciente Particular ] ---")

def main():
    # Criando um paciente particular
    paciente1 = PacienteParticular(
        nome="Bruna Marquezine",
        data_nascimento="04/08/1995",
        cpf="123.456.789-00",
        telefone="(21) 98643-4321",
        tipo_sanguineo="A+",
        numero_prontuario="001",
        forma_pagamento="Cartão de Crédito",
        desconto_fidelidade=0.10
    )

    # Criando um paciente com convênio
    paciente2 = PacienteConvenio(
        nome="Neymar Santos Silva",
        data_nascimento="05/02/1992",
        cpf="987.654.321-00",
        telefone="(21) 91234-5678",
        tipo_sanguineo="O-",
        numero_prontuario="002",
        nome_convenio="Unimed",
        numero_carteirinha="123456789"
    )

    # Exibindo informações detalhadas dos pacientes
    print("\n--- [ Informações do Paciente Particular ] ---")
    print(paciente1.exibir_informacoes(detalhado=True)) 
    print('\n------------------------------------------------')
    print("\n--- [ Informações do Paciente com Convênio ] ---")
    print(paciente2.exibir_informacoes(detalhado=True))

if __name__=="__main__":
    main()


