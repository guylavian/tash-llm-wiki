---
title: "Looking for GPO to redirect rdp/port to a localhost url"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/710112/looking-for-gpo-to-redirect-rdp-port-to-a-localhos
question_id: 710112
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Looking for GPO to redirect rdp/port to a localhost url

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/710112/looking-for-gpo-to-redirect-rdp-port-to-a-localhos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have just depolyed the ManageEngine PAM product and I want to restrict RDP to only this https\localhost url:port.    

I am hoping there is a GPO config for this.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-01-27*

Pardon me for jumping in...     

I want to restrict RDP     

When you say RDP, to me that means that the client is running mstsc.exe and connecting to the server via terminal services over port 3389. The user is not running a browser, so you can't do a redirect because that's not something that mstsc.exe would understand. Or are you using RDS or some other web enabled interface?     

I am not familiar with this ManageEngine PAM product, does it provide an HTTPS enabled RDP solution? How does that product play a role in your question?    

And I don't understand the localhost portion of your question. That would imply that the client machine has already connected to something on the server (ManageEngine??)     

Perhaps if you could provide more details of "what connects to what" then someone might be able to provide an answer. And my favorite question "what's the real problem?".     

Update: Are you looking allow users to use a browser for RDP?    

https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-web-client-admin

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-26*

Simplest solution may be to create an alias record with desired name pointing to the ip address of server.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-26*

You can follow along here to change listening port.    

https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/change-listening-port    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
