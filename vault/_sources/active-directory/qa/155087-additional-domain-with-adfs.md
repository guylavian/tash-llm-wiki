---
title: "Additional domain with ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155087/additional-domain-with-adfs
question_id: 155087
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Additional domain with ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155087/additional-domain-with-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

Currently we have a 3 services that utilize ADFS (syncplicity & Cisco Call manager) that uses domain @mydomain.com. Since we have changed the domain name to @newdomain.com, what are the changes that we have to do with ADFS? or is it required to make changes specific to the published applications?  

Thanks in advance

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-08*

If you have only 1 claim provider trust, and as long as you have not created any custom JavaScript manipulating the username format, ADFS is agnostic of the UPN of the user. It just needs to works in ADDS to work in ADFS.  

Regarding the application it is a different story. Maybe the apps are using the current UPN as an identifier. And by updating that in ADDS you may break the "link" between the user and the app.  

You can look at the rules you currently have for your relying party and check if it leverages the UPN in any of the rules (you can copy/paste screenshots here if you are not sure). You should reach out to the app owner to make sure. And ultimately, if they can't update the anchor attribute they currently use, you can still send the old format to the application by replacing the part of the UPN claim with another domain.
