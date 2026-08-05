---
title: "Hybrid Exchange Public Folder Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1035167/hybrid-exchange-public-folder-issue
question_id: 1035167
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Hybrid Exchange Public Folder Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1035167/hybrid-exchange-public-folder-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Having just migrated some system mailboxes from Exchange to Exchange Online, I've been informed that a certain on prem public folder has stopped receiving email.    

Upon investigation I found that the mail flow for this public folder was as follows:    

SystemMBX (forwarder to DL) > DL (PublicFolder member of DL) > Public Folder    

Since the SystemMBX was migrated I noted two things:     

the forwarder on the mbx was not preserved  (This was later found to be expected behaviour, the forwarder reinstated.)    

The PublicFolder does not exist as a member of the DL  when viewed in Exchange online (hence the reason the PF is no longer receiving mail)    

Up to this point in the migration I have had no major public folder related issues.    

Running the Sync-ModernMailPublicFolders.ps1 from Microsoft at the start of the project, and then regularly to sync any PF updates has worked so far in preventing any issues.    

Checking the latest sync log shows the PF in question has synced successfully    

Checking the PF exists in Exchange Online (Get-MailPublicFolder) also shows the public folder exists.    

So I'm a little confused as to why the EO version of the DL doesn't display the PF as a member (unless this is by design?)    

More importantly why has mail flow stopped to the PF since the source SytemMBX was migrated?    

Any ideas please?    

Thanks

## Answers

_No answers on this thread._
