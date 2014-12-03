# -*- coding: iso-8859-1 -*-
''' Formatador de Pendrive para Slackware

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
from ttk import Combobox
import tkMessageBox
import subprocess
from usbinfo import USBdrv

class main:
    def __init__(self,master):

#-----------------------Interface gr�fica----------------------------------------------------

        Label(master,text='Escolha o dispositivo(CUIDADO)',
              font=('Courier','14'),fg='red').place(relx=0.02,rely=0.02)
        self.device = Combobox(master,font=('Ariel','15'))
        self.device.place(relx=0.04,rely=0.10,relwidth=0.90)

        Label(master,text='Escolha o Sistema de arquivos',
              font=('Courier','14')).place(relx=0.02,rely=0.22)
        self.sis = Combobox(master,font=('Ariel','15'))
        self.sis.place(relx=0.04,rely=0.30,relwidth=0.90)

        self.botao_formatar = Button(master,text='Formatar',font=('Courier','25'),
                                     command=self.formatar)
        self.botao_formatar.place(relx=0.20,rely=0.70)

        self.botao_refresh = Button(master,text='Atualizar',font=('Courier','25'),
                                     command=self.devices)
        self.botao_refresh.place(relx=0.18,rely=0.85)
               
        self.devices()
        self.sis_file()
#----------------------Fun��es---------------------------------------------------------------        
    def devices(self):        
        #devices =  subprocess.check_output(['cat','/proc/partitions']).split('\n')
        self.device['values'] = USBdrv().mounted_drvs

    def sis_file(self):
        sis_file = ['ext2','vfat','ntfs','reiserfs']
        self.sis['values'] = sis_file

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
        
                         
root = Tk()
root.title("SlkFormat")
root.geometry("350x450")
root.resizable(width=FALSE, height=FALSE)
main(root)
root.mainloop()
