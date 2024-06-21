---
title: "Code Review Activity"
teaching: 0
exercises: 0
questions:
- "What challenges and opportunities did you experience during the exercise?"
objectives:
- "Learn how to review code in github"
keypoints:
- "Strive to review PRs that solve a single issue."
---

## Code Review in Github
You don't have to perform code reviews in github, but they are nicely integrated
and widely used so it is helpful to practice there.  Ideally, your project would
develop in the following cycle:
1. A user requests a feature or notices a bug.  They open an **issue**.  Each
issue should contain a single problem or feature and be self contained.
2. A developer works on the issue, implementing the feature or fixing the bug.
The submit a **pull request** consisting of (possibly several) small commits.
Commits should be atomic, e.g. can be selected and applied in any order.
3. A maintainer or other developer **reviews** the pull request.  They should ensure
the PR addresses the issue (and only the issue) while maintaining a high quality
of code in the project.

Obviously, life would be easy if this were always true.  If you are the only developer
you would have to perform all these operations.  As you implement a feature,
maybe you decide to refactor a method at the same time.  When you are rushed,
you may be tempted to merge a PR immediately, foregoing the review.  Try to
resist these urges, especially as you are forming your code review habit.

You can also review code outside of github.  Maybe a coworker calls you over
and you look at a function implementation on their screen and give some quick
feedback.  Or you edit an answer on stack overflow to improve it.  Maybe a
collaborator emails a notebook and you recommend some functions to reduce
duplication in their cells.  These are all valuable and good practice of the
method of critically reviewing other people's code.  However, here we will focus
on the mechanics of providing feedback on a PR in github.

## Code Review Activity
We will be using the excellent practice materials from [code-review.org](code-review.org).

1. [Setup the tutorial](https://code-review.org/docs/setup/setup/) on github.
   Create the text and python exercises.
2. Look over the issue for "text: Exercise 1" and the corresponding recipe.
3. Open the PR for "Exercise 1 text."
    - What do you think of their commits?  The recommended fixes?  Anything to add or change?
4. Click on the "files changed" tab and start a review
5. When you have finished your review, swap reviews with someone else and review
   their reviews!  Focus on the content, tone and helpfulness.  Discuss what you
   liked or they could have done better.
6. Repeat the above with python Exercise 1.
    - Now you can focus on code quality a bit more.  Use what you've learned
      here and in other modules to improve the PR.
    - Before you get carried away with recommendations, what are the ideal
      next steps for recommending larger changes?
7. (Optional) if you have time, review another PR from the tutorial repo,
   a PR from another participant, or a PR in a project you like.

{% include links.md %}

