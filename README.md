# Python exercises

## About

These Python exercises act as a part of my first year studies in my engineering degree.

Despite the task instructions being in Finnish, the coded solutions are strictly in English, due to the English nature of the profession that is programming.

This README was made purely to serve as practice in documenting a project / codebase. Anyone with pretty much any experience with codebases or coding in general will get the idea just by looking at the directory structure as well as the singular files / scripts themselves.

### Viewing / running the exercises

The exercises will all be found under the ```Modules``` folder.

Most common way you will find a singular exercise is by navigating to a ```mod0X.py``` file, and checking out the functions. Each function represents a single exercise.

Each python file is named after the **module** which exercises it consists of. For example, ```mod03.py``` contains all exercises under module 1.

The exercises themselves are (***MAINLY***) separated into functions. The functions are mostly named to describe the scripts outcome rather than displaying the exercise number. You can tell which exercise does each function represent by looking for a number comment above each function's definition. 

Below is an example:

```python
# >mod02.py <--  The module number

# 4 <-- The exercise number
def print_something():
    something = input("Input something: ")
    print(something)

#   print_something() <-- Call the function by uncommenting!
```

There are some exceptions to this though, the most obvious one being the whole of **Module 6**. Since Module 6 is the part that is supposed to introduce functions, I made the decision to split each exercise into it's own file.

In these cases the files are pretty self-explanitary as there is just the "logic" function and a main function that is being ran.

Like so:
```python
# >/mod6/2.py <-- module & exercise number

import random

# 2
def roll_custom_dice(dice_sides : int):
    while (True):
        rolled_value = random.randint(1, dice_sides)
        
        print(f"Rolled {rolled_value}")
        
        if rolled_value == dice_sides:
            break

def main():
    dice_sides = int(input("How many sides does the dice have: "))

    roll_custom_dice(dice_sides)

main() # <-- The exercise runs when main() is called.
```

___________________
### What I've learned?

1. **Python** - duh. But being serious, prior to this course I had next to no experience with python, but a better understanding in other languages such as Php, Javascript and even Java. Like always, switching to a new language and syntax can be hard, but I believe I actually overcame that surprisingly quick.
2. **Problem solving**. It is common knowledge that coding is pretty much all about solving problems, and I think this course capsulated it well. The theory parts were exhausting, but rather had a lot of useful info in a very compact package. This made reading through the theory a lot less exhaustive.
3. **Thinking**. At first glance this might sound odd, but it makes perfect sense. During these excersises I occasionally found myself overcomplicating even the most simplest of problems. But as I progressed in the tasks, I gradually learned to stop and think about alternative solutions and their pros&cons before writing any lines of code.