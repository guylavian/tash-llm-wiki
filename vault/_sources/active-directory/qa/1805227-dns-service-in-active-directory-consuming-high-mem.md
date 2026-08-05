---
title: "DNS Service in Active Directory Consuming High Memory and Crashing on Azure VM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1805227/dns-service-in-active-directory-consuming-high-mem
question_id: 1805227
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["azure-virtual-machines", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# DNS Service in Active Directory Consuming High Memory and Crashing on Azure VM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1805227/dns-service-in-active-directory-consuming-high-mem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts,

I'm experiencing a persistent issue with the DNS service in Active Directory on an Azure VM. Despite scaling the VM from 16 GB RAM to 32 GB, the DNS service continues to consume high memory and eventually crashes. 

Here are the details:

Environment:

VM Configuration: Standard D8s v3 (8 vcpus, 32 GiB memory) [Azure VM with 32 GB RAM ]

Operating System:  Windows (Windows Server 2022 Standard)

Active Directory and DNS Role: Running on the same VM

Issue Description:

The DNS service consumes high memory, leading to performance degradation.

The service eventually crashes, causing DNS resolution failures.

Scaling the VM from 16 GB to 32 GB RAM did not resolve the issue.

Troubleshooting Steps Taken:

Checked DNS logs and Event Viewer for errors or warnings.

Ensured the system is up-to-date with the latest patches and updates.

Configured DNS forwarders to offload external queries.

Adjusted DNS cache settings and reduced logging levels.

Reviewed DNS zones and resource records for unnecessary entries.

Monitored performance using PerfMon and Sysinternals tools.

Scanned for malware and unauthorized changes.

Verified that the VM size is appropriate for the workload.

-  Ensured disk I/O is not a bottleneck.

-  Despite these efforts, the issue persists. 

I am looking for expert advice on the following:

Potential causes for high memory consumption by the DNS service.

Best practices for optimizing DNS configuration in Active Directory.

Any specific tools or methods to diagnose and resolve memory leaks in the DNS service.

Recommendations for managing DNS services in a large environment on Azure.

I appreciate any guidance or suggestions you can provide.

Thank you!

Saurabh ✌

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-22*

It's also a problem on vmware VM and physical server installations!

Also with cumulative update kb5055526 (04.2025) installed.

Immediately after the restart the dns server service uses more than 1.7gb ram  and it gets more every day

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-12*

Hello,

 

Thank you for posting in Q&A forum.

This issue may caused by Azure VM memory pressure.

It's recommended to use PerfInsights , which can provide an Azure VM best practices diagnosis in a user-friendly report. With this tool you can capture a trace with details inside for troubleshooting.

How to download: https://www.microsoft.com/en-us/download/details.aspx?id=54915

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-10*

Hi Saurabh Sutone  ,

Welcome to the Microsoft Q&A Platform! Thank you for asking your question here.

We understand from your query that you are experiencing an issue with the DNS service in Active Directory consuming high memory and crashing on an Azure VM.

This issue might be caused by a memory leak in the DNS server process.

The DNS cache size could be too large, leading to high memory consumption. You can try resolving this by adjusting the MaxCacheSize registry value.

If you are still facing issue, I would suggest filing a support case to investigate this matter further. The support team will be able to examine and assist with resolving the issue.
