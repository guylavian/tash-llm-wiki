---
title: "exchange migration from 2010 to 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/414762/exchange-migration-from-2010-to-2016
question_id: 414762
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange migration from 2010 to 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/414762/exchange-migration-from-2010-to-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have installed exchange 2016 to coexist with exchange 2010 and all went according to plan but when i opened exchange 2016 owa to log into a mailbox that still is on exchange 2010 it doesn't redirect but return this error "internal server error 500"  

does anyone have any idea on this?  

Thanks   

Regards,  

Chris

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-31*

Hi @Christian Abou Haidar   ,    

Can you login to EAC as usual?    

And please check if the MS Form-Based Authentication Service is running, if not, please start it manually.    

Please try the following methods:    

-  Reset the OWA Virtual Directory and restart IIS.     

-  Try enabling the sub-features of .Net 3.5 and .Net 4.5, except Named pipe activation through Server Manager>Add roles and features>Select Features    

-  Change the MSExchangeECPAppPool from .NET Framework from v4.0 to v2.0 and restart IIS.    

To reset the OWA VD, you can run these cmdlets in EMS, or use EAC to reset it.    

Remove-OwaVirtualDirectory -Identity "EXCH01\owa (Default Web site)"    

New-OwaVirtualDirectory -InternalURL https://mail.contoso.com/owa    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
