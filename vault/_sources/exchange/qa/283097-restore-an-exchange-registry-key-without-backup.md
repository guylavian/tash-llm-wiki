---
title: "Restore an Exchange registry key without backup"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/283097/restore-an-exchange-registry-key-without-backup
question_id: 283097
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Restore an Exchange registry key without backup

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/283097/restore-an-exchange-registry-key-without-backup (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day all, The exchange Frontend service stops running and all my effort to get it started proved abortive. In the process, I accidentally deleted the MSExchangeFrontendTransport service registry key in the system registry. Please, how can I get it back? I have no backup and no restore point. I need help urgently. Thanks. Boniface

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-24*

Yes.  

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MSExchangeFrontendTransport.  

It is the folder in the path above (MSExchangeFrontendTransport) that was deleted accidentally.  

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-23*

Hi @Boniface Blue-Jack   ,    

Good day!    

Do you remember which registry key you deleted? If you have a same version Exchange, i think you could manually create one with the same Keys and Values.    

If not, you can try using the recovery mode to restore Exchange server:    

```
E:\Setup.exe /IAcceptExchangeServerLicenseTerms /Mode:RecoverServer
```

More about the recovery mode: Recover a Lost Exchange Server    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
