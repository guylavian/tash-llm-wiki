---
title: "NTLM authentication not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/54481/ntlm-authentication-not-working
question_id: 54481
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# NTLM authentication not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/54481/ntlm-authentication-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings,  

NTLM authentication not working in OnPrem 2016 Exchange. But Basic authentication is working.  

With Regards,  

Anoop Rayas.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-07-30*

You are running 2016 CU2. That is more than 4 years old! That needs to be upgraded to CU17 ASAP. You are running extremely old and unsafe code.   

You should upgrade first and see if the issue continues.   

Not sure what this means" NTLM authentication is failing for incoming, where outgoing is successful."

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-07-30*

Thanks Joy,    

NTLM authentication is failing for incoming, where outgoing is successful. Please find the attachment.    

    

With Regards,    

Anoop Rayas.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-30*

Could you please provide more information about your issue:    

How did you set the NTLM authentication? Did you get any error information after setting this?    

Please also refer to this article to get more information: Outlook Anywhere Basic vs. NTLM Authentication explained    

And the usage and parameter about using the command: Set-OutlookAnywhere
