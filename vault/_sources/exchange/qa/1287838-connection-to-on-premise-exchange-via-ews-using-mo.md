---
title: "Connection to On-Premise Exchange via EWS using ModernAuth"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1287838/connection-to-on-premise-exchange-via-ews-using-mo
question_id: 1287838
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Connection to On-Premise Exchange via EWS using ModernAuth

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1287838/connection-to-on-premise-exchange-via-ews-using-mo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, 

I configured our On-Premise Exchange to work with modern authentication according this https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/enable-modern-auth-in-exchange-server-on-premises?view=exchserver-2019 

and this https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019

Now, all Outlook clients with Windows 11 are able to connect to On-Premise Exchange using Modern Authentication. Also ECP, OWA is working as expected. 

My question is related to EWS. How can I configure EWS to work with Modern authentication.  

I am able to get the access token from ADFS but when I use it in EWS call I get the error 401 Unauthorized.

Regards,

Emil

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 2 · updated: 2023-05-19*

As far as I know, EWS with Oauth only works in Exchange Online:

https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/authentication-and-ews-in-exchange

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-05-22*

Hi @ Emil Pavciak (epavciak)) ,

Yes .As Andy says, OAuth authentication for EWS is only available as part of Microsoft 365 in Exchange Online.

For specific information, please refer to this link: Authenticate an EWS application by using OAuth | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
