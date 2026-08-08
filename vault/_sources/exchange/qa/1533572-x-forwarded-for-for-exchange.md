---
title: "X-FORWARDED-FOR for Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1533572/x-forwarded-for-for-exchange
question_id: 1533572
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-development-iis"]
answer_author_roles: ["Microsoft Moderator"]
---
# X-FORWARDED-FOR for Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1533572/x-forwarded-for-for-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. Haproxy + Exchange 2019 on-premise. I am using Haproxy for client balancing.  

Haproxy does not pass the address of the client, but of the server itself. I can see it in IIS logs.  

After researching Haproxy, I found parameters to enable real IP address transmission.  

I followed the recommendations in this article: https://techcommunity.microsoft.com/t5/iis-support-blog/how-to-use-x-forwarded-for-header-to-log-actual-client-ip/ba-p/873115.  

But this did not result in success.  

How can I get the real address of the client ?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-16*

Hi @Андрей Михалевский  ，

After researching Haproxy, I found parameters to enable real IP address transmission.

According to this blog, X-Forwarded-For Header (XFF) requires to be enabled on your Proxy or Load balancer prior to adding this field in IIS:  

So, I'd like to confirm, by "found parameters to enable real IP address transmission", do you mean you've already followed the guidance from Haproxy to enable it?

Besides, I found a thread below which includes a working haproxy.cfg file shared by the poster, you can have a look at it to see if it can be of some help:  

haproxy and forwarding client IP address to servers
(Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)

In addition, considering that the issue involves IIS, I'll add the IIS tag so that their community can look into this issue as well.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
