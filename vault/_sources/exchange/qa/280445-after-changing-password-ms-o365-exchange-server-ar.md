---
title: "After changing password MS / O365 Exchange server are locking my on premise account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/280445/after-changing-password-ms-o365-exchange-server-ar
question_id: 280445
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# After changing password MS / O365 Exchange server are locking my on premise account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/280445/after-changing-password-ms-o365-exchange-server-ar (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have changed my service admin account password.  

Setup Exchange server is hybrid.  

After password change,  Service account is  lock out immediately after account is unlocked…  

Event ID : 4740  

TargetUserName : My service account  

TargetDomainName :  Random MS servers : VI1P195MB0141, VI1P195MB0655, VI1P195MB0463, PR3P195MB1008, VI1P195MB0256, AM9P195MB0919  

Migration point run under different account. But hybrid was setup with my service account. Exchnage server is 2013.  

Br,  

Borut

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-22*

@Borut Puhar       

I think this phenomenon is caused by hybrid configuration using old account information to verify connection, then account blocked by wrong password. So, I would suggest you create a dedicated admin account for Exchange hybrid, then use this account to rerun HCW.    

You can also check whether there are other event logs that record why the account was blocked.     

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
