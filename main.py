import  conta
import agencia
import views

agencia_digital = agencia.AgenciaVirtual(cnpj="um cnpj", site="bancodoantonio.com",contato="bancodoantonio@email.com")
agencia_comum = agencia.AgenciaComum(cnpj="dois cnpj", contato="bancodoantonio_agpopular@email.com")
agencia_premium = agencia.AgenciaPremium(cnpj="tres cnpj", contato="bancodoantonio_agpremium@email.com")


acc = views.criar_conta_view(agencia_virtual=agencia_digital,
                               agencia_comum= agencia_comum,
                               agencia_premium= agencia_comum
                               )

menu = 0
while True:
    if menu == 0:
        menu = views.menu_principal(conta=acc)
    elif menu == 1:
        menu = views.menu_saldo(conta=acc)
    elif menu == 2:
        menu = views.menu_deposito(conta=acc, agencia=acc.agencia)
    elif menu == 3:
        menu = views.menu_saque(conta=acc)
    elif menu == 4:
        menu = views.menu_transferencia()
    elif menu == 5:
        menu = views.menu_extrato(acc = acc)
    elif menu == 6:
        menu = views.menu_cartao(acc=acc)
    else:
        menu = str.lower(input("Deseja mesmo sair? (y/n)"))
        if menu == "n":
            continue
        else:
            print("Obrigado por testar o Banco do Antonio, vamos sentir saudades (me indica no trampo)")
            break
