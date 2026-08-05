---
title: "Kerberos Authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/830175/kerberos-authentication
question_id: 830175
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Kerberos Authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/830175/kerberos-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have searched over Internet for Configuring Kerberos in Windows Server 2016/19 but could not find satisfactory links or videos. Can anyone help me with tutorial for the same using which I can configure it in my Server  

Please advise!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-30*

I am already aware. But if I troubleshoot as per the KB in log viewer it does not show authentication as Kerberos but as firewall authentication and Auth. Type as AD  

So I am on Microsoft Community as to how to configure Kerberos auth in Server.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-29*

Hi   

The configuration of the firewall to support kerberos authentication is specific to the firewall and not the AD.  Here is an article from Sophos website on configuring kerberos.  If you need more help or information I would try their support community.  

https://docs.sophos.com/nsg/sophos-firewall/19.0/Help/en-us/webhelp/onlinehelp/AdministratorHelp/Authentication/HowToArticles/AuthenticationKerberosTurnOn/index.html#add-an-active-directory-server

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-29*

Frankly speaking I am new to this concept but   

I have Firewall named Sophos where in it supports Kerberos + If I configure the firewall as proxy I can configure it in browser with Kerberos settings in browser.   

Plus it has other features which can be helpful in firewall if Kerberos configured.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-28*

No!  

AD is already in place  

Need to configure Kerberos Authentication instead

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-04-28*

Hi,   

By Kerberos authentication, you mean Active Directory configuration ? If yes, some link Setting up Active Directory in Windows Server 2019 (Step By Step Guide)
