---
title: "Introduction"
teaching: 0
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

## Collaborative Construction Introduction

Testing and debugging are not the best way to find software defects. 
Their primary benefits are to quickly detect and prevent regressions.

Collaborative construction techniques, such as design- and code-reviews are much better at finding defects. 
Two widely-used techniques are:
* Code reviews (extremely widespread)
* Pair-programming (less widespread)

By performing reviews:
* Reviewers can identify bugs that the developer may have overlooked
* Reviewers can gauge how well the code actually satisfies the requirements
* Reviewers may be able to suggest better designs, better refactorings of the code being reviewed, other improvements
* Since reviewers are often less familiar with the code, they can point out where coding style or commenting needs to be improved
* Reviewers can verify that the code has sufficient test-automation, and can suggest additional tests to improve verification

While collaborative construction techniques are often presented as being focused on finding defects, there are many other benefits to be realized from these practices.
* It generates positive peer-pressure to maintain a high standard of code quality, such as performing better commenting, code-cleanup tasks, and writing good tests.
* It facilitates knowledge-transfer among teammates and helps more people understand how the project's code functions.
    * This is an excellent opportunity to mentor junior developers in best-practices.
* It fosters healthy team dynamics by teaching teammates how to give and receive thoughtful feedback with each other and developing a sense of *community responsibility* for project code.
    * This reduces the feeligns of "*my* code" and increases feelings of "*our* code."



{% include links.md %}

