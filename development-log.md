# Development Log

## Log date: 2020-06-14
The main menu is mostly done. I've set up the main menu to take the user input and see if it is a key in a dictionary I've defined in order to run it. This way I can minimise changes to the main program and add functions to the dictionary instead of the main loop if I choose to implement more menu items in the future. I'm not sure if using an eval will cause issues, but the try-except block should keep the program from crashing.

## Log date: 2020-06-16
I've run into an issue with the accuracy calculation. While the solution is quite simple when the user's input is the same length as the sentence to type, the calculation becomes a bit awkward when the lengths are different, particularly as I have to loop over the sentence and could potentially overflow the index. Some of the formulas I've tried have ended with unintuitive results on fringe test cases (e.g. negative scores or scores over 100%), so I need to find an expression that can only return a value between 0 and 100%. I'm currently trying correct_chars / (correct_chars + incorrect_chars).

## Log date: 2020-06-17
An issue with the 'talking' terminal I'm trying to create is that for for some reason the print function only prints one line at a time; even if I have a loop like this:  

```python
print('Loading', end='')
for i in range(1, 5):
    print('.', end = '')
    time.sleep(1)
print('\nLoaded')
```
The entire line prints after 5 seconds rather than printing 'Loading' then a period each second.  

It looks like the issue is that print has a flish parameter that is by default False, causing it to buffer the output. By setting it to True I getthe desired result.

## Log date: 2020-06-19
Functional testing is all green. The debug mode implemented using sys.argv really sped up the process compared to spot checks I was performing in the past. I think I should have gotten more feedback from my peers in regards to the delay timers. At the start of the project, it seemed to be an appropriate speed but it seems slow now, but that could be because of how much I personally use the program. Luckily I've kept it as a static so it should be easy to change in the future.