---
title: "Event 2008 MSExchange OAUth"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1696895/event-2008-msexchange-oauth
question_id: 1696895
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
---
# Event 2008 MSExchange OAUth

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1696895/event-2008-msexchange-oauth (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After recreated oauth cert i get plenty of Event 2008.  

I have an Exchange 2019 server with hybrid Exchange Online

Event 2008 MSExchange OAUth

When retrieving metadata from the url 'https://login.windows.net/domain.onmicrosoft.com/federationmetadata/2007-06/federationmetadata.xml', different certificate(s) have been found.

I have run Get-Federationtrust | Set-FederationTrust –RefreshMetadata  

it says that the command completed successfully, but no settings of 'Microsoft Federation Gateway' have been modified.  

I check oauth connection and both sides were succesfull.  

I have read about   

Get-PartnerApplication Remove-PartnerApplication <application name>

.\Configure-EnterprisePartnerApplication.ps1 -AuthMetadataUrl '<url>' -ApplicationType <type>  

But I don´t know about the inputs thou it seems to be correct.  

Get-PartnerApplication

 

Name            ApplicationIdentifier                Realm UseAuthServer Enabled

----            ---------------------                ----- ------------- -------

Exchange Online 0000000x-0000-0xxx-xx00-000000000000       True          True

Microsoft Graph 0000000x-0000-0000-x000-000000000000       True          True

Does anyone have any ideas or links so I can move on. It's very annoying but despite this it doesn't seem to affect the users.

## Answers

_No answers on this thread._
