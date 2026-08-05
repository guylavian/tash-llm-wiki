---
title: "Default location for search in active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/338479/default-location-for-search-in-active-directory
question_id: 338479
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Default location for search in active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/338479/default-location-for-search-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a way to change the default location that is opened when searching the Active directory?  

By default it is set to search the whole domain.  

(when you search users and computers etc, from this location)   

Instead, I want the default search to be limited to a OU within that domain.  

Is this even possible?  

The reason I'm asking is because I want to prevent disabled users from showing in search suggestions, by moving them to a separate OU.  

Thanx in advance for all the answers...

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-31*

My question is: IS it possible to be able to change this location to a specific OU, as a DEFAULT, and not to search the whole domain?    

The default location is the whole domain :(

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-31*

Hi,    

Do you mean you want to search in active directory through the following way:    

    

If so , you can customer the location     

    

    

If you do the research use the command , you can modify the command to limit the location.    

Best Regards,
