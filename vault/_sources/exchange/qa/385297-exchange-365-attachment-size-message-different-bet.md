---
title: "Exchange/365 attachment size message different between clients"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/385297/exchange-365-attachment-size-message-different-bet
question_id: 385297
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange/365 attachment size message different between clients

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/385297/exchange-365-attachment-size-message-different-bet (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When you try to attach a file above the exchange limit of 34MB the  outlook client will warn with a message such as "the email message cannot be sent because it exceeds the 35MB outgoing message size limit"  

I have noted windows mail and owa will say 33MB, Windows Outlook client will 35MB and Mac can be different again using the same email account. The actual outlook.com limit is 34MB.  

 I need an actual explanation/reason why this is and why windows mail/outlook web would state the limit is 33MB and Outlook windows client would state 35MB when trying to attach a file over the limit.  

This is so I can explain why different numbers are displayed depending on client when the actual limit set is 34MB as part of some research I am doing.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-05-07*

Hi @Vince Viking   ,    

Good day!    

As Leon said, the @harsh.com  .com accounts are not supported by us, we mainly talk about Exchange and other outlook client questions based on the tag.    

Could you tell me how you set the limit for Exchange to 34MB? Using Set-TransportConfig or other cmdlets?    

And also what's the Exchange version in using, is it on-prem or online?    

Based on my knowledge, the default setting for OWA is, Outlook on the web    

maxAllowedContentLength="35000000"  (byte) so it's about 33 converting to MB. You could change it by manually changing the value in Web.config file.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-05-06*

Hi @Vince Viking  ,    

Please note that Outlook.com is currently not supported in the Q&A forums, the supported products are listed over here https://learn.microsoft.com/en-us/answers/products.    

You may ask the experts in the dedicated Outlook.com forum over here:      

https://answers.microsoft.com/en-us/outlook_com/forum    

----------    

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)    

Best regards,    

Leon

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-21*

I think it is the mathematical thing (check MB for MegaByte and MiB for Mebibyte).   

The real question is - why are you depending to send the full 35 MB? Outlook may support it, but does the service, does the recipient (recipients service / recipients mail client) also support this? Is the security level good enough for this scenario?  

I am not sure if there is an actual rule, but I'll stick to the 10 MB border, as for mail. It isn't meant to transfer those masses.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-06*

Thanks - Take the outlook.com aspect out and make it more generic then, if attachment limit is set 34 on exchange, why would outlook client say 35MB whilst owa 33MB?
