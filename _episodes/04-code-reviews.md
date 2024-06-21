---
title: "Code Reviews"
teaching: 0
exercises: 0
questions:
- What are some benefits of formalized code reviews?
- What is the difference between a code read-through and walk-through?
- What is your biggest hurdle to starting code reviews?
objectives:
- Learn why code reviews are important.
- Identify and address challenges when beginning code review.
keypoints:
- Code review saves time, money and reduces error.  The more formal the review, the bigger the savings.
- During a code walk-through, the author is present to discuss the changes.  A read-through does not require the author during the review.
---

## Code Reviews
**Code reviews**, or **peer (code) reviews** are a practice where someone other
than the code’s author reads and reviews the code. The author is often involved
in the review, and answers any questions that the reviewer has.

These are sometimes *formal inspections* of a portion of the code and may be
part of an acceptance process that the project requires (e.g. for
safety-critical software). Code reviews tend to be a more heavy-weight process
with specific criteria to evaluate.

More commonly, code-reviews are *change-based* code reviews, e.g. “Every new
feature or bug-fix must be reviewed before it is incorporated into the
main-line of development.”

This is the process that is adopted by most large software companies, and tends
to be lighter-weight, akin to a “**code walk-through**” or “**read-through**."

## Benefits of Code Reviews
Benefits of formalized code reviews (inspections) are very well documented.

From Code Complete, 2ed. pp.480-481

* IBM found that each hour of inspection prevented about 100 hours of related work (testing and defect correction) (Holland 1999)
* Hewlett-Packard reported that its inspection program saved an estimated $21.5 million per year (Grady and Van Slack 1994)
* A study of large programs found that each hour spent on inspections avoided an average of 33 hours of maintenance work and that inspections were up to 20 times more efficient than testing (Russell 1991)
* A group of 11 programs were developed by the same group of people, and all were released to production.  The first five were developed without reviews and averaged 4.5 errors per 100 lines of code.  The other six were inspected and averaged only 0.82 errors per 100 lines of code.  Reviews cut the errors by over 80% (Freedman and Weinberg 1990).
* [*and many many more...*]

While less-formal code walk-throughs/read-throughs vary much more widely in
their benefits, they can still achieve many of the knowledge-sharing,
team-building and defect-detection benefits, but not as reliably as formal
reviews.

The main differences are:
* The code’s author tends to lead the walk-through, as opposed to a separate moderator in an inspection.  Read-throughs are self-driven by the reviewer.
* Reviewers are varied in their commitment to providing a thorough and detailed assessment of the code.
* Defects in the code may or may not be formally recorded as action-items to address, with a follow-up to see if they have been corrected

Taking care not to lose the rigor of the review process is essential to achieving all the benefits to be had. As usual with life, you get out of it what you put into it.

## Challenges of Code Reviews
From discussions with other RSEs, there is a realization that code reviews are
beneficial but difficult to implement. Maybe you are sold and want to start adding
code reviews to your PRs.  You are able and willing to review, but you need someone
else to review your code! If you work in a small (perhaps solo) development
team, who will review your code and how can you help them get started?

### I work alone or with researchers/novice developers
There is a certain asymmetry with code reviews when you are the expert and decide
to add in code reviews.  You can review PRs from others but not your own work!
It seems intractable to tell someone else, hey you have to look at my code and
catch all the bugs.

However, you don't *need* someone else to review your code, you can perform
self reviews.  Similar to copy editing, you (hopefully) look over your own
writing before submitting it for grading or your PI.  Self reviews are usually
not better than peer reviews, but are vastly better than nothing.  For best
results, let the PR sit for a day or two before performing your review.  That
will give you fresh eyes.

Also, don't underestimate novice developers or even non coders to review code.
If you have a stakeholder that's willing to click a few buttons on github, they
may catch logical or domain specific errors.  You should strive to have your
code readable enough that a novice can follow the algorithm!

### I struggle with all the tools!
Remember the separation of mechanics and methods. The method of code review is
the act of critically evaluating a section of code and providing feedback in a
courteous way.  We have some practice doing this with pair programming.  Here
we will dig into the mechanics: what are you reviewing and where do you write your
comments.  The practice of evaluating code is much more difficult than knowing
which buttons to press on github!

### My project requires a lot of domain knowledge, I don't think anyone else can give me feedback
Even if someone doesn't understand every line of your code, they can still
provide a different view of the code.  Maybe your variable names are unintelligible
to someone without your domain knowledge and they don't have to be. Maybe you
forgot to include a license or your functions are too long or complex.  None
of these require deep knowledge of your domain and can be helpful.

Also note that if your code can't be understood by anyone but you, it may require
some refactoring to improve readability.  Open source software has to be approachable
to would-be contributors.  A non-expert reviewer can help identify places a
general developer will have trouble following.

{% include links.md %}
