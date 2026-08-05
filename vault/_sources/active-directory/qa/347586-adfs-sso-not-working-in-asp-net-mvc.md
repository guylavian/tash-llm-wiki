---
title: "ADFS SSO not working in ASP.NET MVC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/347586/adfs-sso-not-working-in-asp-net-mvc
question_id: 347586
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS SSO not working in ASP.NET MVC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/347586/adfs-sso-not-working-in-asp-net-mvc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I want to integrate ADFS SSO in my MVC application.

I am using the Microsoft.Owin.Security.WsFederation

I have set the meta data url: 'https://********/metadata**'

Wtrealm: 'https://********/'

Wreply:'localhost:4344'

i have also integrate the RedirecUri in action.

I have checked the network tab after some request i got the localhost redirected you too many times

query params of url is

http://localhost:54415/?  

wtrealm=*****  

&wctx=***  

&wa=wsignin1.0  

&wreply=http%3A%2F%2Flocalhost%2F

in each request wctx is changing.

Your help will be highly appreciated.

## Answers

_No answers on this thread._
