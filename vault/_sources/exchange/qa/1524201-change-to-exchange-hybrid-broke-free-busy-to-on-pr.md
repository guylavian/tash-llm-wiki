---
title: "Change to Exchange Hybrid broke Free/busy to on-prem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1524201/change-to-exchange-hybrid-broke-free-busy-to-on-pr
question_id: 1524201
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Change to Exchange Hybrid broke Free/busy to on-prem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1524201/change-to-exchange-hybrid-broke-free-busy-to-on-pr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have inherited an Exchange environment and my predecessor left without doing a handover or any documentation. Everything I will provide here, I have had to figure out myself, and there are some gaps.

We have a complicated setup. We are owned by a parent company, and this company has their own tenant. They want to run most O365 services from their tenant. Due to this our Teams accounts are in their tenant. This was the only integration I was aware of between us and their tenant. We have our own tenant, and but we only use it for Azure services. The business wants to start using our tenant for O365 services like Teams, EXO etc.

For reasons unknown to me, our on-prem Exchange was previously connected (via Hybrid) to this other EXO tenant. I will call this tenant “old tenant” going forward. I only became aware of this after I ran the HCW to connect it to our tenant, and this has caused some issues since doing so.

Previously, a user in the old tenant could access our on-prem EXCH mailboxes free busy info. This means the HCW has successfully set up organisation sharing policies between both EXCH orgs. After running the HCW and connecting to our tenant, the users in the old tenant can no longer connect to see free/busy in our on-prem EXCH mailboxes. Here is the strangest part – our Teams accounts (which I mentioned above) can still access our on-prem mailboxes. The reason I mention this is that we can rule out some service being broken; if you read the Teams documentation here, I am going to assume that the pre-reqs must be good as Teams works. This should rule out issues with OAuth and Autodiscover not being available.

I have checked everything I can think of. When I run the RCA tool and select the “test free/busy on-prem” (the one that tests if an EXO user can see free/busy on-prem) we get the following error. This suggests there is an issue with OAuth, I think. But, I can’t find any issue with it. NOTE: the guid (which I have removed) is the GUID assigned to their tenant, not ours, which I assume is expected since the request is coming from them.

 
`Autodiscover failed for email address <ON-PREM email address> with error System.Net.WebException: The request failed with HTTP status 401: Unauthorized.`
`at System.Web.Services.Protocols.SoapHttpClientProtocol.ReadResponse(SoapClientMessage message, WebResponse response, Stream responseStream, Boolean asyncCall)`
`at System.Web.Services.Protocols.SoapHttpClientProtocol.EndInvoke(IAsyncResult asyncResult)`
`at Microsoft.Exchange.SoapWebClient.AutoDiscover.DefaultBinding_Autodiscover.EndGetUserSettings(IAsyncResult asyncResult)`
`at Microsoft.Exchange.InfoWorker.Common.Availability.SoapAutoDiscoverRequest.<>c__DisplayClass48_0.<EndInvoke>b__0()`
`at Microsoft.Exchange.InfoWorker.Common.Availability.SoapAutoDiscoverRequest.ExecuteAndHandleException(ExecuteAndHandleExceptionDelegate operation) and diagnostics 2000009;reason="The issuer of the token is unknown. Issuer was '00000001-0000-0000-c000-000000000000@<TENANT GUID REMOVED>'.";error_category="invalid_issuer"., inner exception: System.Net.WebException: The request failed with HTTP status 401: Unauthorized.`
`at System.Web.Services.Protocols.SoapHttpClientProtocol.ReadResponse(SoapClientMessage message, WebResponse response, Stream responseStream, Boolean asyncCall)`
`at System.Web.Services.Protocols.SoapHttpClientProtocol.EndInvoke(IAsyncResult asyncResult)`
`at Microsoft.Exchange.SoapWebClient.AutoDiscover.DefaultBinding_Autodiscover.EndGetUserSettings(IAsyncResult asyncResult)`
`at Microsoft.Exchange.InfoWorker.Common.Availability.SoapAutoDiscoverRequest.<>c__DisplayClass48_0.<EndInvoke>b__0()`
`at Microsoft.Exchange.InfoWorker.Common.Availability.SoapAutoDiscoverRequest.ExecuteAndHandleException(ExecuteAndHandleExceptionDelegate operation), diagnostics: 2000009;reason="The issuer of the token is unknown. Issuer was '00000001-0000-0000-c000-000000000000@<TENANT GUID REMOVED>'.";error_category="invalid_issuer"`

It seems to me that our EXCH servers do not trust their O365 tenant. But this cannot be true because nothing has changed their side, I can only assume something on our server changed so that it would no longer trust their tenant. Can anyone advise where to start looking to figure this out, and confirm if this errors seems like it could be OAuth? But then again, if it is OAuth, then how can Teams be working since the documentation says OAuth is a pre-req?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-20*

Hi @Graham Allen  ,

I fixed this myself.

Glad to know the issue has been resolved!

Thank you so much for sharing the solution so others with the same issue can easily reference it, even though the issue is more unique and uncommon! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer :)

[Change to Exchange Hybrid broke Free/busy to on-prem]

Problem symptoms:

After running the HCW and connecting to our tenant, the users in the old tenant can no longer connect to see free/busy in our on-prem EXCH mailboxes.

Resolution:

"If you do, the fix is to remove this object with: remove-authserver -identity [id of the WindowsAzureACS object] Then recreate it with:  

New-AuthServer -Name "WindowsAzureACS" -AuthMetadataUrl "https://accounts.accesscontrol.windows.net/<your tenant coexistence domain>/metadata/json/1" Where the tenant name is the OLD tenant. EXCH on-prem now trusts OAuth tokens from the other tenant"

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-07*

I fixed this myself. My issue is very nuanced.
When running the HCW, it overwrites an AuthServer object called "WindowsAzureACS". This is in relation to OAuth authentication. When a user in another EXO org trires to connect to your on-prem EXCH free/busy it does so with an OAuth token. Exchange must trust the issuer of the token. In our case, this AuthServer was overwritten with the settings on our new EXO tenant, so on-prem no longer trusted the old tenant. This is a very unique situation most people will not come up against. If you do, the fix is to remove this object with:
remove-authserver -identity [id of the WindowsAzureACS object]
Then recreate it with:  

New-AuthServer -Name "WindowsAzureACS" -AuthMetadataUrl "https://accounts.accesscontrol.windows.net/<your tenant coexistence domain>/metadata/json/1"
Where the tenant name is the OLD tenant. EXCH on-prem now trusts OAuth tokens from the other tenant

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-02-05*

Hello @Graham Allen  ,

After running the HCW and connecting to our tenant, the users in the old tenant can no longer connect to see free/busy in our on-prem EXCH mailboxes.

Could you clarify that do the users in the old tenant refer to the all on-prem users?
Based on the error message you provided, it seems that there may be an issue with the OAuth configuration between the local Exchange server and the old tenant. One possible solution is for you to first check the OAuth configuration settings on the Exchange server and make sure they are properly configured to trust the old tenant. You could check the status of an existing OAuth certificate by running the following command in the Exchange Management Shell: (Get-AuthConfig).CurrentCertificateThumbprint | Get-ExchangeCertificate | Format-List

Besides, have you tried running the Hybrid Configuration Wizard again? If possible, you could try running the Hybrid Configuration Wizard again to see whether it can solve the problem.

Alternatively, you could follow the steps in the link below to troubleshoot:
https://support.microsoft.com/en-us/topic/how-to-troubleshoot-free-busy-issues-in-a-hybrid-deployment-of-on-premises-exchange-server-and-exchange-online-in-office-365-ae03e199-b439-a84f-8db6-11bc0d7fbdf0
https://learn.microsoft.com/en-us/exchange/troubleshoot/calendars/troubleshoot-freebusy-issues-in-exchange-hybrid

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
 Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
