import ly


class Unit:
    def __init__(self, location, color, speed):
        self.location = location
        self.color = color
        self.speed = speed
        self.destination = location
        self.yums=0

    def move(self):
        if self.location == self.destination:
            self.destination = ly.randgen_location(700, 800)
        self.location = ly.move_to_destination(self.location, self.destination, self.speed)



