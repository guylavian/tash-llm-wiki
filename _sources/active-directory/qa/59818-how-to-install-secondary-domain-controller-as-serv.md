---
title: "How to install secondary domain controller as server core?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/59818/how-to-install-secondary-domain-controller-as-serv
question_id: 59818
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# How to install secondary domain controller as server core?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/59818/how-to-install-secondary-domain-controller-as-serv (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone!  

  How to install secondary domain controller as server core on 2k19?  

Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-11*

All worked fine, except for:
Set-DnsClientServerAddress –InterfaceAlias <Ethernet> -ServerAddresses <192.168.2.50>
It was impossible to put an alias that could be recognized.
Other than that, it promoted de Server to DC just fine.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-05*

Some basic operations here for core server.      

https://learn.microsoft.com/en-us/windows-server/administration/server-core/server-core-administer      

and some options here to remotely manage and configure the new server.      

https://learn.microsoft.com/en-us/windows-server/administration/server-core/server-core-manage      

--please don't forget to Accept as answer if the reply is helpful--
