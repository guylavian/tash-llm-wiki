---
title: "Getting Error LED=441 4.4.1 | Exchange Server 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1421870/getting-error-led-441-4-4-1-exchange-server-2013
question_id: 1421870
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Getting Error LED=441 4.4.1 | Exchange Server 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1421870/getting-error-led-441-4-4-1-exchange-server-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts,

I am unable to send emails outside the organization. However, I am receiving emails from all and inside communication incoming and outgoing is working fine too.

November 10, 2023 12:24:48 PM" orient-power.com DnsConnectorDelivery Connecting 1   "

 IP address: ""Failed to connect. Winsock error code: 10060, Win32 error code: 10060."" Attempted failover to alternate host, but that did not succeed. Either there are no alternate hosts, or delivery failed to all alternate hosts. The last endpoint attempted was };{FQDN=};{IP=}]" "Friday, November 10, 2023 12:24:32 PM"

Screenshot_1.png

We are running Exchange Server 2013 Service Pack 1 (SP1 aka CU4) 15.0.847.32  

DNS is running from Windows Server and in properties I only have DNS IP of the DC server, no other IPV4 or IPV6 entry is enabled. However, the forwarder tab in DNS properties is empty and there was no entry before and exchange was working fine.

I am able to ping MXs of all affected domains but emails don't go out. I have tried restarting the transport service but that didn't work.  

 

Apologies, If I missed any details. Let me know what else I can provide for better assistance.

An urgent help is much appreciated.

Thank you.

## Answers

_No answers on this thread._
