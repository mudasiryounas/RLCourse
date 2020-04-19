import matplotlib.pyplot as plt
import numpy as np

NUM_TRIALS = 10000
EPS = 0.1
MACHINE_PROBABILITIES = [0.2, 0.5, 0.75]


class Machine:
    def __init__(self, p):
        self.p = p
        self.p_estimated_mean = 0.0
        self.N = 0.0  # number of tests tried or pulled so far

    def pull(self):
        random_num = np.random.random()  # [0.0, 1.0)
        return random_num < self.p

    def update(self, x):  # x = 0 or 1
        self.N += 1.0
        self.p_estimated_mean = ((self.N - 1) * self.p_estimated_mean + x) / self.N


def ucb(mean, N, nj):
    return mean + np.sqrt(2 * (np.log(N) / nj))


def run_experiment():
    machines = [Machine(p) for p in MACHINE_PROBABILITIES]
    rewards = np.empty(NUM_TRIALS)
    total_plays = 0

    # initially play each machine once
    for machine in machines:
        x = machine.pull()
        total_plays += 1
        machine.update(x)

    for i in range(NUM_TRIALS):
        j = np.argmax([ucb(machine.p_estimated_mean, total_plays, machine.N) for machine in machines])
        j_machine = machines[j]
        x = j_machine.pull()
        total_plays += 1
        j_machine.update(x)

        # for the plot
        rewards[i] = x

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
    run_experiment()
