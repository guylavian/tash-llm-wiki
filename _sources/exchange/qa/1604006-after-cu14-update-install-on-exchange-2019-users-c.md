---
title: "After CU14 update install on exchange 2019, users can not change the expired passwords"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1604006/after-cu14-update-install-on-exchange-2019-users-c
question_id: 1604006
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 2
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# After CU14 update install on exchange 2019, users can not change the expired passwords

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1604006/after-cu14-update-install-on-exchange-2019-users-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After CU14 update install on exchange 2019, users can not change the expired passwords, Change password screen appears where you put the current and new passwords and then "something went wrong" appears. Please help

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-04-01*

Hi @Hassan Waheed  and @Jaroslav Mixa  ,

Just wondering are you in a multi-forest topology? If so, please go through the article below and make sure the setting override mentioned there has been configured.  

Users in account forest can’t change expired password in OWA in multi-forest Exchange deployments after installing August 2023 SU

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-28*

We have the same issue. 

We have a hybrid environment and some users cannot log in or change passwords using OWA. The login window appears again and again. 

It seems it happens mainly to external users outside of the domain. 

We cleared the browser cache, saved passwords, and tried an incognito window. We tested Chrome and Firefox. 

It started after the last exchange upgrade.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-01*

Hi @Hassan Waheed  ,

 Please run the Exchange PowerShell below to check if there's an OWA mailbox policy applied to the affected user:

```
Get-CasMailbox  | fl owamailboxpolicy
```

If the result shows there's no OWA mailbox policy applied, go to EAC > Servers > Virtual Directories > Features, make sure the checkbox of "Change password" is selected:  

In case the above has already been checked but the issue remains, please go EAC > Permissions > Outlook Web App policies, select the policy you want to use, click features, make sure the checkbox of the "Change password" is selected:

Apply the owa mailbox policy to the affected user:

```
Set-CASMailbox -Identity  -OwaMailboxPolicy 
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
