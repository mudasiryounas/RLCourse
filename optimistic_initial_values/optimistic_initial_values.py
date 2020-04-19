import matplotlib.pyplot as plt
import numpy as np

NUM_TRIALS = 10000
EPS = 0.1
MACHINE_PROBABILITIES = [0.2, 0.5, 0.75]


class Machine:
    def __init__(self, p):
        self.p = p
        self.p_estimated_mean = 5.0  # initial estimated mean
        self.N = 1.0  # number of tests tried or pulled so far (initialize with 1 otherwise will be removed by update function because (self.N - 1) will become 0)

    def pull(self):
        random_num = np.random.random()  # [0.0, 1.0)
        return random_num < self.p

    def update(self, x):  # x = 0 or 1
        self.N += 1.0
        self.p_estimated_mean = ((self.N - 1) * self.p_estimated_mean + x) / self.N  # mean success rate


def experiment():
    machines = [Machine(m) for m in MACHINE_PROBABILITIES]
    rewards = np.zeros(NUM_TRIALS)

    for i in range(NUM_TRIALS):
        # select next machine
        machine_index = np.argmax([m.p_estimated_mean for m in machines])

        selected_machine = machines[machine_index]
        # pull the arm of machine with largest estimated mean
        x = selected_machine.pull()
        rewards[i] = x
        # update this machine estimated mean
        selected_machine.update(x)

    print(f"original machine probabilities: {MACHINE_PROBABILITIES}")
    for i, m in enumerate(machines):
        print(f"mean estimate for machine {i}: {m.p_estimated_mean}")

    print("total reward earned: ", rewards.sum())
    print("overall win rate: ", rewards.sum() / NUM_TRIALS)
    print(f"number of times each machine selected {[m.N for m in machines]}")

    # plot the result
    cumulative_rewards = np.cumsum(rewards)
    win_rates = cumulative_rewards / (np.arange(NUM_TRIALS) + 1)
    plt.ylim([0, 1])
    plt.plot(win_rates)
    plt.plot(np.ones(NUM_TRIALS) * np.max(MACHINE_PROBABILITIES))
    plt.show()


if __name__ == '__main__':
    experiment()
