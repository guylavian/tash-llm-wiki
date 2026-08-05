---
title: "Server 2025 Domain controller does not boot properly - how to fix?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2276308/server-2025-domain-controller-does-not-boot-proper
question_id: 2276308
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Server 2025 Domain controller does not boot properly - how to fix?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2276308/server-2025-domain-controller-does-not-boot-proper (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Upgraded the domain controller in place from Server 2019 to Server 2025 on a Hyper-V machine. The process went smoothly with no errors, but the server does not want to boot properly. After the domain controller boots, it is attached to a private network instead of a domain network. If I stop the network interface and restart it, it will attach to the domain network and then other computers can authenticate using this domain controller. I goggled this problem and it seems that there is a race condition on boot for the NLA service. I tried to add dependencies for the NLA service and, added start delay for the service, but nothing seems to really fix this problem. Also, with server 2025, we cannot turn off the windows update service, so this MS controlled server is rebooting all the time and then not connecting to the domain. Anybody have a solution that will fix this issue?

BTW, Microsoft seems to have directed all the phone numbers to an AI bot, which directs people back to their support hub page, but that page has been down and reporting errors for the past month. Microsoft developers constantly surprise me with their constant push towards AI and copilot, and yet they cannot detect that their support hub web page is down!!!!

Error provided: "Oops, A problem occurred and our engineers have been notified. Please try again later. (1 month later and still doesnt work)

## Answers

_No answers on this thread._
