---
title: "Exchange Web Services replies with version Exchange 2015"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/183580/exchange-web-services-replies-with-version-exchang
question_id: 183580
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Web Services replies with version Exchange 2015

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/183580/exchange-web-services-replies-with-version-exchang (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!  

I just came across a very interesting situation and hope someone here can help me fix it. I installed an Exchange Server 2016 to migrate vom SBS 2011. Everything fine there. All the mailboxes have been moved to the new server, but the old one hasn't been uninstalled yet. A co-worker is configuring an achriving software that accesses the Exchange Server using EWS. He can connect and sees the mailboxes, but can not archive them. This ist the Error he gets in his logs:  

2020/12/01 10:24:11 138 [014] [i] [TryAutodiscover] ErrorCode: NoError  

2020/12/01 10:24:11 138 [014] [i] [TryAutodiscover] resolved  

2020/12/01 10:24:11 138 [014] [i] [GetUserSettings] autodiscover completed  

2020/12/01 10:24:11 142 [014] [i] [USRSETTING.Dump] EwsSupportedSchemas : Exchange2007, Exchange2007_SP1, Exchange2010, Exchange2010_SP1, Exchange2010_SP2, Exchange2013, Exchange2013_SP1, Exchange2015  

2020/12/01 10:24:11 144 [014] [i] [GetBestExchangeVersion] request highest version in Exchange2007, Exchange2007_SP1, Exchange2010, Exchange2010_SP1, Exchange2010_SP2, Exchange2013, Exchange2013_SP1, Exchange2015  

2020/12/01 10:24:11 144 [014] [i] [GetBestExchangeVersion] highest EWS version for XcService@<Customer Domain>: Exchange2015  

....  

2020/12/01 10:24:11 994 [014] [F] [EWSLOG] msg : Exchange Server doesn't support the requested version.  

2020/12/01 10:24:11 994 [014] [F] [EWSLOG] src : ELOxc  

2020/12/01 10:24:11 994 [014] [F] [EWSLOG] type: Microsoft.Exchange.WebServices.Data.ServiceVersionException  

2020/12/01 10:24:11 994 [014] [e] [LogonService] administrative exchange login failed  

Can someone pleeeeezzzz explain to me how an Exchange Server 2016 can reply as an Exchange Server 2015? (Btw. it is the newest CU!)  

I've been working with Exchange as an MCT/MCSE for over twenty years and never seen anything like this. Does anyone here have a solution?  

Thanks in advance for your support.  

Best Regards,  

Gerrit

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-03*

Whats interesting about that is it appears to be expected? or normal? or something .lol  

https://github.com/EmilTholin/node-exchange-autodiscover/blob/master/README.md

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-03*

Hello EricYin-MSFT,  

my question IS about EWS, not about the archiving software. After all it is EWS that is saying that it is version Exchange 2015 NOT the archiving software. That is why I'm asking here. (BTW. The support of the archiving software said to ask Microsoft, so "Did that, bin there." ;) )  

The software uses autodiscover to access EWS. That part works fine, but then somehow EWS responds as Exchange 2015. How can that be? Where could I check to see what exactly EWS is sending back to the other software?  

Best Regards,  

Gerrit

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-03*

Hi,    

Our forum focus on on-premise Exchange issues. It seems your question is more about the “achriving software that accesses the Exchange Server using EWS”, have you met any issues about EWS? Such as free busy look up, calendar sharing, mail tips and OOO?    

I suppose you should ask for support from the software first, or go to Development forum since it’s related to Exchange.WebServices.Managed.Api.    

Thanks for your understanding.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
