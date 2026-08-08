---
title: "SCCM 2207 and Secondary site or DP role (create new System Site Server)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1005525/sccm-2207-and-secondary-site-or-dp-role-create-new
question_id: 1005525
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
---
# SCCM 2207 and Secondary site or DP role (create new System Site Server)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1005525/sccm-2207-and-secondary-site-or-dp-role-create-new (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I want to ask what the best praxis to have a second DP. A Secondary Site Server or a new System Site Server?

I would like to prefer to create a new Site System Server(new DP).

Are there a step by step guide for new System Site Server?

I can image that I have to do the following steps:

1) install a new Windows Server 20xxx on physical machine, call the machine "SCCM22" , join the domain  

2) Install roles , Remote Differential Compression, IIS Configuration, ISAPI Extensions,

Then on the existing SCCM server, "create Site System Server"  

Put there the new installed "SCCM22"

Is that so correct?

Could you say that is like high availability of SCCM?

Regards

## Answer (community) — community member

*upvotes: 1 · updated: 2022-09-14*

Hi @PerserPolis-1732  ,

Thanks for your information.

1) In my experience, each distribution point supports connections from up to 4,000 clients. If you are in this scenario, we can install DP on the new server directly.

2) Based on your steps, we should add the SCCM site server Computer account to the Local Administrators group on the new DP server before Create Site System Server.  

3) Besides, before we install a new Configuration Manager Distribution Point, the following prerequisites are required.  

• Windows Server Roles and Features  

• Remote Differential Compression  

• IIS Configuration  

• Application Development  

• ISAPI Extensions  

• Security: Windows Authentication  

• IIS 6 Management Compatibility: IIS 6 Metabase and IIS 6 WMI Compatibility.  

• Visual C++ Redistributable

To support PXE or multicast on ConfigMgr DP:  

• Enable a PXE responder on a distribution point without Windows Deployment Service.  

• Install and configure the Windows Deployment Services (WDS) Windows Server role.  

• For a multicast-enabled distribution point, make sure the SQL Server Native Client is installed and up to date.

This guide for your reference:  

How to Install SCCM Distribution Point | ConfigMgr DP (prajwaldesai.com)  

Note: Microsoft provides third-party contact information to help you understand the problem. This contact information may change without notice. Microsoft does not guarantee the accuracy of this third-party contact information.

4) The difference with normal installation, for high availability, we cannot install the distribution point role on both the active site server and the passive site server.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-14*

Hi,    

Thank your for your Replay. IF I create a new Site System Sever on the new machine, It means I have two DPs. Am I right?    

Do you recommend it or Microsoft?     

Or should I create a high Availability for SCCM? If I do that, I have to share my DP. What is the best method? High Availability or have to Site System Server?     

Regards
