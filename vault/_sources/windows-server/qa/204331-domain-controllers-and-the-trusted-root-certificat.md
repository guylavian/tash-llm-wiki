---
title: "Domain controllers and the Trusted Root Certification Authorities container"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/204331/domain-controllers-and-the-trusted-root-certificat
question_id: 204331
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Volunteer Moderator"]
---
# Domain controllers and the Trusted Root Certification Authorities container

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/204331/domain-controllers-and-the-trusted-root-certificat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Microsoft,  

We installed a new Windows 2019 domain/forest with three domain controllers a few days ago.  

In the certificates mmc,  when we look at the Trusted Root Certification Authorities container for the Local Computer, we get different results on al three DC's.  The first DC has 37 certificates in the Trusted Root Certification Authorities container, the second DC has 20 certificates in this container and the third DC has 15 certificates in this container.  

Why the discrepancy? Is there some logic to this?  Replication between the DCs is normal and we have not removed/added any certs to the store.  

I've noticed this discrepancy previously in other domains but I assumed it was due to some sort of maintenance. In this case its a brand new domain.  

Replica

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-12-23*

Before locking this thread, I'll try to add some input for the original question.  

I remember that from a previous "CNNIC incident" in order to save some size on installation media, plus save user the trouble of seeing major CA have expired cert immediately after installation if you try to install it many many years later, Windows do not ship with current cert of common CAs. Instead, it have preset list of CA names that, when the OS see it on any trust chain, it will immediately try to download and trust it. (Remember the CNNIC incident that caused Chrome and Firefox remove CNNIC from trusted CA? That caused me to check whether CNNIC is in my trusted CA store but I can't find it. And as soon as I visited any site that uses CNNIC is CA for their certs, it immediately show up)  

So if the domain controllers have applications signed with different CAs, or someone have visited websites on the domain controllers, the certs listed in certificate store will be different.  

Since cert store data is not synced between domains, maybe that can help explain the difference.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-22*

Hi,    

Thank you for posting in our forum    

the command how to use certutil to check all 5 physical store in trusted root certification authorities store:    

Registry, Third-Party, Group Policy, Enterprise and Smart Card.    

When we use the following command to check the stores we find 5 stores’ name in command line:    

certutil -v –enumstore shows the following:    

Root                 (this is the logical store that aggregates all of the following)    

Root: .Default       (this is the registry store)    

Root: .AuthRoot    

Root: .GroupPolicy    

Root: .Enterprise    

Root: .SmartCard    

https://learn.microsoft.com/en-us/windows-hardware/drivers/install/trusted-publishers-certificate-store    

Hope this information can help you    

Best wishes    

Vicky
