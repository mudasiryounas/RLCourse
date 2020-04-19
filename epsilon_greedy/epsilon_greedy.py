import matplotlib.pyplot as plt
import numpy as np

NUM_TRIALS = 10000
EPS = 0.1
MACHINE_PROBABILITIES = [0.2, 0.5, 0.75]


class Machine:
    def __init__(self, p):
        self.p = p
        self.p_estimated_mean = 0.0  # current estimated win rate
        self.N = 0.0  # num samples tried and collected so far

    def pull(self):
        random_num = np.random.random()  # [0.0, 1.0)
        return random_num < self.p

    def update(self, x):  # x = 0 or 1
        self.N += 1.0
        self.p_estimated_mean = ((self.N - 1) * self.p_estimated_mean + x) / self.N  # mean success rate


def experiment():
    machines = [Machine(m) for m in MACHINE_PROBABILITIES]
    rewards = np.zeros(NUM_TRIALS)
    num_of_times_explored = 0
    num_of_times_exploited = 0
    num_optimal = 0
    optimal_machine_index = np.argmax([m.p for m in machines])

    print("optimal machine number: ", optimal_machine_index)

    for i in range(NUM_TRIALS):
        # use epsilon-greedy to select next machine
        if np.random.random() < EPS:
            num_of_times_explored += 1
            machine_index = np.random.randint(len(machines))  # will give 0, 1 or 2
        else:
            num_of_times_exploited += 1
            machine_index = np.argmax([m.p_estimated_mean for m in machines])

        if machine_index == optimal_machine_index:
            num_optimal += 1

        # pull arm for machine with the largest sample
        m = machines[machine_index]
        x = m.pull()

        rewards[i] = x

        # update the distribution for machine whose arm we just pulled
        m.update(x)

    print(f"original machine probabilities: {MACHINE_PROBABILITIES}")
    for i, m in enumerate(machines):
        print(f"mean estimate for machine {i}: {m.p_estimated_mean}")

    print("total reward earned: ", rewards.sum())
    print("overall win rate: ", rewards.sum() / NUM_TRIALS)
    print("num_of_times_explored: ", num_of_times_explored)
    print("num_of_times_exploited: ", num_of_times_exploited)
    print("num times selected optimal machine: ", num_optimal)

    # plot the result
    cumulative_rewards = np.cumsum(rewards)
    win_rates = cumulative_rewards / (np.arange(NUM_TRIALS) + 1)
    plt.plot(win_rates)
    plt.plot(np.ones(NUM_TRIALS) * np.max(MACHINE_PROBABILITIES))
    plt.show()


if __name__ == '__main__':
    experiment()
