---
title: "Number 2 EDGE Exchange 2019 server ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1187229/number-2-edge-exchange-2019-server
question_id: 1187229
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Number 2 EDGE Exchange 2019 server ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1187229/number-2-edge-exchange-2019-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

if you have 1 mailbox and 1 edge server and it works fine, but you want to install edge server no. 2 because you have 2 WAN connections. 

Can you run a subscription between edge server number 2 and mailbox without affecting the already running subscription between edge server number 1 and mailbox? 

I've been looking for a description but haven't been able to find one :-) 

A tip would be great

Best Regards

John B

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2023-03-07*

```
Solution:
I have a Firewall Zyxel ATP500 where I have 2 WAN ports, each with its own Static WAN IP address.

In MX Record I have configured mail.domain.com for WAN 1 and mx20.domain.com for WAN 2

Everything that came from mail went up to EDGE1 and I got errors on Banner when I tested from outside.

I then installed EDGE2 where I configured the correct banner

When I opened EMS and ran New-EdgeSubscription -FileName "C:\EdgeSubscriptionInfo.xml" on EDGE2 I changed to the following: New-EdgeSubscription -FileName "C:\EdgeSubscriptionInfo2.xml"
Copied EdgeSubscriptionInfo2.xml onto the Mailbox and opened EMS and ran New-EdgeSubscription -FileData ([byte[]]$(Get-Content -Path "C:\EdgeSubscriptionInfo.xml" -Encoding Byte -ReadCount 0)) -Site "Default -First-Site-Name"

When I opened EMS on the Mailbox and ran start-edgesynchronization I got an LDAP error and had to manually configure the host file on EDGE2 and on the Mailbox

My banner test was now in order but I still had errors on SMTP Transaction Time and used the following:
​Run the below in EMS
  get-ReceiveConnector | select name, tarpit interval
Use the following command to change the Tarpitting setting to 1 second. Replace
  Set-ReceiveConnector -identity "Default internal receive connector EDGE-W2K19" -tarpitinterval 00:00:01
  Set-ReceiveConnector -identity "Mail Relay" -tarpit interval 00:00:01

If you have any question please mail me :-)
```
