---
title: "Creating SQL Server Active Directory admin via the REST API"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1509066/creating-sql-server-active-directory-admin-via-the
question_id: 1509066
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Creating SQL Server Active Directory admin via the REST API

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1509066/creating-sql-server-active-directory-admin-via-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Greetings,  

I am trying to set the SQL Server admin to be an azure active directory group via the rest api as the powershell module seems to have an error. Here is the powershell function I am using:

```
function SetSqlServerActiveDirectoryAdministrator(
        [string]$resourceGroupName,
        [string]$sqlServerName,
        [string]$adminDisplayName,
        [string]$adminId,
        [string]$tenantId,
        [string]$subscriptionId) {
       

    $url = "https://management.azure.com/subscriptions/$subscriptionId/resourceGroups/$resourceGroupName/providers/Microsoft.Sql/servers/$sqlServerName/administrators/activeDirectory?api-version=2019-06-01-preview"
    Write-Host $url

    $token = (Get-AzAccessToken).token
    $headers = @{   
            "Authorization" = "Bearer $token"
            "Content-Type"  = "application/json"
            "Accept"        = "application/json, */*; q=0.01"
    }
    $Body = @{
            "id" = "/subscriptions/$subscriptionId/resourceGroups/$resourceGroupName/providers/Microsoft.Sql/servers/$sqlServerName/administrators/activeDirectory"
            "name" = $sqlServerName
            "properties" = @{
                    "administratorType" = "activeDirectory"
                    "login"             = $adminDisplayName
                    "sid"               = $adminId
                    "tenantId"          = $tenantId
            }
    }

    Invoke-RestMethod -Method 'Put' -Uri $url -Headers $headers -Body $Body
}
```

The additional parameters: name and id I copied from the Portal as I tried to mimic the request but it doesn't work without them as well.
Here is the error I receive:

```
{
  "error": {
    "details": [
      {
        "code": "InvalidResourceIdSegment",
        "message": "",
        "target": "parameters"
      }
    ],
    "code": "InvalidResourceIdSegment",
    "message": "The \u0027parameters\u0027 segment in the url is invalid."
  }
}
```

Any idea what I might be missing ?  

Thanks,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-23*

The error you're encountering, "InvalidResourceIdSegment," suggests that there's an issue with how the resource ID is being constructed. In your case, it seems that the inclusion of the "id" field in the request body might be causing the problem. 
Try below?

```
function SetSqlServerActiveDirectoryAdministrator(
    [string]$resourceGroupName,
    [string]$sqlServerName,
    [string]$adminDisplayName,
    [string]$adminId,
    [string]$tenantId,
    [string]$subscriptionId
) {
    $url = "https://graph.microsoft.com/v1.0/myorganization/servicePrincipals/$adminId/appRoleAssignments?api-version=1.6"
    Write-Host $url

    $token = (Get-AzAccessToken).Token
    $headers = @{
        "Authorization" = "Bearer $token"
        "Content-Type"  = "application/json"
        "Accept"        = "application/json, */*; q=0.01"
    }

    $Body = @{
        "principalId" = $adminId
        "resourceId"  = "/subscriptions/$subscriptionId/resourceGroups/$resourceGroupName/providers/Microsoft.Sql/servers/$sqlServerName"
        "appRoleId"   = "00000000-0000-0000-0000-000000000000" # This is the constant GUID for the "Admin" role in SQL
    }

    Invoke-RestMethod -Method 'Post' -Uri $url -Headers $headers -Body ($Body | ConvertTo-Json)
}
```
