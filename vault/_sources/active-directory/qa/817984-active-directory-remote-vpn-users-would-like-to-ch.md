---
title: "Active Directory | Remote (VPN) Users would like to change their own passwords."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/817984/active-directory-remote-vpn-users-would-like-to-ch
question_id: 817984
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active Directory | Remote (VPN) Users would like to change their own passwords.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/817984/active-directory-remote-vpn-users-would-like-to-ch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We have several users that have begun working remotely.  They establish a VPN connection via SonicWall NetExtender.   

Management would like these users to be able to change their passwords remotely.    

I have found this to be a problem. They use their home PCs to connect.  Therefore, when they hit Ctrl-Alt-Del, they are only changing the Computer Account credentials on their home PC, not Active Directory.    

Is there any way to change their Active Directory credentials remotely, besides normal password expiration?  

Thanks in advance.  

Regards,  

Rudy

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-20*

Hello @Rudolf Amarlapudi       

There's no in-built feature in AD to facilitate this, but you have different options:    

-  If using Exchange server in the environment, the users can change password from OWA    

-  Login to Remote Desktop services into a domain machine will allow to change password    

-  You can also create a Website in the domain, using an IIS server, that serves as authentication gate for the domain AD. Usually there a different 3rd party solutions that provide software that can be implemented as a Web AD authenticator server, without exposing your inner network.    

Hope this helps with your query,    

-------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-19*

Try this link: https://www.sonicwall.com/support/knowledge-base/unable-to-change-expired-password-via-netextender/170505269955697/#:~:text=Set%20the%20test%20user%20account,Click%20OK.    

Or ask them to add the Primary DNS suffix like:
