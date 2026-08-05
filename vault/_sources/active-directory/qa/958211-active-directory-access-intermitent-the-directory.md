---
title: "Active Directory Access: Intermitent \"The directory service is unavailable.\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/958211/active-directory-access-intermitent-the-directory
question_id: 958211
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-csharp", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Access: Intermitent "The directory service is unavailable."

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/958211/active-directory-access-intermitent-the-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

We're using the Active Directory Services, and with basic code like this:    

```
using var entry = new DirectoryEntry($"LDAP://{domain}/RootDSE", adminUserName, adminPassword, AuthenticationTypes.Secure | AuthenticationTypes.Sealing | AuthenticationTypes.Signing | AuthenticationTypes.ServerBind);  
   entry.RefreshCache();
```

It's not easily reproducable and works most of the time but intermitantly this will result in the error: "System.Runtime.InteropServices.COMException (0x8007200F): The directory service is unavailable."    

I've added a loop for it to retry but it can still come up.    

We also make sure to use using statements so we also clean up resources anytime we access AD.    

Are there any known reasons for this happening? I've seen very brief posts around it from years ago but no answers.    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-08*

Hi anonymous user    

Have you tried the same code with the options AuthenticationTypes.Secure | AuthenticationTypes.Sealing | AuthenticationTypes.Signing removed  just in case you are hitting a DC which doesn't support one of these options.    

I would also check the health of the domain and DCs by run a dcdiag /v/c on all the DCs.  I would also make sure that the replication is working correctly with repadmin /showrepl and repladmin /replsummary in case there is left over details from a removed DC.    

If you want to repeatedly test the connectivity to the domain you could use the LDAP Performance option in NetTools which repeatedly test the connection to the DC - https://nettools.net/ldap-performance/    

Gary.
