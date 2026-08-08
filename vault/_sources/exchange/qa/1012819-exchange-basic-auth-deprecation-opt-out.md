---
title: "Exchange basic auth deprecation opt-out"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1012819/exchange-basic-auth-deprecation-opt-out
question_id: 1012819
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange basic auth deprecation opt-out

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1012819/exchange-basic-auth-deprecation-opt-out (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have completed the opt-out process for all the legacy protocols based on the steps in this article    

[https://techcommunity.microsoft.com/t5/exchange-team-blog/basic-authentication-deprecation-in-exchange-online-september/ba-p/3609437]    

However when I return to the "run tests" page later, there's no feedback giving any indication that anything has changed, and it just continues to say that I can opt-out protocols.  Is this normal behaviour?, and is there any way to confirm this has taken effect?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-19*

Did you rerun the test (https://aka.ms/PillarEXOBasicAuth)? Another way to confirm the changes would be too look at the BasicAuthBlockedApps property:    

```
Get-OrganizationConfig | select BasicAuthBlockedApps
```

A value of 255 will indicate all protocols are blocked. Values different than that indicate that at least some protocols are enabled for Basic auth.    

```
Exchange ActiveSync (EAS): 1  
Exchange Web Services (EWS): 2  
POP3: 4  
IMAP4: 8  
Remote PowerShell: 16  
MAPI over RPC (Outlook Anywhere): 32  
Offline Address Book (OAB): 64  
RPC: 128
```

And in case you didn't have any auth policies configured beforehand, also check:    

```
Get-AuthenticationPolicy
```
