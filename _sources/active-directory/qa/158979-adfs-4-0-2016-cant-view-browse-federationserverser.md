---
title: "ADFS 4.0 2016 - can't view/browse \"..federationserverservice.asmx\" locally an external"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/158979/adfs-4-0-2016-cant-view-browse-federationserverser
question_id: 158979
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS 4.0 2016 - can't view/browse "..federationserverservice.asmx" locally an external

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/158979/adfs-4-0-2016-cant-view-browse-federationserverser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After a fresh installation of ADFS on Server2016 I'am not able to open the following Url locally on the ADFS Server:  

https://<ADFS-FQDN>/adfs/fs/federationserverservice.asmx  

IE -> This page can’t be displayed   

Chrome -> This site can’t be reached  

"https://Localhost/.." is also not working.  

The ADFS Service is running.  

How can I troubleshoot this?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-11*

Are other endpoints working? If you try https://ADFS-FQDN/FederationMetadata/2007-06/FederationMetadata.xml, is this working?  

What if you try them remotely?  

If that still doesn't work and you don't see errors in the AD FS Admin eventlog, then common issues are DNS, firewall and eventually, TLS version incompatibilities.
