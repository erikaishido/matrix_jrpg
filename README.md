# matrix_jrpg
 a JRPG ish thing that runs in the lil vscode box.
\n
\nwasd: movement
\nx: interact or select menu
\nm: open/close menu
\n(only detects lower case letters)
\n(you will have to type Enter after every input)

# questions
- references to the map entity objects are stored, and only stored in the tilemap (specifically the EntityLayer class). should I have another place to store their references? perhaps a list?

# really future todos
- don't think about implementing combat for now
- turn self.state (inside statemachine) into a state stack, to allow easier handling of textboxes and yes/no prompts
- move valid input keys into an editable config file

# honorable mentions
- https://gameprogrammingpatterns.com/
- https://code.tutsplus.com/how-to-build-a-jrpg-a-primer-for-game-developers--gamedev-6676a
