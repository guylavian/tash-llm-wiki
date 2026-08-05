---
title: "Active Directory Multiple Failed Login Attempts by same user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1229786/active-directory-multiple-failed-login-attempts-by
question_id: 1229786
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory Multiple Failed Login Attempts by same user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1229786/active-directory-multiple-failed-login-attempts-by (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In my organization, a single user logs-in multiple systems ( for example, keep it a count of 5). After the password expiry, the user changes the password with the help of the IT team and logs-in in one system.  

After this incident, the remaining 4 systems which the user previously logged-in session trigger bad password attempts continuously, like 5-10 bad password attempts for each second.
Now my question is: Will the account get locked out for these bad password attempts?
Below is my account lockout policy
Lockout threshold:5
Lockout duration (minutes): 30
Lockout observation window (minutes):30

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-14*

Hello Vijay Radhakrishnan,
Thank you for posting in our Q&A forum.  

Q: Now my question is: Will the account get locked out for these bad password attempts?  

A: Yes, the account will get locked out for these bad password attempts.  

I think you had better remove or delete wrong credential on other system if there are continuous failed login attempts.  

Hope the information above is helpful.
If you have any question or concern, please feel free to let us know.
Best Regards,  

Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.
