---
title: "SSL on domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/167705/ssl-on-domain-controllers
question_id: 167705
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# SSL on domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/167705/ssl-on-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our internal and external domain is the same - domain.com, and for the internal users to be able to reach our website hosted externally, we installed IIS with redirection on all DCs. So when internal users type in http://domain.com they are redirected properly, but when https is used, it bombs.  I believe it's because none of our DCs listen on 443, so all those https requests are dropped.  My question is what is the best approach to remedy this, apart from renaming the domain?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-19*

What is the best practice  

Best practice is to install IIS on its own windows instance, never on a domain controller. The original problem you cited would be better addressed with a split brain setup.  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-19*

You can follow along here.  

https://support.microsoft.com/en-us/help/324069/how-to-set-up-an-https-service-in-iis  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-19*

@Anonymous   Thank you, good info, but unfortunately not what I'm looking for.  We don't need a different answer for internal/external clients, we need our DCs to handle https://domain.com calls.  Plus, our public DNS is handled by a separate server.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-18*

This one may help.    

https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/split-brain-dns-deployment    

--please don't forget to Accept as answer if the reply is helpful--
