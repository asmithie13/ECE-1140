class Block:
    def __init__(self,light,crossing,switch,state):
        self.light = light
        self.crossing = crossing
        self.switch = switch
        self.state = state  #if light, state = True => green, state = False => Red
                            #if crossing, state = True => Up, state = False => Down
                            #if switch, state = True => Default, state = False => Alternate

    