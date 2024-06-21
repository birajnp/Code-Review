---
title: "Best Practices"
teaching: 0
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

## Best Practices for Code Reviews
In this episode, we will learn about the best practices of code-reviews regarding scope, goals, feedback, and tools.

## Scope
It can be tempting to set lofty goals for code reviews, but in reality, people just can't concentrate too deeply or for too long!

Widely-recommended practices are to:
* Make small PRs which are easier to review.
* Have a checklist covering what a PR should contain and accomplish
* Limit code reviews to 60 minutes or less
* Review **at most** 500 lines of code per hour

Reviewing more code than recommended here can lead to fatigue and the temptation
to just say "looks good to me".  Code review requires concentrated, thoughtful
feedback.

## Goals
Reviewers should have a clear sense of what feedback is being solicited. 
Some companies have general guidelines for what code-reviewers should be looking for in the code they review

If you are seeking specific kinds of feedback, communicate that to your reviewers!
In the absence of this, projects should include general code-review goals and guidelines for reviewers to reference

If there is other background knowledge necessary for an effective code-review, provide it to the reviewers.
This can be included or referenced in comments, provided in documentation, etc.

> ## A Checklist from Google
> [Google's engineering practices](https://google.github.io/eng-practices/review/)  recommend code reviews should look at: 
> * **Design**:  Is the code well-designed and appropriate for your system?
> * **Functionality**:  Does the code behave as the author likely intended? Is the way the code behaves good for its users?
> * **Tests**:  Does the code have correct and well-designed automated tests?
> * **Naming**:  Did developer choose clear names for variables, classes, methods, etc.?
> * **Comments**:  Are the comments clear and useful?
> * **Style**:  Does the code follow our style guides?
> * **Documentation**:  Did the developer also update relevant documentation?
{: .callout}



## Feedback
The highest priority should be placed on providing courteous and respectful feedback on another person's work.
This is a critical skill to develop, and should never be compromised, even in jest.

When providing feedback:
* Use objective, constructive, neutral language
* Critique the code, not the programmer
* Avoid theatrics and absolute judgments, like "This is the worst code I've ever seen!"  "I have no idea how this ever worked in the first place."
* Ask questions and seek understanding, rather than rendering judgment
    * The author has thought about the problem a lot more than you have, and they may have reasons for what they did – even if it's still misguided in the end
* Explain your concerns clearly and completely
    * Try to explain your reasoning for issues you point out, e.g. inputs that would trigger undesirable behavior, alternate approaches that may be more efficient, etc.

Programmers are often highly opinionated. Creating software feels personal; you
are problem solving and translating that in the best way you can.  Receiving
criticism can seem like someone challenging how you think!  Remember, that
there are many good ways to solve any given problem – including ways that you
personally wouldn't use: different ways of naming variables, writing
loops, structuring functions, etc.  When providing feedback, indicate whether
your feedback is about a serious issue (e.g. correctness, security, safety),
versus merely you expressing an opinion or suggestion.

> ## A Solution for Nitpicks
> Several companies specify that review feedback should be prefixed with “Nit:  …” if you are merely being nitpicky.
> 
> Reviewer opinions and nitpicks are free to be ignored by the author!
{: .callout}


## Tools
Some goals of code reviews are to check coding style, and to identify bugs, anti-patterns and language abuses. 
The good news is that there are *static analysis tools* to help supplement the code-review process and remove some of the more laborious tasks such as:
* Verify (or apply) the team’s coding standards
* Flag common bugs and language anti-patterns

These tools eliminate a whole range of issues that would otherwise need to be addressed in the code review.
Where possible, codify your project style and set up CI/CD or precommit to
automatically check or correct any issues prior to code review.  These are similar
to using a built-in spell checker, you don't want to waste time looking up spelling
in a dictionary!
Static analysis tools allow the review to focus on higher-level concerns - how
the code works, how it benefits the project, higher-level structural/design
issues, etc.

> ## Examples of Static Analysis Tools for Python
> * [Flake8](https://flake8.pycqa.org/en/latest/) - coding style and linting
> * [Pylint](https://pylint.org/) - coding style and linting
> * [Black](https://black.readthedocs.io/en/stable/) - coding style enforcement
> * [mypy](http://mypy-lang.org/) - check Python code against type annotations
> * [ruff](https://docs.astral.sh/ruff/) - a fast linter and formatter
{: .callout}
{% include links.md %}

> ## Additional Resources
> These three resources are incredibly valuable and should be read by everyone:
> * Google - [Code Review Developer Guide](https://google.github.io/eng-practices/review/)
>   * Very detailed guidelines for all participants of code reviews
>   * "How to do a code review document" is very good for mechanics of reviews
> * Palantir – [Code Review Best Practices](https://blog.palantir.com/code-review-best-practices-19e02780015f)
>   * An excellent and detailed guide about code reviews
> * StackOverflow - [How to Make Good Code Reviews Better](https://stackoverflow.blog/2019/09/30/how-to-make-good-code-reviews-better/)
> These are also excellent articles:
> * Atlassian – [Why code reviews matter (and actually save time!)](https://www.atlassian.com/agile/software-development/code-reviews)
>   * Discusses code reviews in the context of agile development methodologies
> * Perforce – [9 Best Practices for Code Reviews](https://www.perforce.com/blog/qac/9-best-practices-for-code-review)
> * [code-review.org](code-review.org)
>   * A thorough tutorial on how to perform code reviews in github
{: .callout}
{% include links.md %}
