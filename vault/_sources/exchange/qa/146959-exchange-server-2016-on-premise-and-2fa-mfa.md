---
title: "Exchange Server 2016 On-Premise and 2FA/MFA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/146959/exchange-server-2016-on-premise-and-2fa-mfa
question_id: 146959
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Server 2016 On-Premise and 2FA/MFA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/146959/exchange-server-2016-on-premise-and-2fa-mfa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I am trying to find some specific info with regards to Exchange Server 2016 on-premise implementation and 2FA/MFA and not finding much luck.  

I have a client who is looking to implement a 2FA solution for their on-premise exchange environment. They currently have PingFederate in the environment and are implementing Symantec 2FA as the MFA provider.  

From my understanding I believe that we can implement 2FA without any problems for OWA but I have also been asked to investigate the implementation of 2FA for EWS, ActiveSync and the Outlook Mobile app.  This is where I cannot find information.   

Is it possible to implement 2FA for these services? Please advise

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2020-11-01*

Hi,  

To my knowledge, supported services for MFA in Exchange on-premise are OWA/ECP. There are various methods to achieve this,  

-  Using ADFS  

-  Cloud based - Azure  

-  Reverse proxy + cloud based - for instance, reverse proxy can be integrated with NPS for RADIUS and using NPS extension on that server for secondary authentication in Azure  

-  Third party products like PingFederate/Duo and that has the clear documentation on the product itself for configuring MFA for Exchange on-premise  

http://msexchangeguru.com/2017/01/16/secure-owa-ecp-with-mfa/  

https://practical365.com/exchange-server/exchange-web-services-bypass-multi-factor-authentication/  

https://social.msdn.microsoft.com/Forums/en-US/d28e3947-0a19-44d9-b39f-db9a4f6c21f3/mfa-on-premises-exchange-2016?forum=windowsazureactiveauthentication  

If the above suggestion is helpful, please click on "Accept Answer" and Upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-03-08*

Hi,  

I had the same challenge and ended using DUO 2FA for Exchange 2016 OWA on premise, the setup and configuration was straightforward  

owa

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-11*

I also am being tasked with 2FA for OWA onprem Exchange 2016 server. I already have 2FA established throughout the domain and remote users with hardware Yubikey Smart cards. I was hoping I could use these same cards rather than having to now support an additional 2FA solution. Is it possible within exchange 2016 On Prem or 2019 Server to support Hardware Tokens FIDO2 ??? Is there any kind of support for my yubikeys to do 2fa for OWA or am I stuck with having to purchase additional solution?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-29*

@Ashok M      

My specific goal is to implement 2FA for On-Prem Exchange 2019 multi-tenant.  Above you said the goal could be accomplished by various methods.  I'm specifically interested in 1. Using ADFS and 2. Cloud based - Azure.  I can find articles that talk about these topics but not specifically how to accomplish my goal.  Can you give more info on options 1 and 2 please?    

Thanks!!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-02*

Hi @Dhillan Kalyan   ,    

I agree with what AshokM-8240 said.    

In addition, if you use a third-party product to set up MFA for ActiveSync and Outlook on mobile, please note that there are requirements for your mobile system. For specific restrictions, please refer to the instructions of each product.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
