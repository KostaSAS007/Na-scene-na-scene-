
def noteiktDiapazonu(d1,d2,sk): 
    rezultata= "Skaitlis nav dapazona" 
    if d1>=sk<=d2: 
      rezultats= "Skaitlis ir diapazona"
    return rezultats 
  
  
d1 = int(input("ievadi diapazona sakumu:"))  
d2 = int(input("ievadi diapazona sakumu:")) 
sk = int(input("ievadi skaitli:"))  
rez = noteiktDiapazonu(d1,d2,sk) 
print(rez)