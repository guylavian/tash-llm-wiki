---
title: "Can't open Owa FQDN from machine/phone outside domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1525288/cant-open-owa-fqdn-from-machine-phone-outside-doma
question_id: 1525288
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Can't open Owa FQDN from machine/phone outside domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1525288/cant-open-owa-fqdn-from-machine-phone-outside-doma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

DNS resolves correctly, to internal ip, and connects to https://192.168.x.x/owa but if I use the mail server public name I can't connect at all ! 
ERR_CONNECTION_TIMED_OUT with Edge/Chrome Incognito or not.
And that's from the same subnet, in a machine not joined to the .local domain, either in a virtual machine or in wifi ! Ok from other subnet in site/to/site vpn though!
If I join the Windows machine to the domain I get connected immediately even before rebooting. But this is not possible for Android and IOS phones.
No problems with Outlook autodiscover.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-21*

Anybody? Do I need open a ticket at ms support ?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-07*

Phones are not resolving internal IP, but external, strangely. They work on Activesync but cannot access /owa. (we have loopback on sonicwall firewall)
Tcp test fails on fqnd (external ip) but ok using internal ip (portDroid). I am not sure how it gets connected to ActiveSync. I just tried from Outlook app in wifi.

But Windows machines resolve internal ip of the Exchange server using the same public mail server fqdn (eg:outlook.contoso.com set in split dns in our dc), the same in the certificate and antispam lookups.
Test-NetConnection outlook.contoso.com -port 443
TcpTestSucceeded : True

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-06*

Hi @Andre g,

DNS resolves correctly, to internal ip

but if I use the mail server public name I can't connect at all

Can you share some more details on your DNS settings?

If your mail server public name is mail.contoso.com, you need a A or CNAME record to point mail.contoso.com to the internal ip of Exchange.

If the client device which is having the issue is not domain-joined, is it using the same DNS server in your internal network as other domain-joined ones?

If it is using another DNS server, you need to make sure mail.contoso.com can be resolved correctly on that server.

(And if it is a public DNS server, you need to point mail.contoso.com to the public ip address of Exchange or firewalls in front of it)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
