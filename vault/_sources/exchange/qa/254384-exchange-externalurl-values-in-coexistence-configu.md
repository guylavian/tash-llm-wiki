---
title: "Exchange ExternalURL values in coexistence configuration prior to migration [2010/2016]"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/254384/exchange-externalurl-values-in-coexistence-configu
question_id: 254384
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange ExternalURL values in coexistence configuration prior to migration [2010/2016]

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/254384/exchange-externalurl-values-in-coexistence-configu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are in the process of migrating from Exchange 2010 SP3 RU30 to Exchange 2016 CU18 (on-premises for both). We do not publish Autodiscover externally. Mobile device configuration is handled by our MDM software. For external clients, we just have EAS and OWA connections that go to our Citrix Netscalers and then over to our internal F5 network load-balancers. Microsoft Outlook must be on our network / VPN in order to connect.   

We used to have split DNS, but that was removed as part of an unrelated initiative. Our internal DNS is a purely internal namespace (think domain.local). How should we be configuring the ExternalURL values on the Exchange virtual directories given no split DNS and with not publishing Autodiscover externally? Should they be left blank? Should they match the InternalURL values?    

We have separate public DNS records + IPs  for both the existing 2010 environment as well as for the 2016 environment (2 names for 2010 and 2 names for 2016. Call them owa.domain.com and mdm.domain.com (2010) and owa16.domain.com and mdm16.domain.com.  

We've tested connectivity to Exchange 2016 mailboxes using owa16 and mdm16, and they both work. The owa and mdm records work for our 2010 users. Are there any considerations before we update the names for owa and mdm to resolve to the IPs for owa16 and mdm16?

## Answers

_No answers on this thread._
