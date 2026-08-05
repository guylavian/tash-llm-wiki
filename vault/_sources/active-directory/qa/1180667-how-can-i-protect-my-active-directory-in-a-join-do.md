---
title: "How can I protect my Active Directory in a join domain construction?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180667/how-can-i-protect-my-active-directory-in-a-join-do
question_id: 1180667
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How can I protect my Active Directory in a join domain construction?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180667/how-can-i-protect-my-active-directory-in-a-join-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently, I have several servers which are domain Join. This also contains the Active Directory, which has only one forest. What are the possibilities to protect the Active Directory. 

When dissolving the domain join, there is a huge administration effort because I want personalized users. I have read that a bastion environment could be a possibility of protection, but it should not be in the cloud. It should be a solution for my DMZ. Does anyone have any experience or suggestions? 

Thanks for your answers.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-10*

To protect Active Directory without dissolving the domain join, consider the following budgeting enterprise suggestions:

-  Implement a budgeting enterprise bastion environment in your DMZ for added security.

-  Seek expert advice on configuring a personalized user setup to minimize administration effort within your budgeting enterprise framework.

-  Evaluate budgeting enterprise on-premises solutions that provide robust security features and align with your budgetary requirements.

-  Research and compare different budgeting enterprise vendors and their offerings to find the most suitable solution for your needs.

-  Consider the long-term costs associated with maintenance, updates, and support when budgeting for the enterprise solution in your budgeting enterprise plan.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-16*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query

To protect your Active Directory in a join domain construction, you should ensure that all of your systems are up to date with the latest security patches, use strong passwords for all user accounts, use a two-step authentication process for all administrative accounts, enable audit logging on all domain controllers, configure Network Access Protection (NAP) to prevent non-compliant devices from connecting to the domain, and use an antivirus or antimalware solution to protect against malicious software. Additionally, you should use access control lists (ACLs) to limit user access to resources, restrict logon rights for users, and ensure that all domain controllers are located in secure physical locations.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-15*

Hi @Hans

To protect your active directory environment , you should start by implementing 3 tiers model : Active Directory Red Forest Design aka Enhanced Security Administrative Environment (ESAE)

Some ideas to harden your active directory environment :

-  Reduce the number of account with high privilege 

-  Disable weak and insecure authentication protocol ntlmv1

-  Disable weak and insecure encryption type for kerberos authentication like RC4

-  Harden privileged accounts , by checking the option cannot be delegated, delete SPN, applying password policy

-  Use a third party product in order to detect vulnerabilities in your active directory environment like https://www.pingcastle.com/

Please don't forget to mark helpful answer as accepted

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-02-14*

Something here could help.

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/best-practices-for-securing-active-directory  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
