from controller.controller import ControleCriacao

while True:
    opcao = Menu.menu()
    if opcao == '0':
        break
    else:
        ControleCriacao.opcoesMenu(opcao)
