class modelbase:
    def __init__(self):
        self.previous_mode = None

    def update(self, percept):
        temp = percept.get('temperature', 20)
        occupied = percept.get('occupied', False)

        if not occupied:
            target_mode = "off"
        elif temp > 25:
            target_mode = "off"
        elif temp < 18:
            target_mode = "off"
        else:
            target_mode = "idle"

        if target_mode != self.previous_mode:
            send_command = True
            self.previous_mode = target_mode
        else:
            send_command = False

        return target_mode, send_command