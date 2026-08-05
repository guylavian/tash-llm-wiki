---
title: "kerberos authentication error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/572133/kerberos-authentication-error
question_id: 572133
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# kerberos authentication error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/572133/kerberos-authentication-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,     

I can login to any server with authentication successfully. But when come to launch or run cmd or powershell with admin privileges' access. Will throw out error with access denied. Even i'm enterprise admin or domain admin doesn't seem to have access. Only need to try authentication as different user using same account it's successfully.      

Below is the screenshot without authenticate, but i ready have enterprise admin seem not able to manage the remote server.     

Anyone encounter for kerberos authentication error?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-01*

Hello @Limitless Technology      

The issues is I'm getting kerbose authentication error, to any domain servers.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-30*

Hello @Russell Ang       

I agree that besides checking if Enterprise Admin or Domain Admin is member of the local Administrators group, you may be using an account added in "Protected Users" group.    

Since local Admin security is a concern nowadays I would recommend you to implement LAPS as a solution for centralized Local Administrator management of your environment without exposing your domain Admins groups.    

LAPS:    

https://www.microsoft.com/en-us/download/details.aspx?id=46899    

LAPS Guide:     

https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/local-administrator-password-solution-laps-implementation-hints/ba-p/258296    

Hope this helps with your query,    

--------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-09-30*

Did you check SPN configuration ?  

Please don't forget to mark helpful reply as answer

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-30*

@Thameur-BOURBITA       

I've checked security group doesn't not have protected user.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-09-30*

Hi  

Hi  

It seems that the Admin account you are using is members of protected user.  

You can remove it from protected users to be able to use ntlm protocol for authentication.  

Regarding the kerberos error, check if the SPN configuration is correct on the impacted server, if you want keep Admin account with privileged in protected users.  

Please don't forget to mark helpful reply as answer
