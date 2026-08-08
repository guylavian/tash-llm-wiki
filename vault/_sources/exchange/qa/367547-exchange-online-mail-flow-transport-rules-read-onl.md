---
title: "Exchange Online Mail Flow (transport) rules read only can't create new rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/367547/exchange-online-mail-flow-transport-rules-read-onl
question_id: 367547
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online Mail Flow (transport) rules read only can't create new rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/367547/exchange-online-mail-flow-transport-rules-read-onl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We've been using Office 365 for years and for the majority of the time, it works really well and I can find answers to any issues that come up.  

However, this one has me stumped.  

Yesterday, I went into the Exchange Admin Centre to edit one of the anti-phishing rules I have setup, only to find that all my mail flow rules are now read only and can't be edited. I also can't create new mail flow rules. I double checked to confirm my account is setup as global administrator, as it has been since day one. All looks good - as it should as I'm the only global admin.  

It was working fine last week. (I created two new rules to prevent students from sending/receiving external email.)  

So I signed out and back in - still the same.  

Then I created a new account and gave it the exchange admin role.  

Signed in with that account, went to the EAC and exactly the same happens - mail flow rules are read only.  

So then I setup another account with the global admin role. And guess what - that doesn't work either.  

I've tried it in Chrome and Edge, and on a couple of PCs, even at home last night. Still can't get it to work.  

No amount of searching has produced any useful insights as to what might be happening.  

What am I missing? It feels like it should be something simple, but as I'm the only admin, I don't know how it could have changed.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-23*

Hi @Ben Hall      

Have you tried using powershell to manage the tranport rules for your organization?    

New-TransportRule and Set-TransportRule, please check what results return.    

And the roles needed to run the command:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-22*

Ok, maybe someone messed with the ORg mgmt role.    

Verify it has that role. if not, add it and save

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

@Andy David - MVP   Thanks for the quick response.    

I've already tried that. I've added myself and the newly created exchange admin account to the Organization Management role.    

It didn't make any difference.    

This is what I have listed:
