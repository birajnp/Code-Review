---
title: "Pair Programming Activity"
teaching: 0
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

## Setup
* Pair up with someone
    * Install Live Share or Code With Me if you use VS Code or PyCharm and want to try it
* Clone the "[Code-Review](https://github.com/INTERSECT-training/Code-Review)" repo
    * What you need for this activity is in the “activity” folder
* Make sure it runs on your system:
    * Run ```python3 inklimit.py testimage.tiff outimage.tiff```
    * Install any missing modules by running ```pip3 install {moduleName}```
        * E.g. ```pip3 install tifffile```
* Make sure you can view the input and your output image files
    * How to do that depends on your system

## Task
You have a complaint from users: The inkjet printer leaves puddles of ink in the dark areas!

Your task is to:
* Change the code in inklimit.py to limit the total ink in the C, M, Y and K planes for each pixel to a given percentage (e.g. 240%)
* Avoid changing the perceived color of the image
* To limit the time needed for this task, I have provided you with the boilerplate code to open, read and write TIFF files
* Your team needs only to implement the actual ink limiting algorithm

You should now choose who will Drive, who will Navigate, and begin working.

Remember to communicate! What possible approachs could you take?

This process is about the pair programming process, not the code!

{% include links.md %}

