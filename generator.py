from character_manager import load_roster, save_character

# loops to assign stats from a pool of total points
def allocate_stats(total_points):
    stats = {"Strength": 0, "Intelligence": 0, "Agility": 0}
    remaining_points = total_points

    print(f"\nYou have {remaining_points} attribute points to distribute.")
    
    # runs until all points are used
    while remaining_points > 0:
        for stat in stats.keys():
            # if points are all used up, stop looping
            if remaining_points <= 0:
                break
                
            print(f"\nPoints remaining: {remaining_points}")
            try:
                points = int(input(f"How many points for {stat}? "))
                if points < 0:
                    print("You cannot enter negative points.")
                    continue
                if points > remaining_points:
                    print(f"You don't have that many points left. Max allowed: {remaining_points}")
                    continue
                # add to stat and subtract from remaining_points
                stats[stat] += points
                remaining_points -= points
            # if value is not a valid number
            except ValueError:
                print("Please enter a valid whole number.")
                
    # assign points to stats.keys 
    return [stats["Strength"], stats["Intelligence"], stats["Agility"]]

# if this file is run directly, run
if __name__ == "__main__":
    print(" Welcome to the RPG Character Creator! ")
    
    # print saved characters
    print("\n--- Current Character Roster ---")
    current_roster = load_roster()
    if not current_roster:
        print("The roster is currently empty. Create your first hero!")
    else:
        for hero in current_roster:
            # print stats of each character/hero
            print(f"• {hero[0]} the {hero[1]} (STR: {hero[2]}, INT: {hero[3]}, AGI: {hero[4]})")
            
    # now option to create and save a new hero
    print("\n--- Create a New Hero ---")
    name = input("Enter your character's name: ").strip()
    
    print("Choose a class: 1. Warrior  2. Mage  3. Rogue")
    class_choice = input("Enter option (1-3): ")
    # choose class, assigned to 1-3
    classes = {"1": "Warrior", "2": "Mage", "3": "Rogue"}
    char_class = classes.get(class_choice, "Adventurer") # or default
    
    # after create character and class, assign stats with total points hard coded here
    final_stats = allocate_stats(total_points=15)
    
    # save character
    save_character(name, char_class, final_stats)
    print(f"\n {name} the {char_class} has been saved to the roster.")