---
title: "When I try to connect to domain controller, I get network not found message."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198980/when-i-try-to-connect-to-domain-controller-i-get-n
question_id: 2198980
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-networking-other"]
---
# When I try to connect to domain controller, I get network not found message.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198980/when-i-try-to-connect-to-domain-controller-i-get-n (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I try to connect to domain controller, I get network not found message, I also can't access my Sysol or Netlogon

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-15*

Hello Gregory,

Hope you have a lovely day!

There could be several reasons why you are unable to connect to the domain controller and access Sysvol or Netlogon. Here are some troubleshooting steps you can try:

-  Check your network connection: Make sure that your computer is connected to the network and that you have a valid IP address.

-  Check DNS settings: Ensure that your computer is using the correct DNS server address. You can check this by running the command "ipconfig /all" in the command prompt.

   

-  Check firewall settings: Make sure that the firewall on your computer is not blocking the connection to the domain controller. You can temporarily disable the firewall to see if it resolves the issue.

   

-  Check domain controller status: Verify that the domain controller is up and running. You can check this by pinging the domain controller's IP address.

-  Check domain membership: Ensure that your computer is a member of the domain. You can check this by going to the System Properties and checking the Computer Name tab.

If none of these steps resolve the issue, you may need to contact your network administrator or Microsoft support for further assistance.

Best Regards

Rosy
