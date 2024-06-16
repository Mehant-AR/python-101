def calculate_scrabble_score(word):
    # Dictionary mapping letters to points
    letter_points = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,
        'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,
        'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
        'Y': 4, 'Z': 10
    }
    
    score = 0
    for letter in word:
        letter = letter.upper()
        score += letter_points.get(letter, 0)  # Add the points for each letter, defaulting to 0 if not found
    
    return score

word=input()
score = calculate_scrabble_score(word)
print(f"{word} is worth {score} points.")
