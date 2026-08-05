---
title: "[Migrated from MSDN Exchange Dev] Exchange 2010"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/130517/migrated-from-msdn-exchange-dev-exchange-2010
question_id: 130517
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] Exchange 2010

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/130517/migrated-from-msdn-exchange-dev-exchange-2010 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post:  https://social.msdn.microsoft.com/Forums/office/en-US/15d73778-a560-46aa-9917-be33becda96f/exchange-2010?forum=exchangesvrdevelopment  

Hi,  

i have a strange problem. Terminal server / Outlook 2010 / Exchange 2010.  

Some users get the message at the OOF: your automatic reply settings cannot be displayed  

But it works for 99% of users.  

Now the strange thing: If I take a user where it works and put User A's mailbox in Outlook, I can activate the Out of Office agent.  

No matter which mailbox I put in with user A, it doesn't work. So it must have something to do with the Windows user. Anyone have an idea?  

User A can access the Autoddiscover.xml, the login window also appears ...

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-19*

What's the detailed version of your Exchange 2010? You can check with the following command:    

```
Get-Command ExSetup | ForEach {$_.FileVersionInfo}
```

Do you mean when you add other mailbox for the existing profile created for user A (user A is the default account), OOF doesn't work?    

Do you add other accounts from File > Add account, or expand other mailbox with full access?    

Does the error message display when you set OOF for user A (the default account) or other added accounts?    

Try to create a new Outlook profile for user A, then add other accounts again. If the issue still occurs with the new profile, please post the screenshot of the error message, and don't forget to cover your personal information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
