---
title: "Exchange Online Transport Rule to forward mails to external domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168552/exchange-online-transport-rule-to-forward-mails-to
question_id: 168552
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Exchange Online Transport Rule to forward mails to external domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168552/exchange-online-transport-rule-to-forward-mails-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,  

i have a requirement to redirect mails coming in for specific users to reroute/forward onto a an external domain.  

eg:  

******@CompanyA.com forward to ******@CompanyA.com  

so the script should run as follows :  

IF recipient is eligible (maybe managed by a group)  

THEN modify recipient address to delete everything after "@" and append "CompanyB.com"  

not sure if this is even possible but thought it's worth asking.  

Thanks!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2020-11-19*

Example:    

You would need to create a mail enabled contact for the external user.    

What you can't do, is create a rule to dynamically modify the address or anything like that. The rule would have to exist for each possible recipient and external contact.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-20*

@James V       

Agree with AndyDavid and add more suggestions.     

You also can run the message trace, and check the message events for more error information to know why the message is blocked. For your reference: Run a message trace in the classic EAC.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
