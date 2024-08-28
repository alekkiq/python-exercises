# Python exercises

## About

These Python exercises act as a part of my first year studies in my engineering degree.

Despite the task instructions being in Finnish, the coded solutions are strictly in English, due to the English nature of the profession that is software development.

This README was made purely to serve as practice in documenting a project / codebase. Anyone with pretty much any experience with codebases or coding in general will get the idea just by looking at the directory structure as well as the singular files / scripts themselves (hopefully).

### Requirements

To set up the "project" locally, you will need

1. **Python** 3.12.x <
2. **MariaDB** 11.5.x <
3. ```airports.csv``` with correct data as in this example:

```json
"id","ident","type","name","latitude_deg","longitude_deg","elevation_ft","continent","iso_country","iso_region","municipality","scheduled_service","gps_code","iata_code","local_code","home_link","wikipedia_link","keywords"
6523,"00A","heliport","Total Rf Heliport",40.07080078125,-74.93360137939453,11,"NA","US","US-PA","Bensalem","no","00A",,"00A",,,
323361,"00AA","small_airport","Aero B Ranch Airport",38.704022,-101.473911,3435,"NA","US","US-KS","Leoti","no","00AA",,"00AA",,,
6524,"00AK","small_airport","Lowell Field",59.947733,-151.692524,450,"NA","US","US-AK","Anchor Point","no","00AK",,"00AK",,,

...
```

And the following python packages:
1. `mysql-connector-python`
2. `pandas`
3. `geopy`
4. `tabulate`

<div style="color: #0c5460;
  background-color: #d1ecf1;
  border-color: #bee5eb; padding: 16px 24px; border-radius: 5px; margin-block: 20px; line-height: 1.75">
<b>Important:</b> Make sure to add the proper values in <code style="color: black; padding: 4px 6px">Modules/db_helpers/db_config.py</code> to match your systems MariaDB configs. You also have to add the <code style="color: black; padding: 4px 6px">airports.csv</code> to <code style="color: black; padding: 4px 6px">Modules/db_helpers/data/</code> if you do not already have the right database set up in your computer. Alternatively, you can insert the data manually to the right database.
</div>

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

1. **Python** - duh. But being serious, prior to this course I had next to no experience with python, but a better understanding in other languages such as Php, Javascript and even Java. Like always, switching to a new language and syntax can be overwhelming, but I believe I actually overcame that surprisingly quick.
2. **Problem solving**. It is common knowledge that coding is pretty much all about solving problems, and I think this course capsulated it well. The theory parts were exhausting, but rather had a lot of useful info in a very compact package. This made reading through the theory a lot less exhaustive.
3. **Thinking**. At first glance this might sound odd, but it makes perfect sense. During these excersises I occasionally found myself overcomplicating even the most simplest of problems. But as I progressed in the tasks, I gradually learned to stop and think about alternative solutions and their pros&cons before writing any lines of code.