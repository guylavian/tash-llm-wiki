---
title: "Exchange Hybrid (Teams Calendar)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/195976/exchange-hybrid-teams-calendar
question_id: 195976
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-teams-teams-business-other-l1"]
---
# Exchange Hybrid (Teams Calendar)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/195976/exchange-hybrid-teams-calendar (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good evening,    

Been racking my brain around this and the MS documentation is not clear (to me at least).  Hoping to find a nugget here that can help with the current hurdle.    

Current State:    

Downloaded and ran through the HCW on one of our Exchange servers.  Hit a snag with Federation not getting enabled, so we knocked that out.  Seems to have worked just fine (box checked).    

Teams Calendar Issue    

Open Teams and when we click on Calendar we see the infamous "Couldn't load your calendar" error.  Currently this is our only focus and I'm having trouble zeroing in on what to check as every article seems to go down a never ending link to pages that don't necessarily seem related.    

Note:  Prior to enabling Federation we could not do user lookups.  Now, we can at least perform user lookups in the attendees field, but we also receive text below their name stating "Unknown".    

Is there a better site to help identify the correct source Exchange Online URLs we need to white list?  The link below looked correct at first, but the information lists that these ports are ONLY for On-Prem to EXO connections.      

https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide#skype-for-business-online-and-microsoft-teams    

Are the Exchange Online & Skype for Business Online and Microsoft Teams URLs provided in that link all trying to hit our EWS virtual directory?    

Exchange Web Services (EWS Endpoints):    

InternalUrl         : https://mail.domain.com/EWS/Exchange.asmx     TCP 443    

ExternalUrl        : https://mail.domain.com/EWS/Exchange.asmx      TCP 443    

Lastly, if our autodiscover URL is autodiscover.domain.net (internal only), will we be forced to add a public autodiscover.domin.com (public) A record to make it all works or will our EWS provide the connection for autodiscover?    

Thanks for any information or guidance you can provide.    

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

Good afternoon Jimmy.  

Finally was able to try and break down your reply and look more closely at our current configuration and wanted to run a couple of things by you if I may.  

So it seems that Hybrid Modern Authentication is required  (based upon the link you provided).  Makes sense as does most of the article, but when I review the section labelled "Add on-premises web service URLs as SPNs in Azure AD", the cmdlets it specifies are all MSOL based.  As I understand it, MSOL was replaced by the newer Exchange module "ExchangeOnlineManagement" using the connect-ExchangeOnline cmdlet to get started.  Is that correct?  I could install the older MSOL module with no issues, but importing it was never possible as the get-module command never showed it installed in the first place (even though the progress bar indicated success).  Can I just ignore those MSOL commands since they appear to be deprecated?  

Lastly,  if the MSOL commands have been replaced, what would the commands be using the ExchangeOnline module?  Is that an option?  

Get-MsolServicePrincipal -AppPrincipalId 00000002-0000-0ff1-ce00-000000000000 | select -ExpandProperty ServicePrincipalNames   

Thanks much sir.
