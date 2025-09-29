def archers_ready(archers):
    return len(archers) > 0 and all(arrows >= 5 for arrows in archers)

print(archers_ready([1, 2, 3, 4, 5, 6, 7, 8])) 
print(archers_ready([5, 6, 7, 8]))             
print(archers_ready([]))                       
