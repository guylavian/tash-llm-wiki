---
title: "Exchange 2013 Offline Address Book not updating on the server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/121773/exchange-2013-offline-address-book-not-updating-on
question_id: 121773
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2013 Offline Address Book not updating on the server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/121773/exchange-2013-offline-address-book-not-updating-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have only recently started looking at Outlook Cached mode and it has come to light that the Offline address book is not working properly. Clients cannot download it manually using Outlook (Get error 0x80190194). On the 4 Exchange servers the contents of the C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess\OAB\<UNIQUIE GUID> hasn't been updated since Jan/Feb 2020 on 2 servers and Sept 2020 on the other 2 servers.

If I run the Update-OfflineAddressbook <AddressBook> command on the Exchange server there is no error, but I don't see any events in the application log either.

It seems broke on the Exchange servers but I am stuck as to what to do.

Regards,

Matt

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-10-15*

Hi AndyDavid,  

Sorry for not replying sooner.  

I followed your notes and created a new OAB and this worked.  I then went back to the original OAB I was having problems with and tat then worked ok.  

So I'm not sure what happened but it definitely fixed the issue.  

I was also confused about where the OAB files should lie on which Exchange 2013 server.  I assumed that all 4 in our site would have the same files/version and I have since found out that it depends on the Arbitration mailbox responsible for OAB generation and where the mailbox database resides.  We have only one site and one DAG and so it would usually always be on the same server however when we have had issues and the databases have moved around the OAB files would have been on other servers.  I initially thought this was an issue but now realise it's not.  

Thanks for all your help (and your quick reply).  

Regards,  

Matt
