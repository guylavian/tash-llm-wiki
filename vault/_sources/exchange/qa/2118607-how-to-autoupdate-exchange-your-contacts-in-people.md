---
title: "How to autoupdate Exchange Your Contacts in People tab?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118607/how-to-autoupdate-exchange-your-contacts-in-people
question_id: 2118607
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to autoupdate Exchange Your Contacts in People tab?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118607/how-to-autoupdate-exchange-your-contacts-in-people (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, 

in our company we use Exchange Online. Let's assume in the number of 500 users.

Problem:

How to autoupdate/sync all active users to "Your contacts" bookmark in https://outlook.office.com/people/

Best option would be to simply synchronize Global address list to "Your contacts".

What I already performed:

-  I'm able to manually copy everyone in Outlook Classic on Windows from GAL to "Your Contacts" but its not way to do for a whole company (also its not autoupdating when someone new is hired).

-  Ready-made solutions on the market cost too much so for "simple" synchronization.

-  I tried (and am still trying) to achieve this through a powershell script, MSGraph and AzureAP that completes the contact list - but here there is the issue of automation at least every week, updating the entire list in all users, without duplication of contact at each iteration etc. 

Why we do it:

When we have all users synced to ‘Your Contacts’ for everyone, we can use the mobile Outlook app on Android as a phone book to identify exactly who from the company is calling us.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-14*

Hi,@Szymon Miotk

Thanks for posting your question in the Microsoft Q&A forum.Based on your description, you want to automatically update or synchronize all active users to Your Contacts in Outlook Online.

I consulted with the Outlook engineers, and currently Outlook only supports the ability to automatically update already existing contacts when their information is changed.You can refer to this link:https://techcommunity.microsoft.com/blog/microsoft_365blog/new-improved-contacts-in-outlook-on-the-web/3639773

 For the time being, it is not possible to fulfill your request.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
