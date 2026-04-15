 
#task 1
 

total_cards = 52
red_cards = 26

# Q1
p_red = red_cards / total_cards
print(f"\nQ1: P(Red Card) = {p_red:.4f}")

# Q2
hearts = 13
p_heart_given_red = hearts / red_cards
print(f"\nQ2: P(Heart | Red) = {p_heart_given_red:.4f}")

# Q3
face_cards = 12
diamond_face_cards = 3
p_diamond_given_face = diamond_face_cards / face_cards
print(f"\nQ3: P(Diamond | Face Card) = {p_diamond_given_face:.4f}")

# Q4
spade_face = 3
queen_face = 4
overlap = 1

spade_or_queen_face = spade_face + queen_face - overlap
p_spade_or_queen_given_face = spade_or_queen_face / face_cards

print(f"\nQ4: P(Spade or Queen | Face Card) = {p_spade_or_queen_given_face:.4f}")
