---
title: "Exchange 2013 cannot upgrade from CU9 to CU23 without the CU9 install media"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/301682/exchange-2013-cannot-upgrade-from-cu9-to-cu23-with
question_id: 301682
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2013 cannot upgrade from CU9 to CU23 without the CU9 install media

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/301682/exchange-2013-cannot-upgrade-from-cu9-to-cu23-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have inherited an Exchange 2013 CU9 server that urgently needs to be upgraded to CU23 for obvious reasons. I have already done this to another server in the exact same scenario (this one's partner in a DAG) and no issues, however this one is prompting for the CU9 install media in order to process the "uninstalling" stage. It's looking in C:\Temp\CU9, which does not exist, and the log reports  

[ERROR] Couldn't remove product with code 4934d1ea-be46-48b1-8847-f1af20e892c1. The installation source for this product is not available. Verify that the source exists and that you can access it. Error code is 1612.  

The other server, which upgraded fine, does NOT apear to have had the CU9 install media anywhere on it so I can't imagine why this one in particular must have it. Is there a way to bypass this, to force CU23 to perform the removal, or a way I can get my hands on the CU9 install media?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-06*

Some progress - I found the registry was looking for a particular MSI file in c:\windows\installer that does not exist, which is why it's now looking for the copy in c:\temp\cu9.  

I found the equivalent copy in a backup of the other cu9 server, renamed the MSI file and copied it across and the process moved all the way up to Installing Languages.  

At which point it started asking for individual language installers... all FIFTY SIX of them.  

Now I don't know if the installer will fail because I have to somehow deal with all of them before running it again.
