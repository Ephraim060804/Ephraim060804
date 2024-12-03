#Début de programme #
  # presentation de l'application #

print("Bienvenue sur l'aide memoire")
while True:
    state=None
    try:
        state=int(input("Desirez vous lire la documentation tapez 1, sinon 2 pour continue : "))
    except ValueError:
        print("ERROR: entrez une valeur numerique ")  
    if state ==1:
        print(""" Aide memoire est mise a votre disposition pour
              vous permettre d'effectuer vos calcule sur la multiplication """)
        break    
    elif state==2:
        print("Entre les information etape apres etape")
        break
    else:
        print("la valeur choisie  n'est pas valide, faite votre choix entre [1, 2] ")
             
        
        
        
while True:
    valeur = 0
    try:
        valeur=int(input("Entrez votre choix de table : "))
    except:
        print ("ERROR: entre une valeur numerique ")
    if valeur < 0:
        print("Entrez une valeur positive ")
    
    else :
        print("  ")
        break
i=0
i +=1    
for i in range(0,11):
    print(f"{i}*{valeur}= {i*valeur}")    

           
               
