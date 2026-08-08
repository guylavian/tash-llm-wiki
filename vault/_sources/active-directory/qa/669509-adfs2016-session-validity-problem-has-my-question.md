---
title: "Adfs2016 session validity problem, has my question expired?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/669509/adfs2016-session-validity-problem-has-my-question
question_id: 669509
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Adfs2016 session validity problem, has my question expired?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/669509/adfs2016-session-validity-problem-has-my-question (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is my previous question  

This problem often occurs because users often log in long after the login page  

The error page is very unfriendly and gives users a lot of confusion  

Do we have any way to solve it?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-24*

The question was addressed, like you pointed out, in https://learn.microsoft.com/en-us/answers/questions/411768/how-long-does-it-take-to-complete-the-login-for-ad.html. The answer was accepted. This timeout cannot be change.    

Then I asked what is the scenario in which a user takes more than 10 minutes to actually go through the process. That's a real question I am asking, that you have not yet answered. Because I am curious and maybe if this scenario is broad enough, we could try to argue for a Design Change Resquest of the product (although that's a long shot). This was left unanswered (or at best partially answered) here: https://learn.microsoft.com/en-us/answers/questions/660821/adfs2016-session-validity.html.    

The error message can be customized to some extent using some JavaScript. The issue with that customization is that you cannot tell if the error is due to the timeout or for other reasons in the page. So the JavaScript can't know it either. Whatever customization would have to be very generic to avoid creating issues with other error scenarios.    

You can maybe address the issue by instructing the user to be carefull (if that's possible since like I said - multiple times - I don't know what is the reason for that wait).
