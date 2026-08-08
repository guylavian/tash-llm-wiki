---
title: "Update exchanges user's alias without changing others field"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/352181/update-exchanges-users-alias-without-changing-othe
question_id: 352181
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Update exchanges user's alias without changing others field

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/352181/update-exchanges-users-alias-without-changing-othe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

If I update my exchanges user's alias under the general tab in my exchange admin center. I found out it will automatically updated the email address as well under the general tab and the SMTP address under the email address tab as well.It also updated the proxyAddress attribute in AD since its linked to the exchanges email address(SMTP address). May I know whether this is the default behavior of how the exchange server works ?  

As I know so far, the exchange server will use alias for searching for the correct email address,so if you update the alias field in exchanges server for that particular of user, email address(SMTP) in exchanges and proxyAddress attribute in AD will updated automatically.  

So may i know if there any method that i can update the alias only without changing any others value in exchange and AD ? I am not sure whether is there any method on this because I saw that the alias field in exchanges admin center is a mandatory field

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-12*

@Harry Kane      

When we create a new mailbox, we can know that email address prefix and alias use the same value:    

    

    

So, it is an expected behavior that a new email address generated when we change the alias for mailbox.    

If you doesn't want to let Exchange change the email address, you will need to prevent this mailbox from Email address policy as AndyDavid said.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-10*

If your email address policy is based on alias, then that is expected:    

https://learn.microsoft.com/en-us/exchange/email-addresses-and-address-books/email-address-policies/email-address-policies?view=exchserver-2019    

If you do not want to apply that change to a specific mailbox, uncheck this option:
