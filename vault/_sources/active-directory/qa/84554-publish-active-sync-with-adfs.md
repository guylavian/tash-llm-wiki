---
title: "publish active sync with adfs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/84554/publish-active-sync-with-adfs
question_id: 84554
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# publish active sync with adfs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/84554/publish-active-sync-with-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dears,    

i configured since a while active sync and published it using adfs and wap. it was working great.    

relying party trust created type : non claims aware    

publishing on wap using adfs: rich clients    

starting the last night, it stopped working with an error: the username or password are wrong.    

however, nothing has changed.    

these event ids are in the event viewer of adfs    

    

your help is so appreciated

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-17*

this worked after rebooting the exchange server  

thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-03*

"the proxy trust certificate is a rolling certificate valid for 2 weeks and periodically updated. This is stored in an internal, protected store so you won’t see it in any of the usual certificate stores. "  

if the above is real, then why i am seeing proxy certificates are expired in the personal store.  

in addition, owa is working fine usinf adfs and wap. the issue is just with activesync. and wap config is green  

the client informed me, that the activesync stopped working while the pdc was rebooting. however, the pdc is running now but the issue is still persisting  

any ideas  

tahnk you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-02*

adfs proxy trust on adfs personal store shows 2 certifcates: both of the are expired.  

but owa is still working.  

just activesyn is not.  

however, how can i renew the certificate? the adfs proxy certificate is different that the one used for adfs wap and exchange which is a wildcard one.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-02*

Error 521 indicates the any one of the following user actions needed  

User action:  

Examine the request and verify that at least one of the following parameter sets are present.  

Username and password  

Username, password, and device registration certificate  

User certificate  

Probably, check the certificate at first and see the certificate is still valid
