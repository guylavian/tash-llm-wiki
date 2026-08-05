---
title: "ADFS and WAP reverse proxy."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5635764/adfs-and-wap-reverse-proxy
question_id: 5635764
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS and WAP reverse proxy.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5635764/adfs-and-wap-reverse-proxy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm new to proxy configuration.

I want to implement ADFS SAML/SSO configuration for a cloud application but unfortunately the internal domain is not exposed to internet. But for some reason is i cannot achieve. 

WAP server domain is publicly resolvable. Added DNS record from my public DNS to WAP server's public IP.

e.g., wap.contoso.com

ADFS domain is in intranet 

e.g., adfs.contosolocal.com

I've done firewall,dns and published ADFS endpoint in WAP. But while accessing wap.contoso.com from internet or intranet always cause 404. Both the servers are in Azure Vnet as VMs in different subnets.

Some one guide me how to achieve the SAML for this scenario?

Thank you!

## Answers

_No answers on this thread._
