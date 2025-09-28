def filter_text(text): 
#remove extra spaces and split into words
    words = text.strip().split()
#lowercase words
    words = [word.lower() for word in words]
#rejoin the words together 
    filter = ' '.join(words)
#Capitalize the first letter 
    if filter:
        filter = filter[0].upper() + filter[1:]
        return filter
    
print(filter_text("HOW ARE YOU TODAY"))
print(filter_text("how DOES this worK"))
print(filter_text("CAN YOU hear Me"))