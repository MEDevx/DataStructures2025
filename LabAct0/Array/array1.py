pokemon = ["Charizard", "Pikachu", "Snorlax", "Cyndaquil", "Serperior" ] # Collection of Pokémon

print(f"\nMy favorite Pokémon: {pokemon}")

print("\nMy Cyndaquil evolved into Quilava. It is my new favorite now.")
pokemon[3]= "Quilava" # Replace the fourth element in the array
print(f"My favorite Pokémon: {pokemon}")

print("\nI recently started liking Eevee. It is one of my favorites now. ")
pokemon.insert(2,"Eevee") # Add Eevee to index 2 / as the 3rd element
print(f"My favorite Pokémon: {pokemon}")

print("\nI got tired of Snorlax, so it's no longer my favorite. ")
pokemon.remove("Snorlax") # Remove Snorlax from the array
print(f"My favorite Pokémon: {pokemon}\n")

