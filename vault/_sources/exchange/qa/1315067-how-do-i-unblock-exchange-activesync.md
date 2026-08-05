---
title: "How do I unblock Exchange ActiveSync?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1315067/how-do-i-unblock-exchange-activesync
question_id: 1315067
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How do I unblock Exchange ActiveSync?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1315067/how-do-i-unblock-exchange-activesync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I added an email account that utilizes Exchange ActiveSync and my account has been blocked for two days. The notice states that I don’t have to do anything. Content will automatically download as soon as access is granted by your administer. How long does this take?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-06-22*

Hi @Guy Edwards  ,

By research, this is usually caused by the user in question having administrator rights at some point, which changes the security inheritance on their account. You can try the following steps:

-  Open Active Directory Users and Computers.  

-  Click on View and Select Advanced Features  

-  Select a mailbox (User Account) that isn’t working with Active Sync, double click on the account.  

-  Click the Security Tab and then the Advanced button.  

-  Highlight Exchange Servers and check the Include inheritable permissions from this object's parent, enable inheritance.  

-  Click OK to save the settings.

If the above do not work, please check your active sync access rules and provide more details.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
