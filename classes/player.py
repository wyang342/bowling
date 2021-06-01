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
                    if self.frames[i + 1].strike:
                        pass
                    else:
                        self.current_score += self.frames[i+1].num_pins_dropped
                elif self.frames[i].spare:
                    self.current_score += self.frames[i+1].delivery_1
        except:
            return "N/A"

        return self.current_score
