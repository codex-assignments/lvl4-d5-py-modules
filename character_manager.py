# reads saved characters from a file and returns lists of info
def load_roster(filename="characters.txt"):
    roster = []
    try:
        # python opens, and "r" indicates reads from 
        with open(filename, "r") as file:
            for line in file:
                # strip and split by comma
                name, char_class, strength, intelligence, agility = line.strip().split(",")
                # takes line of text from file, converts stats to ints/numbers and nests in a list
                # each list will represent all stats for one character
                roster.append([name, char_class, int(strength), int(intelligence), int(agility)])
    except FileNotFoundError:
        # if no file exists yet, return empty
        return []
    return roster

def save_character(name, char_class, stats, filename="characters.txt"):
    # appends a new character to the text file
    # python opens or creates file if it doesn't exist, and "a" indicates appends
    with open(filename, "a") as file:
        file.write(f"{name},{char_class},{stats[0]},{stats[1]},{stats[2]}\n")