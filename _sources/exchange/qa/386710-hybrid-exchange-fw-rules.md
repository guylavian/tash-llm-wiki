---
title: "Hybrid exchange FW rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/386710/hybrid-exchange-fw-rules
question_id: 386710
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Hybrid exchange FW rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/386710/hybrid-exchange-fw-rules (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

Question about hybrid environment ports.    

Is this the list of ports and IP addresses  needed to open for on-prem<-->o365 hybrid environment?:    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges-21vianet?view=o365-worldwide     

443,25 on-prem ports only to O365 IP addresses?    

Questions:    

Does this O365 addresses changes frequently?    

Is there an easy way to make this rules on firewall?    

Someone mention JSON list to import in FW    

https://forum.opnsense.org/index.php?topic=19472.0     

This ports must be opened from on-prem exchange to O365 because:    

"on premise Email Security Appliance integration with O365 is not supported."    

https://www.sonicwall.com/support/knowledge-base/on-premise-email-security-appliance-and-office365/180807124206957/     

So,mail flow between O365 and on-prem exchange must bypass anti-spam because it is not supported by Microsoft?    

Any advice about O365<-->on-prem exchange ports needed to be open for hybrid environment?    

Thank you

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-05-07*

It does not change frequently. In fact, when it does change, they typically add IP ranges, not remove them, so  would go with that list and not worry about it  :)   

You can see from the change log how often its updated:  

https://endpoints.office.com/version/China?allversions=true&format=rss&clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7
