---
title: "Exchange Server 2019 Cannot configure mobile devices"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/419381/exchange-server-2019-cannot-configure-mobile-devic
question_id: 419381
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Server 2019 Cannot configure mobile devices

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/419381/exchange-server-2019-cannot-configure-mobile-devic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Error Message: The connection to your email server is timed out.    

Exchange Environment:     

Exchange Server 2019    

Reverse Proxy    

Edge Server    

Microsoft Connectivity Analyzer Test ActiveSync Report details,

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-03*

Hi @Al Amran       

Note:     

Since the screenshot contains your personal information, I have edited the question and covered the personal information for you.    

Please don't forget to hide your personal information in your post for security.    

Thanks for your understanding!    

As Robert mentioned, did you have a A or CNAME record in the public DNS for autodiscover.domain.com to point to the internet-facing server in your environment?    

If you have set the correct autodiscover record, can you test with Outlook on a non-domain joined device to access the mailbox?    

If Outlook doesn't work either, do you have some websites on the root domain(domain.com)?    

To narrow down the issue, you may also test with Outlook    

-  open Registry on the device which has Outlook installed    

-  locate HKEY_CURRENT_USER\Software\Microsoft\Office\x.0\Outlook\AutoDiscover    

 (x.0 in this registry path corresponds to the Outlook version (16.0 = Outlook 2016, 15.0 = Outlook 2013, 14.0 = Outlook 2010, 12.0 = Outlook 2007).)    

-  add a DWORD value named ExcludeHttpsRootDomain and set its value to 1    

-  restart Outlook and check if Outlook can connect successfully    

In addition, I noticed that you asked a similar question before:     

Outlook 2016/2019 Client Profile is not configuring from External network, don't retrieve user profile information    

I suppose the cause may be the same in this case.    

And you may need to configure a redirect on the website to redirect all the requests sent to domain.com/autodiscover to autodiscover.domain.com.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-06-02*

From the results shown, it suggest that you haven't properly configured or published the Autodiscover service.    

See; Autodiscover service in Exchange Server
