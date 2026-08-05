---
title: "will a domain controller let encrypted message or document travel in a WAN from a source computer to a destination computer?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202308/will-a-domain-controller-let-encrypted-message-or
question_id: 202308
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# will a domain controller let encrypted message or document travel in a WAN from a source computer to a destination computer?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202308/will-a-domain-controller-let-encrypted-message-or (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

lets take a scenario in which a computer data network is spread across the country. Now one computer in a LAN, which happens to be a part of the country wide WAN, wants to send a message to another computer at a remote location. Both these computers are part of a LAN which have Domain Controllers in network.    

Now we make a device which has a WAN port and a LAN port (both RJ 45).  

The WAN port is connected to the data network coming from outside, and a computer is connected to the LAN port of this device.  

This device has the ability to take the document from the Source computer from LAN side and transmit an encrypted document to WAN side for the Destination computer.  

Now both the LAN (of both computers) has Domain Controller installed and governing the rules.  

So my question is that whether the Domain Controller allow the encrypted document to travel to the destination computer from the source computer. Since the Payload of IP packet is encrypted....but the header contain Source and Destination IP addresses....but the user ID logged on to the Source computer gets encrypted and forms part of the payload....so how will the DC, which monitors user IDs also, let the packets flow to destination?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-24*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-22*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-12-17*

I'd check the required ports listed here are flowing between sites.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

https://www.microsoft.com/en-us/download/details.aspx?id=24009    

--please don't forget to Accept as answer if the reply is helpful--
