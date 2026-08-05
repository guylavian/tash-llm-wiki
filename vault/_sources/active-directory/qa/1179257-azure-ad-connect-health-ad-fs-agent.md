---
title: "Azure AD Connect Health AD FS Agent"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179257/azure-ad-connect-health-ad-fs-agent
question_id: 1179257
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Azure AD Connect Health AD FS Agent

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179257/azure-ad-connect-health-ad-fs-agent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I'm tryng to install a Azure AD Connect Health AD FS Agent on our AD FS servers vainly,

I got the following errors 

```
2023-02-08 15:36:32.543 System.InvalidOperationException: Could not query the MEX on http ports: 443 in hosts: localhost
   at Microsoft.Identity.Health.Adfs.PowerShell.ConfigurationModule.AdfsServiceExaminer.GetAdfsFarmNameFromSts()
   at Microsoft.Identity.Health.Adfs.PowerShell.ConfigurationModule.AdfsServiceExaminer.ComputeServiceSignature()
   at Microsoft.Identity.Health.Common.Clients.PowerShell.ConfigurationModule.RegisterADHealthAgent.ProcessRecord()
```

Is there anything wrong with the AD FS server ?

Thanks in advance

Regards

Louis

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-02-17*

@Da SILVA Louis   Apologies for the delay in reviewing this post, if the issue still persists follow the below steps 

-  checking the bindings in http.sys on the adfs server 

-  you may also want to check that the mex endpoint is enabled in ADFS server 
   Get-AdfsEndpoint -AddressPath "/adfs/services/trust/mex"

-  check if the endpoint is as such also added to HTTP service   netsh http show servicestate |findstr /i /c:Trust/MEX   if its missing but the endpoint is enabled restart the ADFS Service and check if it got re-registered. 

If the issue still persists, let me know we can connect offline to troubleshoot further or if the issue is resolved please share the steps which you tried to resolve as it would help other community members facing similar issue.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-09*

Hi, see these links for a possible solution:

https://social.technet.microsoft.com/Forums/en-US/0decc685-891a-4e88-9b1f-0828b553f29b/error-while-installing-azure-ad-connect-health-for-ad-fs-agent?forum=ADFS

https://serverfault.com/questions/901216/issue-installing-azure-ad-connect-adfs-health-agent
