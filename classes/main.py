from datetime import date

# Importando as classes de seus respectivos arquivos
from clinica import Clinica
from paciente import Paciente
from profissional_saude import ProfissionalSaude
from procedimento import Procedimento
from atendimento import Atendimento
from atendimento import TipoAtendimento

# Como Pagamento é abstrata, será necessário importar uma das classes concretas para simular um pagamento. Vamos usar o PagamentoPix como exemplo.
from pagamento import PagamentoPix #ainda não implementado, mas vamos deixar aqui para quando for implementar


def main():
    print("=== INICIANDO SIMULAÇÃO DO SISTEMA CLÍNICO ===")

    # 1. Criando a Clínica
    print("\n[1] Cadastrando Clínica...")
    clinica_central = Clinica(
        nome="Clínica Saúde Total",
        cidade="São Paulo",
        descricao="Clínica Geral e Especialidades",
        horarioAbertura="08:00",
        horarioFechamento="18:00"
    )
    print(f"-> Clínica '{clinica_central.nome}' criada com sucesso.")

    # 2. Criando o Paciente
    print("\n[2] Cadastrando Paciente...")
    paciente_joao = Paciente(
        nome="João Silva",
        celular="11999998888",
        cpf="123.456.789-00",
        dataNascimento=date(1995, 5, 15)
    )
    status_maioridade = "Sim" if paciente_joao.maiorDeIdade() else "Não"
    print(f"-> Paciente '{paciente_joao.nome}' cadastrado. Maior de idade? {status_maioridade}")

    # 3. Criando o Tipo de Atendimento e o Profissional de Saúde
    print("\n[3] Cadastrando Infraestrutura de Atendimento...")
    tipo_consulta = TipoAtendimento(descricao="Consulta Eletiva")
    
    medico = ProfissionalSaude(
        nome="Dra. Ana Paula",
        celular="11988887777",
        cpf="987.654.321-11",
        especialidade="Cardiologia",
        registroProfissional="CRM-SP 12345"
    )
    print(f"-> Tipo: {tipo_consulta.descricao} | Profissional: {medico.nome} ({medico.especialidade})")

    # 4. Criando o Atendimento Principal (O "Model" central)
    print("\n[4] Iniciando um Novo Atendimento...")
    atendimento = Atendimento(
        data=date.today(),
        horarioInicio="14:00",
        horarioFim="14:45",
        valor=350.00,
        paciente=paciente_joao,
        clinica=clinica_central,
        tipoAtendimento=tipo_consulta
    )

    # 5. Criando e adicionando um Procedimento (Composição)
    print("\n[5] Vinculando Procedimento ao Atendimento...")
    eletro = Procedimento(
        descricao="Eletrocardiograma",
        custo=150.00,
        profissional=medico
    )
    atendimento.adicionar_procedimento(eletro)
    print(f"-> Procedimento '{eletro.descricao}' adicionado ao atendimento.")


    # 6. Simulando um Pagamento via PIX (Composição)
    print("\n[6] Processando Pagamento...")
    pagamento_pix = PagamentoPix(
        data=date.today(),
        valorPago=200.00,
        cpfPagador=paciente_joao.cpf
    )
    atendimento.adicionar_pagamento(pagamento_pix)
    print(f"-> Pagamento de R$ {pagamento_pix.valorPago:.2f} registrado via PIX.")

    # =========================================================================
    # RELATÓRIO FINAL 
    # =========================================================================
    print("\n" + "="*50)
    print("RESUMO DO ATENDIMENTO GERADO COM SUCESSO:")
    print(f"  Paciente: {atendimento.paciente.nome}")
    print(f"  Clínica: {atendimento.clinica.nome}")
    print(f"  Tipo: {atendimento.tipoAtendimento.descricao}")
    print(f"  Procedimentos Realizados:")
    for proc in atendimento.procedimentos:
        print(f"    - {proc.descricao} (Realizado por: {proc.profissional.nome})")
    print(f"  Valor Total do Atendimento: R$ {atendimento.valor:.2f}")
    print(f"  Total Pago até o momento: R$ {sum(p.valorPago for p in atendimento.pagamentos):.2f}")
    print("="*50)

if __name__ == "__main__":
    main() 