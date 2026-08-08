---
title: "No kerberos tgt ticket after unlock screen"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/906029/no-kerberos-tgt-ticket-after-unlock-screen
question_id: 906029
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# No kerberos tgt ticket after unlock screen

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/906029/no-kerberos-tgt-ticket-after-unlock-screen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an application which need kerberos tgt ticket, and I need that client computer contains tgt when user is logon.    

(Client: WIN10, Server: Windows Server 2012)    

After the user logons the computer, we can see the ticket by using klist command.     

    

You can see that the client caches 3 tickets after the user logon.    

However, when I try to lock screen and logon again, all the tickets disapear and regenerate no one.    

    

Using Windows Network Monitor, we can find that the behavior of unlocking screen and logon is the same.    

They all go through kerberos protocol AS request->AS response->TGS request->TGS response......    

But in the end, client computer doesn't store tgt after unlocking screen. It's so weird.    

    

I have searched for many forum about this question but still have no idea why Microsoft designed this mechanism.    

Can someone expalain it and tell me how to auto-regenerate tgt after unlock screen?

## Answer (community) — community member

*upvotes: 1 · updated: 2022-06-30*

Hi there,    

This is by design. There is no way to prevent the Kerberos service ticket(s) from being purged after a screen lock. As soon as you access a new Kerberos-protected resource again, a new authentication procedure takes place and new tickets will appear.     

It is important to understand a distinction between Kerberos tickets - there are two types - the ticket-granting ticket (TGT) and the service ticket (ST). You can ensure that the Kerberos TGT remains in the client cache and does not clear out after a screen lock if your computer is participating in an Active Directory domain and you make what is known as a Group Policy change in order to change the behaviour.    

Hope this resolves your Query !!    

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

If the reply is helpful, please Upvote and Accept it as an answer

## Answer (community) — community member

*upvotes: 1 · updated: 2022-06-29*

Hi @Gary Reynolds  ,    

For my application, I will trigger something when the client goes through kerberos AS request,    

so the different behavior of unlock screen and logon bothers me a lot.     

I think your answer haven't solved my question but still thank for your reply, and here I list a real case example.    

For example:    

(1) If user logoff after he unlocks screen, client has no TGT    

He will go through whole the kerberos event (as->tgs), so my application will trigger. But this is not what I want.    

(2) If user logoff without unlocking screen, client holds TGT    

He will go through kerberos event (tgs), and my application will not trigger. This is the correct operation I want.    

As my understanding,  AS response ticket from server contains TGT ticket(Protocol Description from Wiki), and client will cache the TGT in AS response for further service.     

https://en.wikipedia.org/wiki/Kerberos_(protocol)    

User logon event will cache TGT, and unlock screen will not.(They all go through whole kerberos as -> tgt)    

This is the weird point I think, and I want to know the reason.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-28*

Hi @鴻明 劉  ,    

This network traffic is normal for a TGT exchange, the client will first try and connect without authentication and pre-authentation required response is sent from the server with the accepted authentication methods, client then tries again with a supported authentication method.    

You don't really need to have the TGT ticket cached before the user accesses the service.  If the service is setup to use Kerberos, the client will request the required TGT and TGS tickets.  You just need to make sure you have the correct SPN configured on the service.    

Here are some examples of SPNs https://social.technet.microsoft.com/wiki/contents/articles/717.service-principal-names-spn-setspn-syntax.aspx    

Gary.
