---
title: "issue giving managed identity exchange admin role"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657198/issue-giving-managed-identity-exchange-admin-role
question_id: 1657198
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# issue giving managed identity exchange admin role

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657198/issue-giving-managed-identity-exchange-admin-role (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to give a managed identity exhcange admin role to run automations in azure however when using 

```
$MIAppID = 'my id'
$params = @{
    ServicePrincipalId = $MIAppID # managed identity object id
    PrincipalId = $MIAppID # managed identity object id
    ResourceId = (Get-MgServicePrincipal -Filter "AppId eq '00000002-0000-0ff1-ce00-000000000000'").id # Exchange online
    AppRoleId = "dc50a0fb-09a3-484d-be87-e023b12c6440" # Exchange.ManageAsApp
}
New-MgServicePrincipalAppRoleAssignedTo @params
```

I get: The 'Get-mgserviceprincipal' command was found in the module 'Microsoft.Graph.Applications', but the module could not be loaded. For more information, run 'Import-Module Microsoft.Graph.Applications'.

I then install the latest verson but still the same issue? Any ideas where I am going wrong?

## Answers

_No answers on this thread._
