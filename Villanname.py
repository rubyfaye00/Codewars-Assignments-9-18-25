#Find Your Villan Name
#https://www.codewars.com/kata/536c00e21da4dc0a0700128b
#This code generates a Villan Name based of of your birthday.
#Uses the birth month to select an adjective from a list and the last digit of the birth day to choose a noun.
#This combined creates the final name, I used my birthday Novemeber 20th to get "The Terrifying Mustache"

from datetime import date
def get_villain_name(birthdate): 
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    return first[birthdate.month - 1] + ' ' + last[int(str(birthdate.day)[-1])]

birthday = date(2006, 11, 20)  
print(get_villain_name(birthday))

