---
title: "How to get domain controller certificate?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/457321/how-to-get-domain-controller-certificate
question_id: 457321
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# How to get domain controller certificate?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/457321/how-to-get-domain-controller-certificate (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The dcdiag output is full of No suitable default server credential exists on this system. This will prevent server applications that expect to make use of the system default credentials from accepting SSL connections. An example of such an application is the directory server. Applications that manage their own credentials, such as the internet information server, are not affected by this.  

```
A warning event occurred.  EventID: 0x00009016
```

I like to clear this clutter.   

https://social.msdn.microsoft.com/Forums/en-US/eef6a9cc-8d5d-4477-8b4c-49b1b0bd6498/no-suitable-default-server-credential-exists-on-this-system?forum=winserverDS  

says I need a domain controller certificate. How do I get domain controller certificate?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-30*

Do you have a CA in your environment? Are you using SSL to establish secure connections?    

If no, just ignore the warning.    

If yes, that means that no server certificate was found so you have to issue a certificate to this server.    

https://learn.microsoft.com/en-US/troubleshoot/windows-server/networking/troubleshoot-missing-sysvol-and-netlogon-shares    

Hope this information can help you    

Best wishes    

Vicky
