---
title: "Event ID 1 MSExchange Autodiscover"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1666014/event-id-1-msexchange-autodiscover
question_id: 1666014
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
---
# Event ID 1 MSExchange Autodiscover

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1666014/event-id-1-msexchange-autodiscover (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

Recently I migrated Exchange 2016 to 2019, then I temporarily shut down Exchange 2016 and removed the Autodiscover URL from Exchange 2016

Everything works well but Exchange 2019 shows the below error:

Details

I run this command

Get-ClientAccessService | Select Name, AutoDiscoverServiceInternalUri, AutoDiscoverSiteScope | Format-List

the result is like this :

Name   : ServerExchange2019

AutoDiscoverServiceInternalUri : https://autodiscover.FQDN/Autodiscover/Autodiscover.xml

AutoDiscoverSiteScope          : 

I appreciate any feedback on this.

Thank you so much

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-05-14*

Set the ExternalURL property of the Autodiscover virtual directory, like this:

Get-AutodiscoverVirtualDirectory -Server | Set-AutodiscoverVirtualDirectory -ExternalUrl https://autodiscover.contoso.com/Autodiscover/Autodiscover.xml
