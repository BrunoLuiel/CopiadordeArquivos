from PySimpleGUI import PySimpleGUI as sg
from LeitordeArquvios import copiador as cop

sg.theme('Light Grey')
layout = [
    [sg.Text('Pasta de origem'), sg.Input(key='orig')],
    [sg.Text('Pasta de destino'), sg.Input(key='dest')],
    [sg.Text('Extensão (opcional)'), sg.Input(key='ext', size=(4,1)), sg.Text('.xml .pdf e etc')],
    [sg.Button('Copiar'),sg.Button('Cancelar'), sg.Text('Desenvolvido por Bruno Luiel')]
]

janela = sg.Window('Copiador de Arquivos', layout)

sg.Popup('Para quem busca copiar arquivos de várias subpastas de um diretório, este é o programa ideal!!! \n \n Passo1: Você vai no seu computador copiar o endereço da pasta onde estão todas as subpastas. \n Passo2: Colar o diretório do Passo 1 no campo "Pasta de origem". \n Passo3: Fazer o mesmo com a pasta de destino dos arquivos. \n \n Após a execução, na pasta de destino, estarão todos os arquivos :). \n \n Observação: Este programa não copia pastas!')
while True:
    evento, valores = janela.read()#eventos é click e valores é os dados inseridos
    if evento == sg.WIN_CLOSED:
        break
    if evento == 'Cancelar':
        break
    if evento == 'Copiar':
        x = cop(valores['orig'], valores['dest'], valores['ext'])                       
        sg.Popup(f'Copiado {x} arquivos! \n \n Atividade executada com sucesso!')
        # try:
        #     if cop(valores['orig'], valores['dest'], valores['ext']) == False:
        #         sg.Popup('O diretório não existe')
        #     else:
        #         x= None
        #         cop(valores['orig'], valores['dest'], valores['ext'])                       
        #         sg.Popup(f'Copiado {x} arquivos! \n \n Atividade executada com sucesso!')
        # except:
        #     sg.Popup('Erro na execução do comando')


janela.close()