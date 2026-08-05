---
title: "Understanding LDAP in Windows Active Directory Forest"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/754625/understanding-ldap-in-windows-active-directory-for
question_id: 754625
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
---
# Understanding LDAP in Windows Active Directory Forest

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/754625/understanding-ldap-in-windows-active-directory-for (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I need some help understanding LDAP in a Forest with multiple child domains.  

We are reviewing our firewall logs with a goal to restrict communications between company A and company B, which both have a child domain within the same forest. They used to be on a flat MPLS network but now we have segregated them into their own networks behind some next gen firewalls only allowing required communications between the two.  

When reviewing the network traffic we are seeing clients/servers in child domain A making LDAP connections to the domain controller in child domain B and vice versa. I am trying to understand if this is expected behaviour in a forest where we have transitive two-way trusts in place by default. This traffic is currently permitted on the firewall but we want to look at restricting it so that clients in child domain A only use DCs in child domain A for LDAP and authentication.  

Sites and Services is setup with multiple sites but they are not company specific, so for example we might have a site called India with a DC added from both child domain A and B, there is no India-CompanyA and India-CompanyB sites.  

So my questions are:  

-  Is what we are seeing normal and expected behaviour?  

-  Would it be safe to deny LDAP and Kerberos from clients/servers to DCs in the other child domain? (DC to DC traffic has its own FW rule on the required ports and would not be amended)  

-  Can we manipulate the destination LDAP servers on a per child domain basis?  

-  How are SRV records used in this process?  

Let me know if you need any more information but hopefully making myself clear!  

Thanks

## Answers

_No answers on this thread._
