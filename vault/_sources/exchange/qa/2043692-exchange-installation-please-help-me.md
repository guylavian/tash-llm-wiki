---
title: "Exchange Installation, please help me"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2043692/exchange-installation-please-help-me
question_id: 2043692
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Exchange Installation, please help me

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2043692/exchange-installation-please-help-me (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

I have an AD domain xxx.com and the AD subdomain m1.xxx.com . 

I'm going to install an Exchange 2019 server in a domain M1.xxx.com . 

To carry out the preparatory actions, I created an account in the domain xxx.com ACC1 and included it in the AD groups in the domain xxx.com : Schema Admins, Enterprise Admins and Domain Admins. Next, I created an ACC2 account in the domain M1.xxx.com and included it in the Schema Admins and Enterprise Admins group in the domain xxx.com , as well as to the Domain Admins group in the domain M1.xxx.com . 

I'm going to extend the AD schema with an ACC1 account. As I believe, I need to extend the AD in the domain m1.xxx.com using an ACC2 account. 

After that, I'm going to run the Exchange installation on behalf of the ACC2 account. 

I ask for advice. Did I understand the whole procedure correctly?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-10*

There is an existing exchange organization with Exchange 2013 and Exchange 2016 servers. 

It is necessary to implement new Exchange 2019 servers in the organization for subsequent gradual migration to new servers. 

I know the steps to install new servers: 1. Updating the schema 2. AD update 3. Exchange 2019 setup 

Are there any problems, points, tips when implementing this plan?
