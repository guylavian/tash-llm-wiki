---
title: "Different ADFS farms for Subdomain and root domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4874774/different-adfs-farms-for-subdomain-and-root-domain
question_id: 4874774
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: []
---
# Different ADFS farms for Subdomain and root domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4874774/different-adfs-farms-for-subdomain-and-root-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there anyway to tell O365 to point to a different ADFS farm for the subdomain when the root domain is already federated? Or, can O365 be federated to an ADFS farm chain a pass through to another ADFS farm in a different forest?

The problem I'm working through is two forests with the same netBIOS name. Both of which share the same root domain.

The first forest 'ad.domain.edu' is already federated in our tenant space as the root domain 'domain.edu'.

There is a second forest 'sub.ad.domain.edu' which I need to figure out how to cram into the tenant space.

The problem being... its a different forest, a subdomain by DNS, and they both have the same netBIOS domain name.

This puts forest trusts out of the question. It would be possible to do multiple forest migrations to bring them both together, or even change the domain netBIOS name so that a trust can be built... Yet, this is for 200K+ live accounts. Not going to happen
 easily.

Adding a subdomain to the root will inherit the root domains authentication method (federated) and the ADFS information... which makes this a nasty situation. Any suggestions if the first two questions are not doable?

## Answers

_No answers on this thread._
