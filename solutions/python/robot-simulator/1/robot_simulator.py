# Globals for the directions
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot:
    _directions = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        if direction not in self._directions:
            raise ValueError("Invalid direction")

        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def turn_right(self):
        i = self._directions.index(self.direction)
        self.direction = self._directions[(i + 1) % 4]

    def turn_left(self):
        i = self._directions.index(self.direction)
        self.direction = self._directions[(i - 1) % 4]

    def advance(self):
        x, y = self.coordinates

        if self.direction == NORTH:
            y += 1
        elif self.direction == SOUTH:
            y -= 1
        elif self.direction == EAST:
            x += 1
        elif self.direction == WEST:
            x -= 1

        self.coordinates = (x, y)

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self.turn_right()
            elif instruction == "L":
                self.turn_left()
            elif instruction == "A":
                self.advance()
            else:
                raise ValueError("Invalid instruction")