class Player:
    def __init__(self, name):
        self.name = name
        self.current_score = 0
        self.frames = []

    def return_current_score(self):
        # latest_frame_index = self.frames.length - 1
        try:
            self.current_score = 0
            for i in range(len(self.frames)):
                self.current_score += self.frames[i].num_pins_dropped
                if self.frames[i].strike:
                    pass
                elif self.frames[i].spare:
                    pass
        except:
            return "N/A"

        return self.current_score
