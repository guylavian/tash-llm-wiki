---
title: "Mail queues remain in the exchange server after shift isp primary to secondary"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2140018/mail-queues-remain-in-the-exchange-server-after-sh
question_id: 2140018
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Mail queues remain in the exchange server after shift isp primary to secondary

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2140018/mail-queues-remain-in-the-exchange-server-after-sh (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All experts,

Good day,

We had an exchange in 2019. Exchange-server-1 and Exchange-server-2. If I assign internet from the primary isp, through the firewall. Then it works fine. But when I turn off the primary. And switch to a secondary isp, then all mail queues remain in the exchange server.

When I shift to primary, everything works fine. So I need your help and advice in this. We use the Sonicwall 3650 model as a firewall.

When a client sends a mail, it goes from server 1 to server 2 and then goes out or it doesn’t go out

When the primary isp is up mail works properly. but when I apply secondary link mails not work it is stuck in queue

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-03*

Hi, @Amol Pande  

Given that everything is fine when you assign internet from the primary isp through the firewall, the exchange server should not be a problem.

The problem may be in the way the Sonicwall 3650 firewall handles traffic.

Based on this situation it is recommended that you perform the following troubleshooting:

1.Ensure that both Exchange servers are able to resolve DNS names when using a secondary ISP. You may need to configure the DNS settings on the server or firewall to use the public DNS servers when the secondary ISP is active.

2.Ensure that the SonicWall 3650 has the necessary rules to allow outbound SMTP traffic (typically TCP port 25) when using the secondary ISP. Check to see if there are any restrictive rules that only allow outbound mail traffic to flow through the primary ISP.

3.Verify that NAT policies are properly configured for both ISPs. Ensure that NAT rules exist to handle outbound traffic for mail services when using the secondary ISP.

4.Check the firewall logs for any errors or blocked traffic when switching to the secondary ISP.

5.If possible temporarily disable the firewall and test with the secondary ISP to see if there are any errors.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
