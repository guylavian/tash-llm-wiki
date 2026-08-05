---
title: "ADFS A bind attempt to domain 'domain.com' failed with error code '1722'."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/59975/adfs-a-bind-attempt-to-domain-domain-com-failed-wi
question_id: 59975
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS A bind attempt to domain 'domain.com' failed with error code '1722'.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/59975/adfs-a-bind-attempt-to-domain-domain-com-failed-wi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have multiple domains that use our ADFS servers. They are able to login and authenticate just fine. However, when they attempt to change their password, I get an error in Event Viewer. All the users in our domain are able to change passwords without an issue.

ADFS A bind attempt to domain 'domain.com' failed with error code '1722'.

I cant even find this error anywhere online. Does anyone know where I can start? Our usual ADFS SME no longer works here :(

```
Password change failed for following user: 

Additional Data 

User: 
******@domain.com 

Device Certificate: 

Server on which password change was attempted: 

Error details: 
Microsoft.IdentityServer.Service.AccountPolicy.ADAccountLookupException: MSIS6080: A bind attempt to domain 'domain.com' failed with error code '1722'.
   at Microsoft.IdentityServer.Service.AccountPolicy.ActiveDirectory.ADNameTranslator.CrackUPN(String domain, String userName)
   at Microsoft.IdentityServer.Service.AccountPolicy.ActiveDirectory.ADNameTranslator.CrackName(String userName, String& samAccountName, String& userDomain)
   at Microsoft.IdentityServer.Service.PasswordManagement.PasswordUtil.ChangePassword(String userName, SecureString oldPassword, SecureString newPassword)
```

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-06*

The password update feature required direct communication between the ADFS server handling the request and the domain controller with the PDC emulator role of the user's domain.  

This error suggests that it was not reachable.
