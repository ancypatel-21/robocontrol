class Metrics:
    def __init__(self):
        self.errors = []
        self.control_signals = []

    def record(self, error, control_signal):
        self.errors.append(abs(error))
        self.control_signals.append(abs(control_signal))

    def summary(self):
        avg_error = sum(self.errors) / len(self.errors) if self.errors else 0
        avg_control = sum(self.control_signals) / len(self.control_signals) if self.control_signals else 0

        print("\n=== Metrics Summary ===")
        print(f"Average absolute error: {avg_error:.4f}")
        print(f"Average control signal: {avg_control:.4f}")