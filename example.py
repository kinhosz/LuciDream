from Lucidream import Dream

dream = Dream()

# Defina o início da história
dream.addScene("start", "You wake up in a mysterious room.", image="assets/room.jpg")

# Adicione escolhas
dream.addChoice("start", "Go through the door", "door_scene")
dream.addChoice("start", "Look out the window", "window_scene")

# Defina Cenas
dream.addScene("door_scene", "You find a hallway.", image="assets/hallway.jpg")
dream.addScene("window_scene", "You see a garden below.", image="assets/garden.jpg")

# fim da história
dream.addChoice("door_scene", "Go to end", "end")
dream.addChoice("window_scene", "Go to end", "end")

dream.addScene("end", "the end", image="assets/end.jpg")

# Execute a história
dream.run()
