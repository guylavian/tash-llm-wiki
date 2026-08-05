---
title: "The Kerberos client received a KRB_AP_ERR_MODIFIED error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2236493/the-kerberos-client-received-a-krb-ap-err-modified
question_id: 2236493
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# The Kerberos client received a KRB_AP_ERR_MODIFIED error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2236493/the-kerberos-client-received-a-krb-ap-err-modified (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we are seeing this type of error in multiple DCs event log in our environment. can anyone help us to resolve this issue.

The Kerberos client received a KRB_AP_ERR_MODIFIED error from the server 5cd228bvvx$. The target name used was cifs/5cg0390pmy.sd.shared. This indicates that the target server failed to decrypt the ticket provided by the client. This can occur when the target server principal name (SPN) is registered on an account other than the account the target service is using. Ensure that the target SPN is only registered on the account used by the server. This error can also happen if the target service account password is different than what is configured on the Kerberos Key Distribution Center for that target service. Ensure that the service on the server and the KDC are both configured to use the same password. If the server's name is not fully qualified, and the target domain (SD.SHARED) is different from the client domain (SD.SHARED), check if there are identically named server accounts in these two domains, or use the fully qualified name to identify the server.

Thanks!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-19*

Hello,

Thank you for posting in Microsoft Q&A.

Based on the description, I understand your question is related to KRB_AP_ERR_MODIFIED error.

The KRB_AP_ERR_MODIFIED error in Kerberos typically indicates a mismatch between the Service Principal Name (SPN) and the account it's registered on, or a password mismatch between the service account and the Kerberos Key Distribution Center (KDC).

Check that the service account password is synchronized between the service and the KDC. If the password has been changed recently, update it accordingly.

Check the SPN is correctly registered on the account used by the target service. Run this command:

`setspn`` -L <account_name>`

Check the server names are fully qualified. If the target domain and client domain are different, use the FQDN to identify the server.

Check DNS is correctly configured and that there are no mismatches in DNS name resolution.

Check the network security settings are configured correctly.

Have a nice day. 

Best Regards,

Molly

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it
