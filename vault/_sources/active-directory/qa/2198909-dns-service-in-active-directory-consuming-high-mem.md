---
title: "DNS Service in Active Directory Consuming High Memory and Crashing on Azure VM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198909/dns-service-in-active-directory-consuming-high-mem
question_id: 2198909
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# DNS Service in Active Directory Consuming High Memory and Crashing on Azure VM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198909/dns-service-in-active-directory-consuming-high-mem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts,

I'm experiencing a persistent issue with the DNS service in Active Directory on an Azure VM. Despite scaling the VM from 16 GB RAM to 32 GB, the DNS service continues to consume high memory and eventually crashes. Here are the details:

-  Environment:

-  VM Configuration: Standard D8s v3 (8 vcpus, 32 GiB memory) [Azure VM with 32 GB RAM ]

-  Operating System:  Windows (Windows Server 2022 Standard)

-  Active Directory and DNS Role: Running on the same VM

-  Issue Description:

-  The DNS service consumes high memory, leading to performance degradation.

-  The service eventually crashes, causing DNS resolution failures.

-  Scaling the VM from 16 GB to 32 GB RAM did not resolve the issue.

-  Troubleshooting Steps Taken:

-  Checked DNS logs and Event Viewer for errors or warnings.

-  Ensured the system is up-to-date with the latest patches and updates.

-  Configured DNS forwarders to offload external queries.

-  Adjusted DNS cache settings and reduced logging levels.

-  Reviewed DNS zones and resource records for unnecessary entries.

-  Monitored performance using PerfMon and Sysinternals tools.

-  Scanned for malware and unauthorized changes.

-  Verified that the VM size is appropriate for the workload.

-  Ensured disk I/O is not a bottleneck.

- 

Despite these efforts, the issue persists. I am looking for expert advice on the following:

-  Potential causes for high memory consumption by the DNS service.

-  Best practices for optimizing DNS configuration in Active Directory.

-  Any specific tools or methods to diagnose and resolve memory leaks in the DNS service.

-  Recommendations for managing DNS services in a large environment on Azure.

I appreciate any guidance or suggestions you can provide.

Thank you!

Saurabh ✌

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-09*

Thank you, Daisy.

I have posted this in Questions - Microsoft Q&A.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-09*

Hello Saurabh Sutone,  

Thank you for posting in Microsoft Community forum.  

From the description above, I understand your question is related to DNS issue on Azure VM.   

Since there are no engineers dedicated to DNS issue on Azure VM in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and type "Azure DNS" tag and select any tags related to your productions.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
