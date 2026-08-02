---
title: "Setup Exchange Server 2019 on Azure VM with Azure Load Balancer"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2133680/setup-exchange-server-2019-on-azure-vm-with-azure
question_id: 2133680
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Setup Exchange Server 2019 on Azure VM with Azure Load Balancer

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2133680/setup-exchange-server-2019-on-azure-vm-with-azure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am required to setup exchange client access service availability through azure internal load balancer

I am required to migrate exchange server onpremises to azure vm, there is a VPN setup that passes traffic from onpremises to azure datacenter using VPN to Hub Landing Zone FW to Exchange in Spoke.

I would like to setup publishing each virtual directory and also want to disable basic and ntlm authentication for exchange.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-19*

Hi @Syed Wasil Uddin，

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, you want to migrate your local Exchange server to Azure VM; set up Exchange Client Access service availability through Azure Internal Load Balancer and set up publishing each virtual directory, disabling Exchange Basic Authentication and NTLM Authentication.

First of all, regarding migrating your local Exchange server to Azure VM, you need to join the Azure VM to the domain of the local Exchange server you mentioned and install the exchange server.

Regarding setting up Exchange Client Access service availability through Azure Internal Load Balancer, you need to set it up as per your load balancer configuration.

If you want to disable Exchange Basic Authentication and HTLM Authentication, you can try the following methods:

You can do this through the EAC by selecting Server > Virtual Directory, then selecting the virtual directory settings you want to configure and deselecting Basic Authentication in the Authentication tab.

Refer to: Disable Basic authentication on Exchange Server virtual directories | Microsoft Learn

View or configure Outlook on the web virtual directories in Exchange Server | Microsoft Learn

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne
