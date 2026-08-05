---
title: "Reduce Mailbox Size in Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/356680/reduce-mailbox-size-in-exchange-2019
question_id: 356680
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Reduce Mailbox Size in Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/356680/reduce-mailbox-size-in-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have been assigned an ask to reduce the mailbox size in my Exchange organization and would like to know what are the native options available. I have also checked the Quota option but not sure on the impact of changing it.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-15*

Hi @Exchange_Newbie      

Are suggestions above helpful to your issue?    

I will attach some links below which will help you have a better understanding about the points above.    

1.In-Place Archiving in Exchange Server    

2. Why we need to create a new database and move the existing mailboxes to the new place: Using PowerShell to Get Mailbox Database Size and Available New Mailbox Space     

3. From outlook client side: Reduce the size of your mailbox and Outlook Data Files (.pst and .ost)    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-04-14*

If you are looking for reducing the size of the mailbox database itself, you can plan for creating a new database and move the existing mailboxes to the new database and delete the old database. This will remove whitespaces in your existing database and saves some space

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-15*

Thank you all for your suggestions. I will sure discuss with the management on the exact requirement and take further actions as suggested.
