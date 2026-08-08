---
title: "owa published trhought adfs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/50164/owa-published-trhought-adfs
question_id: 50164
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# owa published trhought adfs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/50164/owa-published-trhought-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

my owa on my exchange server is publsihed through adfs and wap.    

after rebooting the server, when a user connects externally, the adfs page is launched then after inserting the username the owa page is launched in order to sign in to owa.    

it was working after the first sign in on the adfs page.    

one more thing, when i insert the upn i cant sign in, i can just sign in using windows credt    

events:    

Token Type:     

http://schemas.microsoft.com/ws/2006/05/identitymodel/tokens/UserName     

%Error message:     

“xxx@xxxxxxxxxxxxx  .com” -The user name or password is incorrect    

With event ids 342, 1000 and 364.    

thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-07-23*

it was working fine dears, i did the setup like 3 months ago and everything was working  

i recieved a call recently that after the reboot of the servers the issue is happening

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-07-22*

If you are getting a logon prompt for OWA after authenticating to ADFS, then you haven't set it up correctly     

Sounds to me as if you didnt enable the OWA and EAC virtual directories for ADFS Auth per this doc:    

https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-22*

Do you setup up for Exchange OWA/EAC custom claim rules? Use AD FS claims-based authentication with Outlook on the web
