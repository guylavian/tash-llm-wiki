---
title: "PKI on 2012 servers with 2019 Domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/170712/pki-on-2012-servers-with-2019-domain-controllers
question_id: 170712
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# PKI on 2012 servers with 2019 Domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/170712/pki-on-2012-servers-with-2019-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

We currently have a 2012 AD domain with PKI on 2012 servers. We are looking at upgrading the AD domain to 2019,  can we leave the PKI services on the existing 2012 servers or does this need to be migrated to 2019 servers the same as the new Domain  

Im not sure if theres any compatibility issues between the both if they are on different OS  

Thanks in advance!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2020-11-23*

Hi,  

Based on my research, we don't need to migrate the CA from the member server to the 2019 DC when you upgrade the DCs.  

Just keep the CA on the member server.  

If you also want to upgrade the CA server , you can consider migrate it to a 2019 member server ,not necessary to a DC.  

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-migrating-the-active-directory-certificate-service/ba-p/697674  

Best Regards,

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-11-21*

Hi,  

You don't need to migrate PKI on 2012 to another OS , to be able to upgrade the domain controller to Windows 2019.  

a Domain controller on windows 2019 support a member server on Windows server 2012.  

Please don't forget to mark this reply as answer if it help you to fix your issue
