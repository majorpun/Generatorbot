import random
import randomnamegenerator

#The output is an object with seven keys output["name"], output["age"], output["characteristic"], output["trait"], output["occupation"], output["gender"], output["secret"]
 
with open("characteristics.txt", encoding='latin-1') as f:
    characteristiclist = f.read().splitlines() 
	
with open("medievalcharacteristics.txt", encoding='latin-1') as f:
    characteristiclist += f.read().splitlines() 
	
with open("traits.txt", encoding='latin-1') as f:
    traitlist = f.read().splitlines() 	
	
with open("fantasyoccupation.txt", encoding='latin-1') as f:
    occupationlist = f.read().splitlines() 	
	
with open("charactersecrets.txt", encoding='latin-1') as f:
    secretlist = f.read().splitlines() 	
	
with open("fantasycharactersecrets.txt", encoding='latin-1') as f:
    secretlist += f.read().splitlines() 	
	
with open("medievalcharactersecrets.txt", encoding='latin-1') as f:
    secretlist += f.read().splitlines() 
	
with open("femalename.txt", encoding='latin-1') as f:
    femalenamelist = f.read().splitlines()
	
with open("medievalfemalename.txt", encoding='latin-1') as f:
    femalenamelist += f.read().splitlines() 
	
with open("malename.txt", encoding='latin-1') as f:
    malenamelist = f.read().splitlines() 	
	
with open("medievalmalename.txt", encoding='latin-1') as f:
    malenamelist += f.read().splitlines() 
	
with open("surname.txt", encoding='latin-1') as f:
    surnamelist = f.read().splitlines() 	
	
with open("medievalsurname.txt", encoding='latin-1') as f:
    surnamelist += f.read().splitlines() 
	
def main(occupation = "generate"):
# Generates a random Non Player Character from tables and RNGs, the output is an object

	NPClist = []

	i = len(NPClist)
	
	NPClist.append({})
	

	if random.random() < 0.496:
		NPClist[i]["gender"] = "Male"
		NPClist[i]["name"] = random.choice(malenamelist)
	else:
		if random.random() < 0.978:
			NPClist[i]["gender"] = "Female"
			NPClist[i]["name"] = random.choice(femalenamelist)
		else:
			NPClist[i]["gender"] = "Unknown"
			NPClist[i]["name"] = random.choice(random.choice(malenamelist),random.choice(femalenamelist))
			
	if random.random() < 0.5:
		NPClist[i]["name"] += " " + random.choice(surnamelist)
			
	if random.random() < 0.8:			
		NPClist[i]["age"] = random.randint(15, 40)
	else:
		NPClist[i]["age"] = random.randint(40, 90)
	NPClist[i]["characteristic"] = str(random.choice(characteristiclist))
	NPClist[i]["trait"] = random.choice(traitlist)
	
	if occupation == "generate":
		NPClist[i]["occupation"] = random.choice(occupationlist)
		NPClist[i]["occupationgenerated"] = True 
	else:
		NPClist[i]["occupation"] = occupation
		NPClist[i]["occupationgenerated"] = False 
	
	if random.random() < 0.30:
		NPClist[i]["secret"] = random.choice(secretlist)
	else:
		NPClist[i]["secret"] = "Has no secret"
		
	return(NPClist[i])
   


   

