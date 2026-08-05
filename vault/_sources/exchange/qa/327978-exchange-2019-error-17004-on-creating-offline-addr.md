---
title: "Exchange 2019 error 17004 on creating Offline Address Book"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/327978/exchange-2019-error-17004-on-creating-offline-addr
question_id: 327978
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 error 17004 on creating Offline Address Book

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/327978/exchange-2019-error-17004-on-creating-offline-addr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recently uninstalled Exchange  2016 from our Exchange environment leaving just one Exchange ‎‎2019 CU8 Exchange Server. Before removing Exchange 2016 we migrated all the Arbritration boxes ‎including the Default Offline Address List. Since removing the Exchange 2016 server my Outlook clients ‎can’t download the Offline Address Book (nor is the Outlook client updating automatically). ‎  

When we try to download the address book we get “Reported error (0x8004010f): The operation ‎failed. An object cannot be found.”‎  

However, Outlook Web Access (OWA) both on the network and off network had updated email ‎addresses. So I know we have an active Global Address Book.‎  

I’ve noticed in the event viewer we are getting Event ID 17004 “Generation of OAB "\Default Offline ‎Address List (Ex2013)" failed.    Dn: CN=Default Offline Address List (Ex2013),CN=Offline Address ‎Lists,CN=Address Lists Container,CN=Florida Dept of Veterans Affairs,CN=Microsoft ‎Exchange,CN=Services,CN=Configuration,DC=FDVA,DC=STATE,DC=FL,DC=US      ObjectGuid: 394ecdf7-‎cfd3-404d-b88f-5abc5d4436e5” ‎  

But when I do a Get-Mailbox -database “xxx” -arbitration | FL I am getting this:‎  

GeneratedOfflineAddressBooks           : {\Default Offline Address List (Ex2013)}‎  

‎…‎  

‎…‎  

Alias                                  : SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}‎  

So it looks like my new Exchange 2019 environment is confused about what Offline Address Book to ‎create. I am also concerned (based on research) the “SystemMailbox{bb558c35…}” is the wrong ‎version. If this is the case, how do I get the addresses in the old OAB (“SystemMailbox{bb558c35…}” to ‎the new ““394ecdf7-cfd3-404d-b88f-5abc5d4436e5”?‎  

FYI – My virtual OAB directory (i.e. E:\Exchange\Client\OAB) has a folder “394ecdf7-cfd3-404d-b88f-‎‎5abc5d4436e5” folder which matches the Event Viewer Error message. ‎  

Is there an easy way to fix this? ‎  

Please advise.‎  

Thank you

## Answers

_No answers on this thread._
