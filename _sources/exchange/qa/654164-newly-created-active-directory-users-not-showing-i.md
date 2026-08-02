---
title: "Newly created Active Directory Users not showing in Exchange Admin Center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/654164/newly-created-active-directory-users-not-showing-i
question_id: 654164
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Newly created Active Directory Users not showing in Exchange Admin Center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/654164/newly-created-active-directory-users-not-showing-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I create around 100 users in the active directory, but they did not appear in Exchange Admin Center.  

We have a hybrid environment with an exchange on-premises and Office 365.  

I was able to assign all the users the proper license, but I also want them on the exchange server.  

Any idea why they are not showing up?

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2021-12-08*

Based on my test, if you create a AD user and do not enable it as a mailbox, after forcing a AAD sync, you could see that user in O365 portal. But it is neither an Exchange on-premise recipient type nor an Exchange online recipient type. So when running Get-Recipient or Get-RemoteMailbox, you could find it nowhere.  

Connect to Exchange online Powershell, run enable-mailbox towards those user accounts and you could see them in Exchange Online EAC after a while.  

Please mark as "Accept the answer" if the above steps helps you. Your suggestion will help others also !

## Answer (community) — community member

*upvotes: 1 · updated: 2021-12-08*

@Khalid Said Mohammed Al Shukaili      

Do you mean that you create AD accounts in local AD, then sync them to Azure AD, after that assign license to those accounts?    

If so, it is an expected behavior that you cannot see those mailboxes on Exchange on-premises.    

If you want to see those mailboxes on Exchange on-premises admin center, you will need to use command below to enable remote mailboxes for those accounts:    

```
Enable-RemoteMailbox "ToOnlineUser" -RemoteRoutingAddress "******@OnlineDomain.mail.onmicrosoft.com"
```

    

Then you will could see this mailbox show are Office 365 mailbox on Exchange on-premises admin center.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-12-07*

What is "proper" license, Exchange Online one? If you have provisioned a mailbox for them by creating a user object and assigning an Exchange Online license, you will not see them listed as (remote) mailboxes in your on-premises EAC. Instead, you should either provision a remote mailbox, or create the mailbox on-prem first, then migrate it to Exchange Online. Read here for example: https://techcommunity.microsoft.com/t5/exchange-team-blog/on-provisioning-mailboxes-in-exchange-online-when-in-hybrid/ba-p/1406335
