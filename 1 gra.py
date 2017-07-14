#Jakis idle game
#idle game ktory ma dawac przyjemnosc z grania

from appJar import gui
import random
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
        lines3=lines[10:16]
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
        haslo=register1.getEntry("Hasło")
        rephaslo=register1.getEntry("Powtórz hasło")

##########################################################################
# HASLO I LOGIN + LOSUJ
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
            register1.stop()
        elif str(haslo)!=str(rephaslo):
            register1.errorBox('Error','Popraw haslo')
##########################################################################           

#WYJSCIE Z REJESTRACJI

    elif btn=="Wyjdz":
        register1.stop()

##########################################################################
# Save register do pliku TXT

    login1=str(login)
    loginreg=(login1+".txt")
    filepath=("C:/Python34/Projekty CTO/Projekty 05.07.17/appJar/Idle games/1 gra/Gracze/"+str(loginreg))
    f=open(filepath,'w')   
    f.write(str(login)+'\n')
    f.write(str(rephaslo)+'\n\n')
    f.write("Imie: "+imie+'\n')
    f.write("Nazwisko: "+nazw+'\n')
    f.write("Data urodzenia: "+data+'\n')
    f.close()

###########################################################################

entry1=gui("==Zaloguj==")
entry1.addLabelEntry("Login",0,0,0)
entry1.addSecretLabelEntry("Hasło",0,1,0)
entry1.addButtons(["Zaloguj","Rejestruj","Wyjdz"],przyciski1,1,1,0)


register1=gui("REJESTRACJA")
imie=register1.addLabelEntry("Imie",0,0,0)
nazw=register1.addLabelEntry("Nazwisko",1,0,0)
data=register1.addLabelEntry("Data urodzenia",2,0,0)

register1.addSecretLabelEntry("Hasło",3,0,0)
register1.addSecretLabelEntry("Powtórz hasło",4,0,0)
register1.addButtons(["Rejestracja","Wyjdz"],przyciski2)


entry1.go()

# ladowanie loginu do wpisania do gry

filepath=("C:/Python34/Projekty CTO/Projekty 05.07.17/appJar/Idle games/1 gra/Gracze/"+str(ent_log)+'.txt')
lines=[]
with open(filepath,'r') as fp:
     for line in fp:
        line=line.rstrip()
        lines+=line
        lines1=''.join(map(str,lines))
#LOGIN
        lines2=lines[0:10]
        lines2=''.join(map(str,lines2))

    

def przyciski3(btn):
    if btn=="Kop":
        print ('save')
        
        win.addImage('im1','kilof1.gif')
    elif btn=="Save":
        print ('save')
    elif btn=="Wyjscie":
        
        win.stop()

win=gui("IDLE Game")
win.setResizable(True)

win.addLabel('l1','kurwa')
win.addButtons(['Kop','Save','Wyjscie'],przyciski3)
win.go()
###########################################################################

#pygame.init()
#screen=pygame.display.set_mode((640,480))
#fps_clock = pygame.time.Clock()


