---
title: "Exchange 2016 disclaimer not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199309/exchange-2016-disclaimer-not-working
question_id: 199309
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 disclaimer not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199309/exchange-2016-disclaimer-not-working (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.  

We just update our disclaimer on Exchange 2016 (on prem), but for some reasons, the old disclaimer still showing in user Outlook email.  

For example:  

The old disclaimer has url "securemail.contoso.com".  

The new disclaimer has url "secure.contoso.com".  

The only change was that we change the "securemail" to "secure".  

Thanks for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-16*

Has the disclaimer been updated after 15 min?    

If not, is the transport rule agent enabled on your server?    

```
Get-TransportAgent "Transport Rule Agent" | Format-List
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-15*

Give it 15 minutes, if it still doesnt show the updated disclaimer, verify the change in EAC under rules and restart the transport service on all the Exch Servers
