# Rough Outline

1. write history (earlier?)
2. generate rooms/dungeon
3. place rooms
4. make 1:1 image with different colored pixels for different rooms and such (but walls???)
5. take 1:1 and use another algorithm to upscale it and add walls
6. other algorithm will populate rooms with loot/monsters (use encounter generator/calculator to check that encounters are safe.)

# OUTLINE

## Dungeon 1:1 img generation

1. Choose Room
    - Choose Random room
2. Choose Direction
    - Look for obstructions (room, edge, etc)
    - choose out of remaining options
3. Choose Distance
    - Distance based on density and a random factor
    - Draw Hallway
4. Place Room
    - Randomly choose size
    - Choose location based on where the hallway is and size
    - Check for obstructions
    - if obstruction is found, change size and check again. (until tried 3 times)
    - Append room stats to dungeon object



# NOTES

- maybe just do an encounter generator?? (need array of monsters/api with monster data.) (great starting point)
