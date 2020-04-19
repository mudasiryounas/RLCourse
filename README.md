
# Epsilon Greedy Strategy Theory

<p align="center"><img src="https://github.com/mudasiryounas/RLCourse/blob/master/epsilon_greedy/theory/p1.jpeg" width="450"></p>
<p align="center"><img src="https://github.com/mudasiryounas/RLCourse/blob/master/epsilon_greedy/theory/p2.jpeg" width="450"></p>
<p align="center"><img src="https://github.com/mudasiryounas/RLCourse/blob/master/epsilon_greedy/theory/p3.jpeg" width="450"></p>


## Output 

```
optimal machine number:  2
original machine probabilities: [0.2, 0.5, 0.75]
mean estimate for machine 0: 0.1702786377708978
mean estimate for machine 1: 0.4608150470219436
mean estimate for machine 2: 0.7493054071382783
total reward earned:  7214.0
overall win rate:  0.7214
num_of_times_explored:  982
num_of_times_exploited:  9018
num times selected optimal machine:  9358
```

<p align="center"><img src="https://github.com/mudasiryounas/RLCourse/blob/master/epsilon_greedy/theory/p4.png" width="450"></p>


# Optimistic Initial Values Strategy Theory

<p align="center"><img src="https://github.com/mudasiryounas/RLCourse/blob/master/optimistic_initial_values/theory/p1.jpeg" width="450"></p>
<p align="center"><img src="https://github.com/mudasiryounas/RLCourse/blob/master/optimistic_initial_values/theory/p2.jpeg" width="450"></p>


## Output
```
original machine probabilities: [0.2, 0.5, 0.75]
mean estimate for machine 0: 0.7333333333333333
mean estimate for machine 1: 0.7391304347826086
mean estimate for machine 2: 0.7538384345208254
total reward earned:  7525.0
overall win rate:  0.7525
number of times each machine selected [15.0, 23.0, 9965.0]
```

look at the mean estimate values they are not 0.75 (which is our true mean) but they are close to it, so our algorithm is greedy and it does not go anymore.

if we look at the number of times each machine is selected [15.0, 23.0, 9965.0], we can understand that as soon as their estimate mean value goes below 0.75 they are no longer selected and hence our last machine which is optimal, is select rest of the times, i.e 9983 times. 

<p align="center"><img src="https://github.com/mudasiryounas/RLCourse/blob/master/optimistic_initial_values/theory/p3.png" width="450"></p>

