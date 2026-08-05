---
title: "Microsoft Learn and installing Active Directory Domain Structure Network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194462/microsoft-learn-and-installing-active-directory-do
question_id: 2194462
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-network-connectivity-file-sharing"]
---
# Microsoft Learn and installing Active Directory Domain Structure Network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194462/microsoft-learn-and-installing-active-directory-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear community,

good afternoon.

I am very happy with the Microsoft Learn possibilities. I doubt that there is anyone who can get the better of me regarding the theory. But when I try to get some hands on practice nothing ever works. I understand how it is. That all are free to learn as much as they like, but when you want to put it to work there must be someone who did it all already and needs to point you to what is not found through learning. The system makes it perfectly impossible for one to learn on its own and put anything to use. Thus where is that person that points me to a working Active Directory Domain Structure network?

Mst recently I used the netsh firewall set icmpsetting type=all mode=disable

And nothing ever works.

Thank you in advance.

Yours sincerely,

Bjarne Petersen

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-18*

Hi,

Thank you for your reply. I suggest you open cmd as an administrator and run the following command to check whether the teredo service is disabled. 

netsh int Teredo show state 

If it is disabled, run the following cmd command to see if it can solve the problem. 

netsh interface Teredo set state disable 

netsh int ter set state enterpriseclient

Best Regards

Zunhui

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-17*

Dear ZunHui,

good afternoon.

Easy. I've added -t to the command thus I am seeing it right now:

PING: transmit failed. General failure.

Yours sincerely,

Bjarne Petersen

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-17*

Hello,

What problem did you encounter when configuring the AD domain? The cmd command you ran is to enable the ICMP setting on the firewall so that the device allows incoming or outgoing ICMP communication. I hope you can describe it in detail so that we can troubleshoot the problem.

Best Regards

Zunhui
