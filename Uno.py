def can_play(hand, face_up):
    
    if not hand:
        return False
    
    face_color, face_number = face_up.split()

    for card in hand:
        card_color, card_number = card.split()
        if card_color == face_color or card_number == face_number:
            return True

    return False

print(can_play(["yellow 3", "yellow 7", "blue 8", "red 9", "red 2"], "red 1"))  
print(can_play(["yellow 3", "yellow 7"], "blue 7"))                             
print(can_play(["yellow 3", "yellow 5", "red 8"], "red 2"))                     
print(can_play(["yellow 3", "yellow 5", "red 8"], "blue 5"))                    
print(can_play(["yellow 3", "blue 5", "red 8", "red 9"], "green 4"))            
print(can_play(["yellow 3", "red 8"], "green 2"))                               
print(can_play([], "red 5"))                                                    
