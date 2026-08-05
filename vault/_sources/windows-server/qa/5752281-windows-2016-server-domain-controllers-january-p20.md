---
title: "Windows 2016 server Domain controllers January p2026 patches causing sync issues"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5752281/windows-2016-server-domain-controllers-january-p20
question_id: 5752281
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Windows 2016 server Domain controllers January p2026 patches causing sync issues

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5752281/windows-2016-server-domain-controllers-january-p20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

After i patched my domain controllers with the January 2026 patches i am having issues with replication, ldap queries, and rpc stopping due to excessive memory usage.  

Is there a OOB patch to fix this issue?.  I have reviewed all the the replication it is working but due to the excessive memory it stops the services.

Is there any known issues.  i had the servers on different esx hosts, i combined them on to one server

## Answer (community) — community member

*upvotes: 0 · updated: 2026-01-30*

It appears that you are experiencing issues with Active Directory replication, LDAP queries, and RPC services after applying the January 2026 patches to your Windows Server 2016 domain controllers. While the specific out-of-band (OOB) patch for this issue is not mentioned in the provided context, there are general troubleshooting steps you can take to address excessive memory usage and replication issues:

-  Check Memory Usage: Monitor the memory usage of your domain controllers. High memory usage can lead to replication failures and service interruptions. Ensure that the physical memory is adequate for the load.

-  Investigate Resource Depletion: Look into potential causes of memory depletion, such as low available physical memory, paging file issues, or exhaustion of the paged/non-paged pool. You can use Performance Monitor to analyze memory usage and identify any leaks or excessive consumption.

-  Review Active Directory Performance: Utilize tools like Performance Monitor and Resource Monitor to check for high CPU and memory usage, and ensure that the Ntds.dit and edb.log files are active as expected.

-  Replication Traffic Monitoring: If you suspect that high replication traffic is causing issues, consider monitoring the replication traffic and adjusting the environment accordingly. You can use commands like `repadmin /showreps` to gather detailed information about replication status.

-  Consult Microsoft Support: If the issues persist, it may be beneficial to open a service request with Microsoft support for further assistance, especially if you suspect that the patches have introduced new issues.

As for known issues related to the January 2026 patches, the provided context does not specify any, so checking Microsoft's official documentation or support channels for updates on this matter would be advisable.

References:

-  Troubleshooting AD Replication error 8477: The replication request has been posted; waiting for reply

-  Troubleshooting AD Replication error 8446: The replication operation failed to allocate memory
