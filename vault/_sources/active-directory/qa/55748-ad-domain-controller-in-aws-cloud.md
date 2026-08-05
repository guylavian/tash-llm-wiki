---
title: "AD Domain controller in AWS cloud"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/55748/ad-domain-controller-in-aws-cloud
question_id: 55748
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# AD Domain controller in AWS cloud

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/55748/ad-domain-controller-in-aws-cloud (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, We are in phase of deploying an AD domain controller in AWS. We are using third party DNS i.e. Infoblox. What are the pre-requisites do we need to fulfil before deploy a DC in AWS. We have root and child structure i.e. root.local and child domain is corp.domain.com. The reason to ask this question is currently facing an issue with that in our lower environment. It has the same parent child domain structure i.e. root.local and child domain is corp.domain.com, and only difference is that in lower environment we having AD integrated DNS. When we deployed the DC in corp.domain.com in lower environment everything is working fine, all the test shows no errors. But there is one issue came to know that AWS DC is not in the list of replication partners. When I checked repadmin /replsum from an On-prem DCs, getting 1722 RPC error for AWS DC, and from AWS DC no RPC error and it is not in the Source DSA but in the Destination DSA. AWS team has opened all the AD ports. Any suggestion?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-07-31*

Hello pintokumar16,    

Thank you for posting here.    

The most common issues for 1722 RPC error are related to:    

-  Network Connectivity    

-  DNS     

-  AD ports     

Especially, high dynamic port range ports 1025 through 5000(the default port range for Windows Server 2003) and ports 49152 through 65535(the default port range beginning with Windows Server 2008), we should check on DC both on-premise and AWS.    

For AD port requirements, we can refer to the link below.    

Active Directory Replication over Firewalls    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727063(v=technet.10)?redirectedfrom=MSDN    

Active Directory and Active Directory Domain Services Port Requirements    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772723(v=ws.10)?redirectedfrom=MSDN    

For more information about troubleshooting 1722 RPC error, we can refer to the following two links.    

Active Directory Replication Error 1722: The RPC server is unavailable    

https://support.microsoft.com/en-us/help/2102154/active-directory-replication-error-1722-the-rpc-server-is-unavailable    

Windows Server Troubleshooting: RPC server is unavailable    

https://social.technet.microsoft.com/wiki/contents/articles/4494.windows-server-troubleshooting-rpc-server-is-unavailable.aspx    

We can check with the network team in your company.    

Best Regards,    

Daisy Zhou
