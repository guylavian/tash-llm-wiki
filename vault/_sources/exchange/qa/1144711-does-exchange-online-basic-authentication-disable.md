---
title: "Does Exchange Online Basic authentication Disable by Microsoft will impact to BizTalk POP3 Adapter Basic Authentication?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1144711/does-exchange-online-basic-authentication-disable
question_id: 1144711
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["biztalk-server", "office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Does Exchange Online Basic authentication Disable by Microsoft will impact to BizTalk POP3 Adapter Basic Authentication?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1144711/does-exchange-online-basic-authentication-disable (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We are using the POP3 Adapter in BizTalk Server 2020 for Polling email from Exchange Online(Office365) Mail Server.    

Microsoft given the statement in the below site and saying that "Starting on October 1, 2022, Microsoft is starting to disable an outdated way of logging into Exchange Online known as 'basic authentication', Exchange Online starting January 2023 when we permanently disable basic authentication".    

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-online-email-applications-stopped-signing-in-or-keep/ba-p/3641943    

Based on the above statement, The BizTalk POP3 adapter Basic Authentication also will impact?     

The above site suggesting to move OAuth modern authentication but in BizTalk POP3 adapter is not having the OAuth Authentication Scheme.    

All we tried to change the Authentication Scheme from Basic to SPA and Digest but we are getting the below error.    

SPA:    

 The adapter "POP3" raised an error message. Details "The POP3 server does not support the specified authentication scheme.     

 Please change the scheme to the one supported by POP3 server.     

 URL: POP3://outlook.office365.com     

 Scheme: SPA     

 Error: -ERR Protocol error. 14 ".    

Digest:    

 The adapter "POP3" raised an error message. Details "The POP3 adapter could not authenticate using the supplied credentials.     

 Please change the scheme and supplied credentials.     

 URL: POP3://outlook.office365.com     

Error: +OK The Microsoft Exchange POP3 Service is ready.    

Could you please help to assist on this issue and possible way of implement OAuth for the POP3 Adapter in BizTalk.    

Regards,    

Devanand Sekar

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-29*

You need to start using the Office 365 Outlook Email adapter

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-28*

Yes, BizTalk will need to support creating an application in Azure to authenticate with POP. You probably need to talk to their support    

See:    

https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-28*

Yes, POP3 is affected. BizTalk will need to move to an Oauth/Modern Authentication method for this to work.
