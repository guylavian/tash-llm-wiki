---
title: "exchange online aliases"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1127875/exchange-online-aliases
question_id: 1127875
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# exchange online aliases

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1127875/exchange-online-aliases (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello @Vasil Michev    and all others    

I need one quick help ...    

I have a  tenant  (eg., contoso.com)  with   Exchange Online (EOL)    

If I want to add one  more  proxy-address (alias)  on the mailbox   which is made up subdomain of  verified domain  i.e.,   abc.contoso.com  ,   is it possible ??    

Bear in mind,   abc.contoso.com   is NOT a verified domain of this tenant  because it is a verified domain of some another tenant.    

Thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-21*

Hi @testuser7   ，    

According to the relevant description of the accepted domain, if you select internal relay, your organization will accept email for all subdomains of this accepted domain.    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-16*

thanks @Aholic Liang-MSFT       

Yes, I realized.     

So  I can send email from   abc.contoso.com   domain only after adding alias made up of this domain and  in order to add such  proxy-address (alias)  I need to first add this domain as the verified domain of the tenant.    

If I do not have abc.contoso.com  as verified domain then obviously I can NOT send email using this domain.    

if somebody sends email at   john@jaswant  .contoso.com,  obviously it will not reach to John's  mailbox because there is no such proxy-address.    

But    

if I had kept   "contoso.com"  as   "accepted domain"  with  Internal-relay with "accept mail for all subdomains"  in mail-flow rule with   ,   then what will happen to the email with recepient=john@jaswant  .contoso.com,    

Thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-14*

Hi @testuser7   ，    

To make the domain name available for sending and receiving mail, you must use a verify domain of the same tenant.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
