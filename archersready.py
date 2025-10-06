#Every Archer Has its Arrows
#https://www.codewars.com/kata/559f89598c0d6c9b31000125
#This code checks if the archers have at least 5 arrows.
#Returns true if the list is empty and every value that is 5 or greater
#returns false if archers have fewer than 5 arrows 
def archers_ready(archers):
    return len(archers) > 0 and all(arrows >= 5 for arrows in archers)

print(archers_ready([1, 2, 3, 4, 5, 6, 7, 8])) 
print(archers_ready([5, 6, 7, 8]))             
print(archers_ready([]))                       

