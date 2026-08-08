---
title: "Issue with Secondary ADFS Server Creation – Event ID 4"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2182091/issue-with-secondary-adfs-server-creation-event-id
question_id: 2182091
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issue with Secondary ADFS Server Creation – Event ID 4

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2182091/issue-with-secondary-adfs-server-creation-event-id (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

error1.pngI am facing an issue while creating the secondary ADFS server. My primary ADFS server is functioning properly; however, when attempting to set up the secondary server, I encountered an error during the pre-check process with Event ID 4.

Below are the error details:

Service Account: srvadfapp

Error Screenshot: [Attach error.png]

**"**The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server srvadfapp. The target name used was host/hfcyotpdaf1v01.niwashfc.intra. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server name is not fully qualified, and the target domain (NIWASHFC.INTRA) is different from the client domain (NIWASHFC.INTRA), check if there are identically named server accounts in these two domains, or use the fully-qualified name to identify the server."

Could you please review the error and provide a possible solution to resolve this issue?

Thanks and Regards,

Anil Kadam

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2025-03-06*

Hello,

Thank you for posting in Q&A forum.

To further troubleshoot this Kerberos authentication issue, please kindly try below steps:

1.Check and ensure that SPN host/hfcyotpdaf1v01.niwashfc.intra is only registered on service account srvadfapp.

Open CMD Window as administrator and run below command:

a.Check SPN

setspn -Q host/hfcyotpdaf1v01.niwashfc.intra

b.Remove incorrect SPN:

setspn -D host/hfcyotpdaf1v01.niwashfc.intra <incorrect_account>

c.Add correct SPN:

setspn -S host/hfcyotpdaf1v01.niwashfc.intra srvadfapp

REF: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731241(v=ws.11)

2.Check if the service account password is correct or not.

3.Restart ADFS service on the primary and secondary server to get changes taken effect by CMD command:

Restart-Service adfssrv

To help other customers who may be facing the same issue, please don't forget to vote if the reply is helpful.

Best Regards

Zunhui
