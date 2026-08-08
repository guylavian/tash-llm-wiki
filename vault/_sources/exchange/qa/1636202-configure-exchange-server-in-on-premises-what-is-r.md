---
title: "Configure Exchange server in on-premises ? what is requirement"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1636202/configure-exchange-server-in-on-premises-what-is-r
question_id: 1636202
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Configure Exchange server in on-premises ? what is requirement

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1636202/configure-exchange-server-in-on-premises-what-is-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want configure the exchnage server on-premises, then what reuirement like mx record or if suppose mail communication external server then what will do on premise ?

Please guide us

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-29*

Configuring Microsoft Exchange Server on-premises requires careful planning and consideration of various requirements. Here are the key requirements and considerations:

-  MX Record:    You need to create an MX (Mail Exchange) record in your DNS settings that points to the public IP address of your Exchange server. This record tells other mail servers where to deliver email messages for your domain.

-  External Communication:    Ensure that your Exchange server has a public IP address or is behind a firewall/NAT device with port forwarding configured to forward SMTP (port 25) traffic to the Exchange server.    If your Exchange server is behind a firewall, you need to configure firewall rules to allow incoming SMTP traffic from the internet to reach the Exchange server.    Obtain a valid SSL/TLS certificate for your Exchange server to enable secure communication (HTTPS) with clients and other mail servers. This certificate should match the hostname used for accessing Exchange services (e.g., mail.example.com).

-  Domain Configuration:    Configure your Exchange server to accept email for your domain(s). This involves adding accepted domains and configuring email address policies.    Ensure that your internal DNS infrastructure is configured to resolve external domain names (e.g., example.com) to their public IP addresses.

-  Internet Connectivity:    Ensure that your Exchange server has reliable and continuous internet connectivity to send and receive emails. Consider redundant internet connections for high availability.

-  SPF Record:    Consider publishing SPF (Sender Policy Framework) records in DNS to specify which servers are authorized to send emails on behalf of your domain. This helps prevent email spoofing and improves email deliverability.

-  Reverse DNS (PTR) Record:    Some email servers perform reverse DNS lookups to verify the sender's identity. Ensure that your ISP configures a reverse DNS (PTR) record for your Exchange server's public IP address.

-  Security and Compliance:    Implement security best practices to protect your Exchange server from unauthorized access, malware, and spam. This includes regularly applying security updates and patches.    Configure Exchange server settings for compliance with industry regulations and company policies regarding email retention, archiving, encryption, and data protection.

-  Testing and Monitoring:    Perform thorough testing of your Exchange server configuration to ensure that it can send and receive emails successfully.    Set up monitoring and alerting to detect and respond to issues promptly, such as email delivery failures or abnormal server behavior.

Details at https://learn.microsoft.com/en-us/exchange/plan-and-deploy/plan-and-deploy?view=exchserver-2019

If the above response helps answer your question, remember to "Accept Answer" so that others in the community facing similar issues can easily find the solution. Your contribution is highly appreciated.

hth

Marcin
