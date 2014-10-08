# -*- coding: iso-8859-1 -*-
''' Formatador de Pendrive para Slackware
autor: Volney Casas volneyrock@gmail.com
                6/10/2014

Você pode alterar, usar, ou distribuir este código como quiser,
desde que me mande uma cópia com as alterações por e-mail'''


from Tkinter import *
from ttk import Combobox
import tkMessageBox
import subprocess

class main:
    def __init__(self,master):
        Label(master,text='Escolha o dispositivo(CUIDADO)',
              font=('Courier','14'),fg='red').place(relx=0.02,rely=0.02)
        self.device = Combobox(master,font=('Ariel','15'))
        self.device.place(relx=0.04,rely=0.10,relwidth=0.90)

        self.botao_formatar = Button(master,text='Formatar',font=('Courier','25'),
                                     command=self.formatar)
        self.botao_formatar.place(relx=0.20,rely=0.40)

        self.botao_refresh = Button(master,text='Atualizar',font=('Courier','25'),
                                     command=self.devices)
        self.botao_refresh.place(relx=0.18,rely=0.60)
               
        self.devices()
        
    def devices(self):
        devices =  subprocess.check_output(['cat','/proc/partitions']).split('\n')
        self.device['values'] = devices

    def formatar(self):
        dv = '/dev/'+self.device.get()[25:29]
        try:
            subprocess.call(['umount','%s'%dv])
            subprocess.call(['mkfs.vfat','%s'%dv])
            tkMessageBox.showinfo('Aviso!',u'Device formatado com sucesso')
        except:
            tkMessageBox.showinfo('Erro!',u'Device ocupado, ou inválido, ou você não é root')
        self.devices()
            
        
       
        

                        
root = Tk()
root.title("Formatador")
root.geometry("350x450")
main(root)
root.mainloop()
