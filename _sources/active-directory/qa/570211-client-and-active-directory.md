---
title: "client and active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/570211/client-and-active-directory
question_id: 570211
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# client and active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/570211/client-and-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have multi domain controllers in our organization and I have several questions regarding them:  

-  How can I determine which domain controller is in use when joining a client to domain controller?  

-  if one domain controller is corrupted, how can I prevent client from connecting it when join a client to domain controller?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-29*

Hi Rick,  

The DC discovery processes uses the DsGetDcName API which returns the DC which will be used by subsequent AD functions.  You can manually call this function to determine which DC will be returned, have a look at https://nettools.net/dsgetdcname  

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-29*

As @Andreas Baumgarten    mentioned, Windows Client DC Discovery process only use DCs which are good and healthy, so you should not worry about it.     

Domain joining files are saved in C:\Windows\Debug\ directory, you can read the name of the Domain Controller, which was used to join the Domain.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-09-29*

Hi @RICK-0238 ,  

-  Simple way: If you ping on the client using the domain name you get an answer from a DC. It's most likely this DC will get the request to join the client to AD.  

-  If the DC is corrupt the DC should answer any request at all because AD service isn't running. Or what do you mean with "DC is corrupted"?  

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)  

Regards  

 Andreas Baumgarten
