import random



def feladat1():
    szam:int=int(input("Adj meg egy páratlan számot!"))
    while(szam%2==0):
        szam:int=int(input("Adj meg egy páratlan számot!"))
    print(szam)

def feladat2():
    i:int=0
    db:int=0
    while (i<7):
        szam:int=int(random.random()*96)+5
        print(szam)
        if(szam%5==0):
            db+=1
    
        i+=1
    print(f"A számok között {db} db 5-tel osztható van!")


def feladat3(text, betu):
    hossz=len(text)
    i:int=0
    while(hossz[i]):
        i+=1
    print(f"A szövegben {betu} db 'a' betű van")

    



    






        
   



    

