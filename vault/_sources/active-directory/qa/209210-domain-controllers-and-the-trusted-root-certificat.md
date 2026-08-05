---
title: "Domain controllers and the Trusted Root Certification Authorities container"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/209210/domain-controllers-and-the-trusted-root-certificat
question_id: 209210
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain controllers and the Trusted Root Certification Authorities container

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/209210/domain-controllers-and-the-trusted-root-certificat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello @Vicky Wang    .    

Hello Microsoft ,    

We installed a new Windows 2019 domain/forest with three domain controllers a few days ago.    

In the certificates mmc, when we look at the Trusted Root Certification Authorities container for the Local Computer, we get different results on all three DC's. The first DC has 37 certificates in the Trusted Root Certification Authorities container, the second DC has 20 certificates in this container and the third DC has 15 certificates in this container.  This was noted immediately after all three domain controllers came up. Its a brand new domain, nothing has been done to it, no certificates installed or removed, no application servers, no users, nothing deployed, no GPO, nothing. Its untouched,     

Why the discrepancy between the three DCs?  Is there some logic to this? Replication between the DCs is normal and we have not removed/added any certs to the store.    

I've noticed this discrepancy previously in other domains but I assumed it was due to some sort of maintenance. In this case its a brand new domain.    

Thanks

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-12-31*

Please refer to here to see the behavior I described before, plus how to use PowerShell script to show the certificates embedded in crypt32.dll.  

Any certificates not listed here are installed by Root Certificate Auto Update.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-25*

Hi,    

Based on my research, the Microsoft Trusted Root Certificate Program releases changes to our Root Store on a monthly cadence, except for December.    

Make sure all the DCs have the latest version.    

Following link for your reference:    

https://learn.microsoft.com/en-us/security/trusted-root/release-notes    

https://learn.microsoft.com/en-us/security/trusted-root/release-notes    

Best Regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-24*

@Anonymous       

Hello,    

Very simple: 3 Windows 2019 servers, all installed at the same time with the same media.  Create new domain on one DC (first image). Then promote the other two servers to DCs in the new domain.  All done in a couple of hours. Issue visible immediately. Nothing else was done, nothing installed, nothing removed, no GPOs, nothing    

No issue at this point, just trying to understand why in case there is a cert issue in the future,  I've noticed this many times over the years in other domains, I just assumed in the past that some work was done that would cause the number of Trusted CA certs to vary between DCs but I don't think that's the case now. Please see attached screen shots
