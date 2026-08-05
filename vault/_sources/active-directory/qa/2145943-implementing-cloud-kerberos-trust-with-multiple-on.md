---
title: "Implementing Cloud Kerberos Trust with Multiple On-premises AD Forests"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2145943/implementing-cloud-kerberos-trust-with-multiple-on
question_id: 2145943
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Implementing Cloud Kerberos Trust with Multiple On-premises AD Forests

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2145943/implementing-cloud-kerberos-trust-with-multiple-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a question about setting up Cloud Kerberos trust in an environment with multiple on-premises Active Directory (AD) forests that are configured with domain trusts between them.

Is it sufficient to configure Cloud Kerberos trust for only one on-premises AD forest, or is it necessary to set it up for each of the AD forests connected by domain trusts?

Has anyone done something like this?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2025-01-15*

Hello,

Thank you for posting in Q&A forum.

Yes, we need to configure Cloud Kerberos trust for every AD forest. Here are the steps to follow:

1.Enable Entra Kerberos in every domain involved in all forest.

2.Create AzureADKerberos Computer Object: For each AD forest, create an AzureADKerberos computer object in the respective domain. This object acts as a read-only domain controller (RODC) and is used by Microsoft Entra ID to generate Ticket Granting Tickets (TGTs)1.

3.Configure Cloud Kerberos Trust on endpoints via GPO or Intune.

4.Verify the configuration and ensure that users can authenticate via Cloud Kerberos Trust.

For further details, please refer to below Microsoft Official Documentation:

REF: https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/deploy/hybrid-cloud-kerberos-trust?tabs=intune

To help other customers who may be facing the same issue, please don't forget to vote if the reply is helpful.

Best Regards

Zunhui
