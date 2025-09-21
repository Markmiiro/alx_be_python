#PROMPT USER FOR INPUT
weather = input("what is the weather like today?(sunny/rainy/cold: ").lower()
#provide clothing reccomendations
if weather == "sunny":
    print("wear a t-shirt and sun glasses")
elif weather == "rainy":
    print ("dont forget your umbrealla and rain coat")
elif weather =="cold":    
    print ("Make sure to wear a warm coat and a scarf")   
else :
    print("sorry, i dont have recommendations for this weather")     