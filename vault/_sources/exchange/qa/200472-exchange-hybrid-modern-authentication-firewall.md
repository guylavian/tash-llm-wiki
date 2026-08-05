---
title: "Exchange hybrid modern authentication firewall"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/200472/exchange-hybrid-modern-authentication-firewall
question_id: 200472
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange hybrid modern authentication firewall

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/200472/exchange-hybrid-modern-authentication-firewall (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a question about hybrid modern authentication.    

When we want to setup hybrid we can choose to allow only traffic from office 365 endpoints as described here:    

https://learn.microsoft.com/en-us/exchange/hybrid-deployment-prerequisites#hybrid-deployment-protocols-ports-and-endpoints    

When I want to enable hybrid modern authentication, and allow laptops to connect to exchange on prem, do I need to further open the firewall? Are there seperate firewall requirements for modern authentication in exchange on prem? Or are these the same as for "normal" hybrid exchange?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-17*

@Jeroen Bonsel       

The hybrid Modern Authentication still using 443 port: Using hybrid Modern Authentication with Outlook for iOS and Android    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-16*

Hi,    

Yes, Exchange on-premise requires connection with Office365 endpoints. Please refer the below documents,    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide#microsoft-365-common-and-office-online    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/hybrid-modern-auth-overview?view=o365-worldwide#do-you-meet-modern-authentication-prerequisites    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/configure-exchange-server-for-hybrid-modern-authentication?view=o365-worldwide#using-hybrid-modern-authentication-with-outlook-for-ios-and-android    

If the above suggestion helps, please click on "Accept Answer" and upvote it
