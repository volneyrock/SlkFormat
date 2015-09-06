# -*- coding: iso-8859-1 -*-
''' SlkFormat

Copyright 2014 Volney Casas volneyrock@gmail.com
          

# Este � um software livre; voc� pode redistribu�-lo e/ou
#
# modifica-lo dentro dos termos da Licen�a P�blica Geral GNU como
#
# publicada pela Funda��o do Software Livre (FSF); na vers�o 2 da
#
# Licen�a, ou (na sua opini�o) qualquer vers�o.
#
#
#
# Este programa � distribu�do na esperan�a de que possa ser �til,
#
# mas SEM NENHUMA GARANTIA; sem uma garantia impl�cita de ADEQUA��O a qualquer
#
# MERCADO ou APLICA��O EM PARTICULAR. Veja a
#
# Licen�a P�blica Geral GNU para maiores detalhes.
#
#
#
# Voc� deve ter recebido uma c�pia da Licen�a P�blica Geral GNU
#
# junto com este programa, se n�o, escreva para a Funda��o do Software
#
# Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#
# Ou acesse o endere�o https://www.gnu.org/licenses/gpl.html
#'''


from Tkinter import *
from ttk import Combobox, Progressbar
import tkMessageBox
import subprocess
from modules.usbinfo import USBdrv
#from threading import Thread
from modules.config import *

class main:
    def __init__(self, master):

#-----------------------Interface gr�fica----------------------------------------------------
        self.frame1 = Frame(master, bg = COR_FUNDO)
        self.frame1.place(relheight = 1.0, relwidth = 1.0)

        self.botao_refresh = Button(self.frame1, text = 'Atualizar dispositivos', font = ('Courier','10'),
                                     fg = 'black', bg = COR_BOTAO_2, borderwidth = 3,
                                     command = self.devices)
        self.botao_refresh.place(relx = 0.202, rely = 0.02, relwidth = 0.54)
        
        Label(self.frame1, text = 'Escolha o dispositivo(CUIDADO)',
              font=('Courier','14'), fg = 'red', bg = COR_FUNDO).place(relx = 0.02, rely = 0.12)
        self.device = Combobox(self.frame1, font = ('Ariel','15'))
        self.device.place(relx = 0.04, rely = 0.20, relwidth = 0.90)

        Label(self.frame1, text='Escolha o Sistema de arquivos',
              font=('Courier','14'), fg = 'white', bg = COR_FUNDO).place(relx = 0.02, rely = 0.32)
        self.sis = Combobox(self.frame1, font = ('Ariel','15'))
        self.sis.place(relx = 0.04, rely = 0.40, relwidth = 0.90)

        self.botao_formatar = Button(self.frame1, text = 'Formatar', font = ('Courier','25'),
                                     fg = 'black', bg = COR_BOTAO_1, borderwidth = 3,
                                     command = self.formatar)
        self.botao_formatar.bind("<Button-1>", self.mudabotao)
        self.botao_formatar.place(relx = 0.21, rely = 0.82, relwidth = 0.54)

        self.devices()
        self.sis_file()
#----------------------Fun��es---------------------------------------------------------------        
    def devices(self):        
        #devices =  subprocess.check_output(['cat','/proc/partitions']).split('\n')
        self.device['values'] = USBdrv().mounted_drvs

    def sis_file(self):
        sis_file = ['ext2','vfat','ntfs','reiserfs']
        self.sis['values'] = sis_file

    def mudabotao(self,event):
        self.botao_formatar['text'] = 'Espere'

    def formatar(self):
        
        dv = self.device.get()
        st = self.sis.get()

        try:
            subprocess.call(['umount','%s'%dv])
            if st == 'vfat':
                subprocess.call(['mkfs.vfat', '%s' %dv])
                
            elif st == 'ntfs':
                subprocess.call(['mkfs.ntfs', '%s' %dv])

            elif st == 'reiserfs':
                subprocess.call(['mkfs.reiserfs', '%s' %dv])

            else:
                subprocess.call(['mkfs.ext2', '%s' %dv])

            tkMessageBox.showinfo('Aviso!',u'Device formatado com sucesso')
                
        except:
            tkMessageBox.showinfo('Erro!',u'Device ocupado, ou inv�lido, ou voc� n�o � root')
                
        self.devices()
        self.botao_formatar['text'] = 'Formatar'      
        
root = Tk()
root.title("SlkFormat")
root.geometry("350x450")
root.resizable(width=FALSE, height=FALSE)
main(root)
root.mainloop()
