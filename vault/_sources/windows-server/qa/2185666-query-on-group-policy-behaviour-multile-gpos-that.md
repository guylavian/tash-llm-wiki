---
title: "Query on Group Policy behaviour - multile GPOs that rename local Administrator account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185666/query-on-group-policy-behaviour-multile-gpos-that
question_id: 2185666
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Query on Group Policy behaviour - multile GPOs that rename local Administrator account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185666/query-on-group-policy-behaviour-multile-gpos-that (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone, 

I'm hoping you can help me with a query on the behaviour of Group Policy when multiple GPOs that rename the local Administrator account apply to the same server.

I believe I understand the concepts around Group Policy precedence and the winning GPO. However I am not clear as ti what happens in this particular scenario.

In such a case would the local Administrator account be renamed only once at GPO application (to match the name specified in the winning GPO) or would it be renamed multiple times? For example if there were two applicable GPOs that apply would the local administrator account be first renamed as per the GPO that is applied first,  followed by another rename as per the GPO that applies last? Would it mean that the local administrator account name will flips back and forth at each GPO refresh?

The background is that I'm looking into implementing a consistent naming standard across all member servers joined to an Active Directory domain that I manage.  I was toying with the possibility of linking an enforced GPO with the desired "official" local adminisrator account name at the root of the OU hierarchy that contains member servers.

I am curious as to the behaviour of this particular policy setting when there are multiple GPOs at  play.

Any clarifcation on this would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-04*

Hi Neuvi,

Thank you so much for your response. This is extremely helpful and fills a gap in my knowledge of Group Policy. It all seems very clear now!

As you recommend I will test in a UAT environment that is similar to production before implementing.

Thank you once more.
