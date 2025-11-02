
# --- 1. Print Survey Header and Ask Questions ---
print("SURVEY")

# Ask each question.
# .lower() handles 'y' or 'Y'.
# The '== 'y'' comparison immediately creates a Boolean (True/False)
# which is stored in the variable.
is_interested_cs = input('Are you interested in computer science? (y/n): ').lower() == 'y'
likes_games = input('Do you like playing computer games? (y/n): ').lower() == 'y'
has_instagram = input('Do you have an Instagram account? (y/n): ').lower() == 'y'


# --- 2. Print Survey Results ---
print("\nSURVEY RESULTS") # The '\n' adds a blank line for formatting

# When printing, convert the Boolean (True/False) to a "Yes"/"No" string.
# We use a ternary expression: 'value_if_true' if condition else 'value_if_false'
print(f"Interested in computer science: {'Yes' if is_interested_cs else 'No'}")
print(f"Playing computer games: {'Yes' if likes_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if has_instagram else 'No'}")
