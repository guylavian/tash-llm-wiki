---
title: "Kerberos Authenication Across Domain Trusts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194482/kerberos-authenication-across-domain-trusts
question_id: 2194482
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 3
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Kerberos Authenication Across Domain Trusts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194482/kerberos-authenication-across-domain-trusts (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there a document that explains how to make this work?

I have setup domain trusts from DOMAIN A to DOMAIN B as Forest Type / Transitive.

When I try to connect to a file share on DOMAIN B from a PC on DOMAIN A it wants to use NTLM.

When NTLM is blocked via GPO it just fails to access the share.

It does work from a PC on DOMAIN B to Share on DOMAIN B and PC on DOMAIN A to Share on DOMAIN A

## Answer (community) — community member

*upvotes: 4 · updated: 2024-01-22*

1st link does not work

other's are of no real use

## Answer (community) — community member

*upvotes: 3 · updated: 2024-10-16*

These documents are about creating trusts between a non-Windows Kerberos realm for AWS EMR or Informatica (whatever that is) and NOT about accessing SMB shares across a transitive Windows trust using Kerberos auth only.

I get really tired of people that purport to work for MSFT giving "answers" that do not address the question at all.

Also, while I'm not concerned about what language people use in general, if a question is asked and responded to in one language (English in this instance), it's only polite to provide links to info in the same language (unless there is literally no alternative). Both sites both provided an EN version, but unless you know what to look for, switching language is not immediately obvious.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-22*

Hi Peter,

I apologize for the wrong link. Here is the correct link to the documentation on Kerberos authentication across domain trusts:     

https://docs.informatica.com/zh_cn/data-quality-and-governance/data-quality/10-5/_security-guide_data-quality_10-5_ditamap/GUID-1239AF64-F67F-489A-B36F-681CBEA3F6B2/GUID-10F49A8B-1AB7-4DA0-A1DF-F21C9BF2D191.html

https://docs.aws.amazon.com/zh_cn/emr/latest/ManagementGuide/emr-kerberos-cross-realm.html

They provide details on how to configure Kerberos authentication across domain trusts, including troubleshooting tips for common issues.

Best regards

Qiuyang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-18*

Hi Peter,

Yes, there is Microsoft documentation that explains how to configure Kerberos authentication across domain trusts. You can refer to the following articles for more information:  

https://docs.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-over-forest-trust-topologies  https://learn.microsoft.com/en-au/troubleshoot/windows-server/windows-security/kerberos-authentication-troubleshooting-guidance  https://learn.microsoft.com/windows-server/security/kerberos/kerberos-authentication-overview     

The article provides step-by-step instructions on how to configure Kerberos authentication across domain trusts, including troubleshooting tips for common issues. It is important to note that both domains must be configured to use Kerberos authentication and have the necessary trust relationships to work properly.

Best regards

Qiuyang
