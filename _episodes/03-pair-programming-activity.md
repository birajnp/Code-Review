---
title: "Pair Programming Activity"
teaching: 0
exercises: 0
questions:
- "What are some benefits and challenges with pair programming?"
objectives:
- Experience pair programming
keypoints:
- "Pair programming is a skill and practice will improve your experience as a
driver and navigator."
---

## Setup
* Pair up with someone
    * Install Live Share or Code With Me if you use VS Code or PyCharm and want to try it
    * Or setup a zoom, teams, meet, huddle to share screens
    * Or sit close to each other
* Clone the "[Code-Review](https://github.com/INTERSECT-training/Code-Review)" repo
or download the script and test image:
    * `git clone https://github.com/INTERSECT-training/Code-Review.git`
    * OR 
        * `wget https://raw.githubusercontent.com/INTERSECT-training/Code-Review/main/activity/inklimit.py`
        * `wget https://raw.githubusercontent.com/INTERSECT-training/Code-Review/main/activity/testimage.tiff`
    * We will work in the `activity` folder
    * Ideally you would have a shared file system or switch roles after a commit.
    You can borrow each others' computer or work on discrete portions of the script.
* Install any dependencies:
    * (Recommended) Make a new virtual environment or conda env
    * `pip install numpy pillow`
    * Run `python3 inklimit.py testimage.tiff outimage.tiff` to test the script
        works.
* Make sure you can view the input and your output image files

## Task
You have a complaint from users: The inkjet printer leaves puddles of ink in the dark areas!

Your task is to:
* Change the code in inklimit.py to limit the total ink in the C, M, Y and K planes for each pixel to a given percentage (e.g. 240%)
* Avoid changing the perceived color of the image
* To limit the time needed for this task, you have a skeleton of the algorithm.  Extend the base class and implement the `apply` function
* Your team needs only to implement the actual ink limiting algorithm

You should now choose who will Drive, who will Navigate, and begin working.
About half-way through, you can swap roles.

Remember to communicate! What possible approaches could you take?

This process is about the pair programming process, not the code!  If you have
extra time you can polish and refactor other parts of the code.

{% include links.md %}

