---
title: "Code Reviews"
teaching: 0
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "First learning objective. (FIXME)"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

## Code Reviews
**Code reviews**, or **peer (code) reviews** are a practice where someone other than the code’s author reads and reviews the code. The author is often involved in the review, and answers any questions that the reviewer has.

These are sometimes *formal inspections* of a portion of the code and may be part of an acceptance process that the project requires (e.g. for safety-critical software). Code reviews tend to be a more heavy-weight process with specific criteria to evaluate.

More commonly, code-reviews are *change-based* code reviews, e.g. “Every new feature or bug-fix must be reviewed before it is incorporated into the main-line of development.”

This is the process that is adopted by most large software companies, and tends to be lighter-weight, akin to a “**code walk-through**” or “**read-through**."

## Benefits of Code Reviews
Benefits of formalized code reviews (inspections) is very well documented.

From Code Complete, 2ed. pp.480-481

* IBM found that each hour of inspection prevented about 100 hours of related work (testing and defect correction) (Holland 1999)
* Hewlett-Packard reported that its inspection program saved an estimated $21.5 million per year (Grady and Van Slack 1994)
* A study of large programs found that each hour spent on inspections avoided an average of 33 hours of maintenance work and that inspections were up to 20 times more efficient than testing (Russell 1991)
* A group of 11 programs were developed by the same group of people, and all were released to production.  The first five were developed without reviews and averaged 4.5 errors per 100 lines of code.  The other six were inspected and averaged only 0.82 errors per 100 lines of code.  Reviews cut the errors by over 80% (Freedman and Weinberg 1990).
* [*and many many more...*]

While less-formal code walk-throughs/read-throughs vary much more widely in their benefits, they can still achieve many of the knowledge-sharing, team-building and defect-detection benefits, but not as reliably as formal reviews.

The main differences are:
* The code’s author tends to lead the walk-through, as opposed to a separate moderator in an inspection.  Read-throughs are self-driven by the reviewer.
* Reviewers are varied in their commitment to providing a thorough and detailed assessment of the code.
* Defects in the code may or may not be formally recorded as action-items to address, with a follow-up to see if they have been corrected

Taking care not to lose the rigor of the review process is essential to achieving all the benefits to be had. As usual with life, you get out of it what you put into it.

{% include links.md %}