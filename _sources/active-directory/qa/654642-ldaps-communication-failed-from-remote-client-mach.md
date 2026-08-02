---
title: "LDAPS communication Failed From Remote (Client) Machine."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/654642/ldaps-communication-failed-from-remote-client-mach
question_id: 654642
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# LDAPS communication Failed From Remote (Client) Machine.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/654642/ldaps-communication-failed-from-remote-client-mach (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Team,   

I configured LDAPS using documents from online. Connection works fine in local machine using Ldp.exe tool.  

But I couldn't connect from other same network machines. I can able to ping IP and telnet to port 636. Ldp.exe and other application communication "Failed to Connect".  

I solved errors reg connection from Event logs too.   

can anyone help me with any reference doc or assistance?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-09*

Hi there,    

This issue is the result of a non-default domain policy set in the active directory that enforces all LDAP authentication to be secured with SSL. You can use some of the troubleshooting methods to sort this out.    

-Verify the Server Authentication certificate    

-Verify the Client Authentication certificate    

-Check for multiple SSL certificates    

-Verify the LDAPS connection on the server    

For detailed troubleshooting methods, you can use the below link    

Troubleshoot LDAP over SSL connection problems    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/ldap-over-ssl-connection-issues    

-----------------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-12-07*

Hi @Ajith Berlin       

Have a look at this article that provides details on how to troubleshoot LDAPS connection issues.    

https://nettools.net/howto-troubleshoot-ad-ldaps-connection-issues/    

Gary.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-12-07*

I'd check the required ports are flowing between networks.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts#windows-server-2008-and-later-versions    

https://www.microsoft.com/en-us/download/details.aspx?id=24009    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
