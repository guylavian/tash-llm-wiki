---
title: "Exchange 2013 KB5000871 installed but no files updated"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/326420/exchange-2013-kb5000871-installed-but-no-files-upd
question_id: 326420
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 KB5000871 installed but no files updated

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/326420/exchange-2013-kb5000871-installed-but-no-files-upd (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, We have 2 separate Active Directory environments - both are in isolated networks and both have an Exchange 2013 server (CU23). I've tried installing the "Zero Day" patch, KB5000871, which will go through and stop/start services then complete. There is no prompt to restart the server and none of the files are updated to the version that is stated in the "Files List.xls. Each attempt to install I have opened the command prompt as Administrator and executed the file via command line. This appears to have the same symptoms as when just double-clicking the file (not via Admin Command Prompt) except there are no issues with OWA or ECP. When checking the Windows Update - Update History it lists this update as installed. When we scan the server it states that the update is still needed (Nessus). What am I missing? I've looked through event logs but cannot find anything related to the update. Thanks!

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-23*

Thanks for the response. I had our security team scan again and this time the update applied (or maybe it was the scanning plug-ins) so it looks like the update did install this time.  

John
