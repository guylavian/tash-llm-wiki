---
title: "My Domain Controller is unavailable (Windows Server 2012 R2). What to do?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/477497/my-domain-controller-is-unavailable-windows-server
question_id: 477497
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# My Domain Controller is unavailable (Windows Server 2012 R2). What to do?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/477497/my-domain-controller-is-unavailable-windows-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,  

One of my Domain Controllers "died". I had to reboot it, but it doesn't work, and it crashed. So, I have a backup made last week (this DC is a VM). What should I do?  

1- Use this Backup? If so, how to initialize the DC? Should I initialize this DC by using an authoritative restoration? How to make this?  

2- Making a MetaData Cleanup of the unavailable Domain Controller and then creating a new DC from the scratch?   

Thank you.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-16*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-16*

Hi，  

Welcome to share here!  

If the "died" DC is not the only on your domain, we don't need to restore it from the backup.  

For a FSMO holder, we may try to size the FSMO role from a good DC.  

Then perform a metadata cleanup.  

If you still want to it a DC again, you can create a new one as you mentioned above.  

If you have any questions about it, feel free to let us know.  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-15*

Any progress or updates?
