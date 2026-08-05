---
title: "Device Does Not Show Up in Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/967746/device-does-not-show-up-in-active-directory
question_id: 967746
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Device Does Not Show Up in Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/967746/device-does-not-show-up-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm adding a new device to my domain. Active Directory is not showing the device in Users & Computers folder where it should have been deployed to receive all of my Group Policies. How do I fix this?

## Answer (community) — community member

*upvotes: 2 · updated: 2024-08-13*

Also, check your filter settings in the ADUC panel. I was researching this very same issue when I discovered the View filter options had somehow been set to only show Users, not computers, domain controllers or other container items. Instant solution to the problem!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-16*

Hi @Conrad Banez       

If the machines are joining the domain without any error but are not displayed, the issue might be caching in the ADUC console, as it does cache the previously read objects from AD and might not show newly added objects until the OU view is refreshed (press F5) or ADUC is restarted.    

Also by default if machines are joined to the domain using the system properties dialog, they will be placed in the Computers container, you might need to move the computer objects to the correct OU.     

Gary.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-08-15*

Not much to go no but I'd probably just try joining the domain again. Make sure the domain controller and problem member both have the static ip address of DC listed for DNS and no others such as router or public DNS.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
