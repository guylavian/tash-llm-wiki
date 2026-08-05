---
title: "Active Directory lDAPAdminLimits MaxPoolThreads in VM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/526373/active-directory-ldapadminlimits-maxpoolthreads-in
question_id: 526373
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory lDAPAdminLimits MaxPoolThreads in VM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/526373/active-directory-ldapadminlimits-maxpoolthreads-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

MaxPoolThreads MaxPoolThreads Microsoft Active Directory is a value within the LDAP policy in Active Directory that defines the maximum number of threads per-processor that a Domain Controller dedicates to listening for network input or output (I/O).

This value also determines the maximum number of threads per-processor that can work on LDAP Requests at the same time.

(source: ldap wiki https://ldapwiki.com/wiki/MaxPoolThreads)

In my VM, when I look at the Task Manager > Performance > CPU I see:

Sockets: 2  

Virtual Processors: 6

If I understood it correctly, it means I have 2 CPUs (sockets) with 3 Cores each, totalizing 6 Virtual Processors (sockets * cores = virtual processors)

I would like to know, the MaxPoolThreads will be applied to the number of Sockets or Virtual Processors?

Thanks in advance

## Answers

_No answers on this thread._
