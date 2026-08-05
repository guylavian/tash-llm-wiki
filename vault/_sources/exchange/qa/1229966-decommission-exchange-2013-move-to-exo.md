---
title: "Decommission Exchange 2013 - Move to EXO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1229966/decommission-exchange-2013-move-to-exo
question_id: 1229966
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Decommission Exchange 2013 - Move to EXO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1229966/decommission-exchange-2013-move-to-exo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am reaching out to the community as Microsoft has ended support two days ago for any help / guidance with Exchange Server 2013.  We are looking to remove all the local Exchange servers (we have server roles for CAS and MBX).  From what I've already read through on other threads, is that we need to remove the DAG and any associated mailboxes that exist on-prem.  However, I don't have clarity on if having CAS and MBX not on the same server poses a problem from the MS comment "Do not uninstall the last server" (https://learn.microsoft.com/en-us/exchange/manage-hybrid-exchange-recipients-with-management-tools).  Does it matter which server is the "last" server part of Exchange.  There is another server that I plan to have for recipient management (Exchange Server 2019 Tools).

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-04-14*

Hi @Brandon Epler  ,

However, I don't have clarity on if having CAS and MBX not on the same server poses a problem from the MS comment "Do not uninstall the last server"  (https://learn.microsoft.com/en-us/exchange/manage-hybrid-exchange-recipients-with-management-tools). Does it matter which server is the "last" server part of Exchange

Per my understanding, the method in the document is not applicable to your scenario, as one of its requirements is "You're running only one on-premises Exchange server and only for recipient management.":

Given this and also considering that Exchange 2013 has reached the end of support, personally I'd suggest migrating to Exchange 2019 first and then use the new method in the aforementioned document to shut down the last Exchange server.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
