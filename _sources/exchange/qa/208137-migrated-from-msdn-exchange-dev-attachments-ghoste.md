---
title: "[Migrated from MSDN Exchange Dev]  Attachments Ghosted for one user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/208137/migrated-from-msdn-exchange-dev-attachments-ghoste
question_id: 208137
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]  Attachments Ghosted for one user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/208137/migrated-from-msdn-exchange-dev-attachments-ghoste (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/7d542f68-d1bd-43bb-93fc-56dee7b24cda/attachments-ghosted-for-one-user?forum=exchangesvrdevelopment  

I have a user who has emails with attachments come in that are ghosted.  If she forwards the same email with the attachment to herself she can then open the attachment.  The environment is Exchange 2013, her client is Outlook 2016.  I have tried rebuilding her profile but to no avail.  Any help would be greatly appreciated, thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-23*

Do you mean the attachment "disappeared" when sending to her clients? Not pretty sure about you said "ghosted".    

Which version Outlook is your user using? Can she reproduce the issue with OWA? Check the message in Sent Items, can the attachment be seen there?    

Does it only happen when specific sender sending to specific clients?    

When running message tracking, check if the value "totalsize", does it include the size of attachment?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
