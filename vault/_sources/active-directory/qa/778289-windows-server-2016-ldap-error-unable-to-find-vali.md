---
title: "Windows Server 2016 ldap error unable to find valid certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/778289/windows-server-2016-ldap-error-unable-to-find-vali
question_id: 778289
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Windows Server 2016 ldap error unable to find valid certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/778289/windows-server-2016-ldap-error-unable-to-find-vali (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Experts, We have an LDAPS server that is Windows Server 2016 that has multiple certificates in it's computer store. Recently, one of the certs was renewed by our issuing CA. It's not publicly signed so it is creating a problem with an LDAPS service. The cert that is publicly signed is still in the computer, but for some reason it is not being used to establish the LDAPS connection any more. We have one service provider that is no longer using the correct certificate that is publicly signed, but instead using the new one that is locally signed. Is there any way to force our LDAPS server to use the previous cert that was working that is publicly sign to restore the LDAPS service?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-03-18*

Hi,    

You should assign the LDAPS certificate  to active directory service on domain controller. This certificate will be used only for LDAPS connection :    

    

    

    

    

    

Please don'y forget to mark helpful reply as answer
