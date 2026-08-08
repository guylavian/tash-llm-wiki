---
title: "Upgrade Azure AD Connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289599/upgrade-azure-ad-connect
question_id: 1289599
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Upgrade Azure AD Connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289599/upgrade-azure-ad-connect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have AD Connect version 1.6.16.0 on Windows Server 2012 R2 Datacenter. I am going to upgrade to the current version of AD Connect. I know I need to build a new Windows (2019) server and do a swing migration from what I have been reading. Since I have never done this before, I am looking for step-by-step instructions on how to do the migration. I have found a couple of docs, but they are different. Anyone have any experience doing the swing migration? Are there any good instructions that I could follow?

Thanks,

JP

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-23*

Hello,

Thanks for the reply. But I am looking for information on how to do a swing migration of the Azure Ad Connect software that syncs our on-premise directory to Azure. We have a hybrid environment. We are running Windows Server 2012 with AD Connect version 1.6.16.0. I can't upgrade the AD Connect software since the operating system is too old. I need to build a new server running 2019, install the new version of the Azure AD Connect Sofware. Since I have not done this, I am looking for good step-by-step instructions on how to accomplish this without any issues. 

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-23*

Hello Jimmie,

Thank you for your question and for reaching out with your question today.

Please carry out the following steps in order to migrate 2012 R2 to 2019

-  Prepare Windows Server 2012 R2 (existing AD DC).

adprep

forestprep

domainprep

gpprep.

-  Freshly install Windows Server 2019 on new hardware.

Standard configuration of a server:

Assign hostname

fixed IP assigned

Set NTP

Install AD role on Destination Server

Promote Windows Server 2019 as an ADC

-  Perform replication between both DCs.

-  Transfer FSMO roles to Windows Server 2019

-  Transfer all other role configuration files manually from 2012 to 2019. (Here is my biggest uncertainty, because these procedures are not described anywhere).

-  Remove Windows Server 2012 R2 Essentials from all AD services and all other roles.

If the reply was helpful, please don’t forget to upvote or accept as answer.

Best regards.
