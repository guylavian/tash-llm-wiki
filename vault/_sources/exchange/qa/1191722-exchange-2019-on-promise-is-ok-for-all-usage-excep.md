---
title: "Exchange 2019 on promise is ok for all usage except Iphone"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191722/exchange-2019-on-promise-is-ok-for-all-usage-excep
question_id: 1191722
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 on promise is ok for all usage except Iphone

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191722/exchange-2019-on-promise-is-ok-for-all-usage-excep (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, i have install an Exchange 2019 and all fonctions are ok (Outlook in interne or external, acces for android phone ok) except Iphones phones.

When i test by https://testconnectivity.microsoft.com/ the active-sync, it's ok. no error.

When i test with a smartphone (excep Iphone), i can send and receive email, check contact, etc...

When i test with a iphone (with Outlook app), it's ok in app.

When i test with iphone, i can test parameters of my exchange account but i cann't check email, send email or connect in server. I send me "Connection Server Fail".

I have not serious orientation for search reason... Maybe SSL but it's ok on my web navigator.

Apple use another method for connect or another protocol ?

Thank you for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-22*

Thank You for Your Answer. 

We have applicate this solution but it's the same issue.

We have applicate this rights directly in domain for the Exchange Servers Groups with this right : Descendant msExchActiveSyncDevices checked.

I must reboot exchange server ? I must wait a few time for right propagation ? 

Where i can test for look errors ? 

Thank you for your answer.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-22*

Assign the Exchange Servers group the right to change permissions against msExchActiveSyncDevices objects to work around this issue. To do this, follow these steps:

-  Start Active Directory Users and Computers.

-  Click View, and then click to enable Advanced Features.

-  Right-click the object where you want to change the Exchange Server permissions, and then click Properties. ( Note - You can change permissions against a user, an organizational unit, or a domain.

-  On the Security tab, click Advanced.

-  Click Add, type Exchange Servers, and then click OK. 

-  In the Apply to box, click Descendant msExchActiveSyncDevices objects.

-  Under Permissions, click to enable Modify Permissions.

-  Click OK three times.
