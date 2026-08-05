---
title: "How do I see LDAPS status on a Windows DC ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/391291/how-do-i-see-ldaps-status-on-a-windows-dc
question_id: 391291
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
---
# How do I see LDAPS status on a Windows DC ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/391291/how-do-i-see-ldaps-status-on-a-windows-dc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello experts, We have 2 Server 2016 Domain Controllers in our environment and the both should be running LDAPS. They were both working last year. I updated the certificates on both of them about a month ago, but now only one is working for LDAPS connections. I'm not sure why the 2nd server stopped working. On my bench computer, if I run  u the LDP.exe test tool or use the command openssl.exe s_client -connect <DCNAME>:636 I can see the cert on the 1st DC, and make a good connection, but I get an error on the other server and cannot connect. Looking at the certificates MMC console, I can see both servers have current and valid certificates so I am really confused why the one stopped working when all I did was replace the certs.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-12*

Hi,  

Thank you for posting in our forum.  

I am glad that your problem has been solved by yourself.  

Thank you also for sharing the method, if you can, you can make your own answer.  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-11*

I got this sorted out finally. I had to use the certutil and certreq commands on the local machine to create a new private key and get the cert signed in order for it to work. Apparently using a remote MMC snap in created some issues and either I did not have access to the key or something.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-11*

I should also mention that our server is Windows Server Core and I am managing the certs remotely using the MMC snap in. So I feel like something is not updating correctly. Also When I use the openssl.exe s_client connect command, the error is 10054 no peer certificate available like the 2nd DC doesn't have a private key or something. It's really confusing.
