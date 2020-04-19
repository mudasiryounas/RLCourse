
# Optimistic Initial Values Strategy Theory

![Optimistic Initial Values Strategy Theory P1](https://github.com/mudasiryounas/RLCourse/blob/master/optimistic_initial_values/theory/p1.jpeg)

![Optimistic Initial Values Strategy Theory P2](https://github.com/mudasiryounas/RLCourse/blob/master/optimistic_initial_values/theory/p2.jpeg)


```
mean estimate for machine 0: 0.625
mean estimate for machine 1: 0.6666666666666666
mean estimate for machine 2: 0.7555844936391872
total reward earned:  7541.0
overall win rate:  0.7541
number of times each machine selected [8.0, 12.0, 9983.0]
```

look at the mean estimate values they are not 0.75 (which is our tru mean) but they are close to it, so our algorithm is greedy and it does not go anymore.

if we look at the number of times each machine is selected, we can understand that as soon as their estimate mean value goes below 0.75 they are no longer selected and hence our last machine ewhich is optimal is remained and select 9983 times. 

![Optimistic Initial Values Strategy Theory P4](https://github.com/mudasiryounas/RLCourse/blob/master/optimistic_initial_values/theory/p3.jpeg)
