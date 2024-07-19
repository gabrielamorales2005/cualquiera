#diccionario version final 
import json
from difflib import get_close_matches


file_path= '/Users/gabrielamorales/Desktop/VERANO24/PYTHON/Dictionary/13. Application 1 Build an Interactive English Dictionary/data.json.json' #open file and right click in name and copy its path 
with open(file_path, 'r') as file: #this means to open the file above as r format es asi y punto 
    data = json.load(file) #the file will have the name of data 
    print("Type:", type(data))
    
def vocabulary(v): 
    if v in data: 
        v=v.lower() 
        return data[v] 
    elif v.title() in data:
        return data[v.title()]
    elif v.upper() in data: #in case user enters words like USA or NATO
        return data[v.Upper()]
    elif len(get_close_matches(v, data.keys())) > 0: 
        qs= input("Did you mean %s instead? Enter Y as yes; and N for no"% get_close_matches(v,data.keys())[0])
        if qs=="Y":
            return data[get_close_matches(v, data.keys())[0]]
        elif qs=="N":
            return "the word does't exist"
        else:
            return "word asked was not clear!"
    else: 
        return "word not located"

#ACTUAL PROGRAM ITSELF
print("Hello! Welcome to the english dictionary!")


#word= input("Enter word: ") 
word= input("Enter word: ") 
while word != 'salir':
    output= vocabulary(word)
    if type (output) == list: #meaning if the type of the output is a list; multiple definitions 
        for item in output:
            print(item)
    else:
        print(output) 
    word= input("Enter word: ") 

#LIBRERIA MAL ESCRITA DIFFLIB 
# EN FUNCITON:
    #double vv cuando es 1
    #en el get close matches hay un espacio
    #el 0  es una o y falta los brackets there
#0 en la palabra word osea  W0RD
#un words estava escrito wsord





    
    
    
    
    
