---
title: "Exchange 2019 EWS connection issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1029103/exchange-2019-ews-connection-issue
question_id: 1029103
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 EWS connection issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1029103/exchange-2019-ews-connection-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I install a second Exchange in the domain another exchange 2019 server (to change vm). When I open ews I find an error "server encountered an error while retrieving tracking information from https://server:444/EWS/Exchange.asmx. If I try to open the url localy it works but if I try from the other exchange server ..can't reach this page.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-03*

Few pointers which you need to look at.    

1 - What is your Exchange CU version? According to my research, similar problems occurred in earlier versions of Exchange. If your Exchange version is lower, please upgrade Exchange to a newer version.    

2 - Please run the following command to check whether the Url settings of the EWS virtual directory are correct:      

```
Get-Webservicesvirtualdirectory -showmailboxvirtualdirectories | fl Identity,*url*
```

3 - Delivery reports for administrators uses the Exchange admin center (EAC) to perform a targeted search of the message tracking logs. So please make sure the message tracking logs usually exist.    

4 - Please try to run the following commands to remove and recreate the EWS virtual directory:    

```
Remove-WebServicesVirtualDirectory -Identity <>  
New-WebServicesVirtualDirectory -WebSiteName <> -InternalUrl <> -ExternalUrl <>
```

5 - Please check any related error logs in the event viewer.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

Port 444 suggest that the EWS back end site seems to be the culprit at least.    

Give it a go to recreate the webservices virtual directory on the new box, it tend to shake stuff like this loose.    

Here is a reasonable guide I found for you.    

https://www.alitajran.com/recreate-virtual-directories-in-exchange-server/#h-why-you-want-to-recreate-exchange-virtual-directories    

Let me know if it works please :)    

Got a couple of other ideas but this would be my first.    

Cheers
