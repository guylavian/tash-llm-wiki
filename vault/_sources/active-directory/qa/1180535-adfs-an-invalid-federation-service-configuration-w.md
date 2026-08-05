---
title: "ADFS: an invalid Federation Service configuration when request from intranet"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180535/adfs-an-invalid-federation-service-configuration-w
question_id: 1180535
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS: an invalid Federation Service configuration when request from intranet

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180535/adfs-an-invalid-federation-service-configuration-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear all,

I have installed the PBIRS and config it to authentication through WAP and ADFS, so I followed the instruction on ms document (https://learn.microsoft.com/en-us/power-bi/report-server/connect-adfs-wap-report-server).

The problem is when I request report.company.com/reports from the internet, everything works as expected, but I'll get an error "The incoming sign-in request is not allowed due to an invalid Federation Service configuration." when I request the same URL from the internal network or use the VPN.

My workaround is to re-check all configurations on PBIRS, WAP, and ADFS, and I have no idea what's wrong. I  searched around Stackoverflow and learn.microsoft.com and found no answer to my problem. And I also compared the URL that redirects into ADFS between requests from the internal network and the internet and realized that both URLs are the same, as shown below. Still, an error occurred only when requested from the internal network.

/adfs/ls?version=1.0&action=signin&realm=urn'%'3AAppProxy'%'3Acom&appRealm=ee591f40-053e-ec11-90f0-005056b358f2&returnUrl=https'%'3A'%'2F'%'2Freport.company.com'%'2Freports&client-request-id=F3F0E577-2E0A-0007-0D70-F9F30A2ED901 

For more information about configurations,

-  ADFS has the public domain as adfs.company.com, but different IP resolved when requested from the internet and intranet (public and private IP)

-  The domain report.company.com points to the public IP of WAP for both intranet and internet.

-  As I mentioned, other configurations were set up step by step in the ms document.

I need help. I appreciate and welcome any ideas.

Thank you,

Sopanawit Pi

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-02-20*

@Sopanawit Pichidtienthum   ,

Adding onto @Pierre Audonnet - MSFT  kindly validate the access control policy on ADFS.

-  While adding the application group what access policy was configured for intranet.

Thanks,

Akshay Kaushik
