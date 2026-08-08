---
title: "Cannot uninstall Exchange Server 2013 - arbitration mailbox can't be removed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/285361/cannot-uninstall-exchange-server-2013-arbitration
question_id: 285361
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Cannot uninstall Exchange Server 2013 - arbitration mailbox can't be removed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/285361/cannot-uninstall-exchange-server-2013-arbitration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange Server 2019 install where all mailboxes have been migrated over from a previous Exchange 2013 server.  

Cannot uninstall Exchange 2013 because of "FederatedEmail..." arbitration mailbox still in the last database on the 2013 server. The 2013 server doesn't "appear" to be needed as we have run on the 2019 server for over 2 days with no issues while the 2013 server was completely shut down.  

I have reviewed the other similar threads but none of the suggestions have worked to move (or remove) this arbitration mailbox. I don't see a "FederatedEmail..." arbitration mailbox on the new server. We are a single domain, single Exchange server, onsite configuration. Do we even need a "FederatedEmail..." mailbox?  

I would like to gracefully uninstall the 2013 server so all the info is removed from Active Directory but the uninstall won't proceed because of this one mailbox.  

Is there another way to force removal of the old mail server from Active Directory without jeopardizing the live 2019 Exchange Server?  

What would happen if I just unjoin the 2013 Server from the domain and then shut it down permanently?  

All suggestions are welcomed and appreciated.

## Answers

_No answers on this thread._
