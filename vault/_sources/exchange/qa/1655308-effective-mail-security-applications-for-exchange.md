---
title: "Effective Mail Security applications for Exchange 2019 on-prem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1655308/effective-mail-security-applications-for-exchange
question_id: 1655308
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Effective Mail Security applications for Exchange 2019 on-prem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1655308/effective-mail-security-applications-for-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I currently use Symantec Mail Security for Microsoft Exchange on our on-prem Exchange 2019 environment but am looking for a new product.  The environment is not connected to the Internet, but on a large stand alone network and I initially wondered if Microsoft Defender for Endpoint would be suitable in this situation.  I know it is good for Exchange Online, and after some initial investigation, it looks as though it would work for an on-prem environment, but I am after some confirmation this would work.

I would also be interested in other suggestions for other Exchange security applications people may have (Symantec Mail Security for Exchange could previously be updated using its Intelligent Updater files, however the later versions need to access Live update (or in my case an internal Live Update Administrator installation, which is not viable on our network).

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-15*

Agreed with @Jake. Considering your Exchange Server 2019 environment and the limitations regarding internet connectivity, Microsoft Defender for Endpoint might not be the most suitable option as it heavily relies on cloud-based features for optimal performance.

However, you can explore alternative mail security solutions  for on-premises environments. Before making a decision, ensure to evaluate each solution's compatibility with your Exchange server environment, ease of deployment, management capabilities, and overall effectiveness in meeting your security requirements.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-15*

Hello @Chris48,

Based on your description, I'd like to explain that while Microsoft Defender for Endpoint does provide protection for on-premises Exchange servers, it is primarily an endpoint security solution designed to help prevent, detect, and respond to advanced attacks that could compromise your network . threaten. For Exchange specifically, Microsoft offers Exchange online protection, which is designed to protect your email environment. However, it's worth noting that the service is primarily cloud-based and typically requires an internet connection to take advantage of all features, such as real-time updates of the latest threat intelligence. As for the non-networked environment you mentioned, I have no right to recommend third-party software to you. If possible, you can try connecting your environment to the Internet and try Exchange online protection. For specific operations, refer to the following documents:https://www.yisu.com/zixun/25575.html
