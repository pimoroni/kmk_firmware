import digitalio


class GPIOScanner:
    def __init__(
        self,
        pins,
        rowcount=4,
        colcount=4,
        pull=digitalio.Pull.UP
    ):

        self.inputs = [
            x
            if x.__class__.__name__ is 'DigitalInOut'
            else digitalio.DigitalInOut(x)
            for x in pins
        ]

        for pin in self.inputs:
            pin.switch_to_input(pull=digitalio.Pull.UP)

        self.len_state_arrays = len(pins)
        self.state = bytearray(self.len_state_arrays)
        self.report = bytearray(3)

    def scan_for_changes(self):
        for idx, pin in enumerate(self.inputs):
            new_val = int(not pin.value)
            old_val = self.state[idx]

            if old_val != new_val:
                self.report[0] = idx % 4
                self.report[1] = idx // 4
                self.report[2] = new_val
                self.state[idx] = new_val
                return self.report

        return None
