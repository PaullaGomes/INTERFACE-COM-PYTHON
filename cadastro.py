from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
Layout = [
  [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
  [ sg.Text ('Senha'), sg.Input(key= 'senha', password_char='*', size=(20, 1))],
  [sg.Checkbox('Salvar o login')],
  [sg.Button('Entrar')]
]
#Janelas
janela = sg.Window('Tela de Login', Layout)
#Ler os eventos
while True:
 eventos, valores =  janela.read()
 if eventos == sg.WINDOW_CLOSED:
  break
  if eventos == 'Entrar':
   if valores['usuario'] == 'paulla' and valores['senha'] == '123456':
    print ('Bem-vindo a Tela que a Paulla acabou de criar')
