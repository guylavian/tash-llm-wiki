---
title: "Exchange Hybrid eDiscovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/242612/exchange-hybrid-ediscovery
question_id: 242612
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Hybrid eDiscovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/242612/exchange-hybrid-ediscovery (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Just running a test in my lab environment. It consists of Exchange 2010, 2013 and 2016 (all latest CU). Everything (web services etc) points to 2016 on prem.  

When trying to perform an ediscovery (from 2016) as a user with the Discovery Management role for a mailbox in 365, it fails with the error "Estimate Failed" in the console and digging deeper it says "Object reference not set to an instance of an object."  

In event viewer on the Exchange box, there is the below error:  

The description for Event ID 10052 from source Exchange Discovery Search cannot be found. Either the component that raises this event is not installed on your local computer or the installation is corrupted. You can install or repair the component on the local computer.  

If the event originated on another computer, the display information had to be saved with the event.  

The following information was included with the event:   

https://autodiscover-s.outlook.com/autodiscover/autodiscover.svc  

System.Net.WebException: The request failed with HTTP status 400: Bad Request.  

   at System.Web.Services.Protocols.SoapHttpClientProtocol.ReadResponse(SoapClientMessage message, WebResponse response, Stream responseStream, Boolean asyncCall)  

   at System.Web.Services.Protocols.SoapHttpClientProtocol.EndInvoke(IAsyncResult asyncResult)  

   at Microsoft.Exchange.SoapWebClient.AutoDiscover.DefaultBinding_Autodiscover.EndGetUserSettings(IAsyncResult asyncResult)  

   at Microsoft.Exchange.InfoWorker.Common.MultiMailboxSearch.UserSettingAutodiscovery.UsersettingsDiscoveryCompleted(IAsyncResult result)  

2438ce81-1006-4758-b200-270f1f1164a2  

the message resource is present but the message is not found in the string/message table  

I have confirmed and tested oAuth and that is successful both ways.  

Im at a loss at to what to check next. Any advice greatly appreciated

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-24*

Hi Andy,  

Thanks for the response.  

I've just checked my lab and I dont appear to have a discovery mailbox for some reason? I assume its just a case of recreating it.  

The customer Im testing this for has a lot of mailboxes on prem and in 365 so want a single console to be able to search on both platforms easily,  

Thanks for the prompt response. Gives me something to work on.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-23*

I always recommend running discovery/searches  "local" to where the mailboxes are and not run them from on-prem EAC for 365 mailboxes, I have simply found it works better that way. Use on-prem for on-prem mailboxes and the SCC for 365 mailboxes.    

Just curious though.. Where is your discovery mailbox on-prem? Can you move it back to 2013 and see if that works?    

https://learn.microsoft.com/en-us/office365/troubleshoot/ediscovery/cannot-run-ediscovery-search-cloud-mailbox
