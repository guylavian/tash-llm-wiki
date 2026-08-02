---
title: "Need to remove ADFS settings from Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/617215/need-to-remove-adfs-settings-from-exchange
question_id: 617215
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Need to remove ADFS settings from Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/617215/need-to-remove-adfs-settings-from-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I was doing some testing and setup ADFS for Exchange 2019 OWA.  Now I need to remove it.  I have removed all settings from ADFS but still get redirected to the ADFS URL.  It fails to do anything because all ADFS settings are removed but I can not seem to find why OWA is still being redirected to the ADFS URL. I see the set-organizationconfig but can not figure out how to clear those settings out.  Putting $null in just gives an error.    

Assistance would be greatly appreciated.  Thanks!!

## Answer (community) — community member

*upvotes: 1 · updated: 2021-11-05*

Wow, you're awesome! I would never have guessed just having the auth method enabled with others still enabled would have forced ADFS.  

Thanks a million.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-05*

Thanks for the quick answer  

The only thing I did to the virtual directories was to enable ADFS authentication. I did not disable any of the other auth methods, just enabled ADFS auth.  

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-11-05*

Did you reverse all the virtual dir settings and restart IIS on the Exchange Servers?
