#Jakis idle game
#idle game ktory ma dawac przyjemnosc z grania
#dostep do tableta
#D:\Python-Projekty\Idle game\Gracze
#dostep CTO
#"C:/Python34/Projekty CTO/Projekty 05.07.17/appJar/Idle games/1 gra/Gracze/

from appJar import gui
import random
import time
#import pygame
      
def przyciski1(btn):

    if btn=="Wyjdz":
        entry1.stop()
    elif btn=="Rejestruj":
        register1.go()
    elif btn=="Zaloguj":
        ent_log=entry1.getEntry("Login")
        global ent_log 
        ent_haslo=entry1.getEntry("Hasło")

### Zaladuj dane

        filepath=("C:/Python34/Projekty CTO/Projekty 05.07.17/appJar/Idle games/1 gra/Gracze/"+str(ent_log)+'.txt')
        #filepath=("D:/Python-Projekty/Idle game/Gracze/"+str(ent_log)+'.txt')
        lines=[]
        with open(filepath,'r') as fp:
            for line in fp:
                line=line.rstrip()
                lines+=line
        lines1=''.join(map(str,lines))
#LOGIN
        lines2=lines[0:10]
        lines2=''.join(map(str,lines2))

#HASLO
        lines3=lines[10:18] #8znakow
        lines3=''.join(map(str,lines3))
        

### warunki na prawidlowosc loginow
        if str(ent_log)==str(lines2) and str(ent_haslo)==str(lines3):
            entry1.stop()

        elif ent_log!=str(lines2) or ent_haslo!=str(lines3):
            entry1.errorBox("Error",'Nieprawidłowy login lub haslo')
        
              
def przyciski2(btn):

##########################################################################
# Rejestracja

    if btn=="Rejestracja":
        imie=register1.getEntry("Imie")
        nazw=register1.getEntry("Nazwisko")
        data=register1.getEntry("Data urodzenia")
        haslo=register1.getEntry("Hasło(8 znakow)")
        rephaslo=register1.getEntry("Powtórz hasło")

        print (len(haslo))
        if len(haslo)>8 and len(haslo)<8:
            register1.errorBox('Error','Popraw dlugosc hasla')
        elif len(haslo)==8:

##########################################################################
# HASLO I LOGIN + LOSUJ + ZAPIS LOGINU I HASLA DO PLIKU .TXT

            imie_list=list(str(imie))
            imie_list1=imie_list[0:3]
            imie_list2=(''.join(imie_list1))

            nazw_list=list(str(nazw))
            nazw_list1=nazw_list[0:3]
            nazw_list2=(''.join(nazw_list1))

            data_list=list(str(data))
            data_list1=data_list[6:10]
            data_list2=(''.join(data_list1))

            tup1=[]
            for x in range(4):
                x=random.randrange(0,9)
                tup1+=[x,]
            tuple1=''.join(map(str,tup1))
            login=imie_list2.lower()+nazw_list2.lower()+tuple1

            if str(haslo)==str(rephaslo):
                register1.infoBox('Powodzenie rejestracji',['Login: '+login,
                                  'Haslo: '+rephaslo])

##########################################################################
# Save register do pliku TXT

                login1=str(login)
                loginreg=(login1+".txt")
                filepath=("C:/Python34/Projekty CTO/Projekty 05.07.17/appJar/Idle games/1 gra/Gracze/"+str(loginreg))
                #filepath=("D:/Python-Projekty/Idle game/Gracze/"+str(loginreg))
                f=open(filepath,'w')   
                f.write(str(login)+'\n')
                f.write(str(rephaslo)+'\n\n')
                f.write("Imie: "+imie+'\n')
                f.write("Nazwisko: "+nazw+'\n')
                f.write("Data urodzenia: "+data+'\n')
                f.close()
                register1.stop()

            elif str(haslo)!=str(rephaslo):
                register1.errorBox('Error','Popraw haslo')
#########################################################################           

#WYJSCIE Z REJESTRACJI

    elif btn=="Wyjdz":
        register1.stop()

   

###########################################################################
# PRZYCISKI DO GUI


entry1=gui("==Zaloguj==")
entry1.addLabelEntry("Login",0,0,0)
entry1.addSecretLabelEntry("Hasło",0,1,0)
entry1.addButtons(["Zaloguj","Rejestruj","Wyjdz"],przyciski1,2,2,0)

register1=gui("REJESTRACJA")
imie=register1.addLabelEntry("Imie",0,0,0)
nazw=register1.addLabelEntry("Nazwisko",1,0,0)
data=register1.addLabelEntry("Data urodzenia",2,0,0)

register1.addSecretLabelEntry("Hasło(8 znakow)",3,0,0)
register1.addSecretLabelEntry("Powtórz hasło",4,0,0)
register1.addButtons(["Rejestracja","Wyjdz"],przyciski2)





##############################################################################################################
# ladowanie loginu do wpisania do gry

#filepath=("C:/Python34/Projekty CTO/Projekty 05.07.17/appJar/Idle games/1 gra/Gracze/"+str(ent_log)+'.txt')
#filepath=("D:/Python-Projekty/Idle game/Gracze/"+str(ent_log)+'.txt')
#lines=[]
#with open(filepath,'r') as fp:
#     for line in fp:
#        line=line.rstrip()
#        lines+=line
#        lines1=''.join(map(str,lines))
#LOGIN
#        lines2=lines[0:10]
#        lines2=''.join(map(str,lines2))


#############################################################################################################
# IDLE 

def przycisk1(btn):

################################################################################
### Licznik klikniec
    if btn=="Kop":

        licznik+=1
        suma=int(licznik)
        print (licznik)
 
        win.setLabel("K1",suma)
        #win.setImage('im1','kilof2.gif')
        #time.sleep((1/15))
        #win.setImage('im1','kilof1.gif')
        global licznik
        global suma
    elif btn!="Kop":
        pass

def przycisk2(btn):
    if btn=="Kup":
        global wartosc
        wartosc=30
        win.setLabel("K2",wartosc)
        global wartosc

def przycisk3(btn):
    global nowe_pieniadze
    if btn=="Pieniadze":
        
        pieniadze=suma
        win.setLabel("S1",pieniadze)
        pieniadze=nowe_pieniadze
        win.disableButton("Pieniadze",przycisk3)
        

global suma
global licznik
global pieniadze
global nowe_pieniadze
licznik=0
win=gui("IDLE Game")
win.setResizable(True)
win.setBg("white")
#win.addImage('im1','kilof1.gif',0,0,0,0)
win.addButton('Kop',przycisk1)
win.addButton('Kup',przycisk2)
win.addButton('Pieniadze',przycisk3)
win.addLabel("K1")
win.addLabel("K2")
win.addLabel("S1")
win.go()
#entry1.go()
###########################################################################

#pygame.init()
#screen=pygame.display.set_mode((640,480))
#fps_clock = pygame.time.Clock()
