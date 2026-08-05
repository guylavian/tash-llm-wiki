---
title: "Microsoft Exchange 2019 (Incomplete Setup)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155379/microsoft-exchange-2019-incomplete-setup
question_id: 155379
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Microsoft Exchange 2019 (Incomplete Setup)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155379/microsoft-exchange-2019-incomplete-setup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Experts,  

I have deployed a second instance for Exchange 2019 which was successful. I installed a third instance and it failed at Transport Service during installation.   

I tried restarting the setup, but it stops at same place. My Exchange ECP is showing that Server in the list with "NONE" role assigned.  

i need to remove this server from the list.  

Kindly Help.  

Regards

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-09*

@Raheel Zubair      

Hi,    

Have you tried the following command on the third instance to uninstall the server?    

```
Setup.exe /IAcceptExchangeServerLicenseTerms /mode:Uninstall
```

Does it work fine or will you get some error messages?    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
