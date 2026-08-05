---
title: "Deactivate of IPv6 on domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191248/deactivate-of-ipv6-on-domain-controllers
question_id: 2191248
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-networking-other"]
---
# Deactivate of IPv6 on domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191248/deactivate-of-ipv6-on-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello community,

Is there an official stance on deactivating IPv6 on domain controllers if IPv6 is generally deactivated in the network anyway? advantages disadvantages? Please share if official documentation is available

Unfortunately I can't find any suitable articles 

Best Regards

## Answer (community) — community member

*upvotes: 1 · updated: 2023-11-10*

Hello,

Uncertain whether you've had a chance to review this article: IPv6 for the Windows Administrator: Why you need to care about IPv6 - Microsoft Community Hub

The article provides a strong case for why administrators should care about IPv6 and not disable it. Microsoft's guidance, as highlighted in the article, is to enable and support IPv6 rather than disabling it.

Here's a summary of the pros and cons of enabling or disabling IPv6 on domain controllers and servers, based on the discussions online and Microsoft's recommendations:

Advantages of Enabling IPv6:

1.IPv6 works well with new technology and keeps your network compatible with the latest advancements.

2.It prepares your network for changes because IPv6 is the way forward.

-  It's like having both IPv4 and IPv6 on standby, which is smart.

-  Sometimes, IPv6 makes things run smoother and safer.

Disadvantages of Enabling IPv6

It might seem a bit more complicated, especially if you're not used to it. In some cases, it can reduce confusion during troubleshooting.

Regards,

Karlie
