---
title: "Event ID 2008 warning from Event Source MSExchange OAuth appearing randomly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/126533/event-id-2008-warning-from-event-source-msexchange
question_id: 126533
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Event ID 2008 warning from Event Source MSExchange OAuth appearing randomly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/126533/event-id-2008-warning-from-event-source-msexchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The following two event log entries are appearing once or twice a month seemingly at random. They will spam us with hundreds of warnings for about a day and then stop. It has happened on 10/14/2020, 10/6/2020 and 9/15/2020 – 9 /16/2020. It has happened a couple other times also, but I don’t have the dates. They started after we configured our Exchange Organization in a hybrid configuration and enabled OAuth. Our Microsoft Exchange Server Auth Certificate is valid.  

Log Name:      Application  

Source:        MSExchange OAuth  

Date:          10/14/2020 10:42:30 AM  

Event ID:      2008  

Task Category: Configuration  

Level:         Warning  

Keywords:      Classic  

User:          N/A  

Computer:      <Exchange_Server>  

Description:  

When retrieving metadata from the url 'https://login.windows.net/<Our_Domain_Name>/federationmetadata/2007-06/federationmetadata.xml', different certificate(s) have been found.  

Log Name:      Application  

Source:        MSExchange OAuth  

Date:          10/14/2020 10:42:30 AM  

Event ID:      2008  

Task Category: Configuration  

Level:         Warning  

Keywords:      Classic  

User:          N/A  

Computer:      <Exchange_Server>  

Description:  

When retrieving metadata from the url 'https://accounts.accesscontrol.windows.net/<Our_Domain_Name>//metadata/json/1', different certificate(s) have been found.

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-10-15*

@Allen Terry       

Do you have other partner applications that have the certificate imported? You may have to remove the partner application and re-configure it.    

```
Get-PartnerApplication  
Remove-PartnerApplication   
.\Configure-EnterprisePartnerApplication.ps1 -AuthMetadataUrl '' -ApplicationType 
```

Here are similar issues for your reference:    

Exchange 2016 / Skype for Business - MSExchange OAuth Error,    

Exchange 2013 Partner Applications and Error 2008.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-10-15*

Hi @Allen Terry       

I see this all the time and now just ignore them. There doesnt seem to be an actual issue.    

Sometimes this clears it for awhile and its perfectly safe to run:    

    Get-Federationtrust | Set-FederationTrust –RefreshMetadata  

Others have seen this as well:    

https://techcommunity.microsoft.com/t5/exchange/exchange-oauth-different-certificate-s-have-been-found/m-p/1450541
