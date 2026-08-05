---
title: "LAPS for computer outisde the domain controller but inside the same network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1136030/laps-for-computer-outisde-the-domain-controller-bu
question_id: 1136030
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# LAPS for computer outisde the domain controller but inside the same network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1136030/laps-for-computer-outisde-the-domain-controller-bu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have 3 servers outside my domain (where LAPS is already and correctly configured) but in the same lan of the DC.    

They have no domain at all.    

There is a way to let my DC to store/set the password for the local admins for these 3 servers?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-20*

Hello @Lawero  ,    

It is possible to use Local Administrator Password Solution (LAPS) to manage the local administrator passwords for computers that are outside of the domain, but within the same network as the domain controller. However, you will need to make sure that the LAPS client is installed on the computers that you want to manage, and that the client is configured to communicate with the LAPS infrastructure on the domain controller.    

To install the LAPS client on the computers outside of the domain, you will need to download the LAPS client package from the Microsoft Download Center and follow the instructions in the installation guide to install the client on the computers.    

Once the LAPS client is installed, you will need to configure the client to communicate with the LAPS infrastructure on the domain controller. You can do this by setting the "ms-Mcs-AdmPwd" attribute on the computer object in Active Directory. You can set the attribute using a script or a tool like the LAPS UI, or you can set it manually using the Active Directory Users and Computers snap-in.    

Good luck!
