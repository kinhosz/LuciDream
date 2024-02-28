from Lucidream import Dream

dream = Dream()

# Defina o início da história
dream.addScene("start", "You wake up in a mysterious room.", image="room.jpg")

# Adicione escolhas
dream.addChoice("start", "Go through the door", "door_scene")
dream.addChoice("start", "Look out the window", "window_scene")

# Defina Cenas
dream.addScene("door_scene", "You find a hallway.", image="hallway.jpg")
dream.addScene("window_scene", "You see a garden below.", image="garden.jpg")

# Execute a história
dream.run()
