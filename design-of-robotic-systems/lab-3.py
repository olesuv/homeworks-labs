import numpy as np
import matplotlib.pyplot as plt


class PIDSimulator:
    def __init__(self, Kp, Ki, Kd, time_end, y0, dt):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.time_end = time_end
        self.y0 = y0
        self.dt = dt
        self.y = None

    def simulate(self):
        time_steps = int(self.time_end / self.dt)
        self.y = np.zeros(time_steps)
        integral = 0
        self.y[0] = self.y0

        for t in range(1, time_steps):
            error = -self.y[t - 1]
            integral += error * self.dt
            derivative = (self.y[t] - self.y[t - 1]) / self.dt if t > 1 else 0
            self.y[t] = self.Kp * error + self.Ki * integral + self.Kd * derivative

        return self.y

    def plot(self):
        if self.y is None:
            print("No data to plot. Please run simulate() first.")
            return

        plt.plot(self.y, label=f"Kp={self.Kp}, Ki={self.Ki}, Kd={self.Kd}")
        plt.title("PID Controller Simulation")
        plt.xlabel("Time (steps)")
        plt.ylabel("Deviation y(t)")
        plt.legend()
        plt.grid(True)


time_end = 50
y0 = 10
dt = 1

coefficients = [
    {"Kp": 0.4, "Ki": 0, "Kd": 0},
    {"Kp": 0.2, "Ki": 0.05, "Kd": 0},
    {"Kp": 0.45, "Ki": 0, "Kd": 0.01},
    {"Kp": 0.1, "Ki": 0.03, "Kd": 0.21},
    {"Kp": 0.25, "Ki": 0.05, "Kd": 0},
    {"Kp": 0.6, "Ki": 0, "Kd": 0.04},
    {"Kp": 0.12, "Ki": 0.02, "Kd": 0.1},
]

plt.figure(figsize=(12, 8))
for coeff in coefficients:
    simulator = PIDSimulator(coeff["Kp"], coeff["Ki"], coeff["Kd"], time_end, y0, dt)
    simulator.simulate()
    simulator.plot()

plt.title("PID Controller Simulation for Various Coefficient Sets")
plt.show()
