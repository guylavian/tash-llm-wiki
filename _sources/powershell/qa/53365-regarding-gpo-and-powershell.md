---
title: "Regarding GPO and PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/53365/regarding-gpo-and-powershell
question_id: 53365
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell"]
---
# Regarding GPO and PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/53365/regarding-gpo-and-powershell (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi there,

I setup the GPO to change the Client's registry like the shown below:

```
# ($_OneDrive = Get-Item -path HKLM:\Software\Policies\Microsoft\OneDrive -ErrorAction SilentlyContinue) -eq $null
if((Test-Path "HKLM:\Software\Policies\Microsoft\OneDrive" -ErrorAction SilentlyContinue) -eq $true)
{
    Write-Host $_OneDrive

    New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT

    if((Test-Path "HKCR:\CLSID\{04271989-C4D2-689D-E58A-84C94193AFF6}" -ErrorAction SilentlyContinue) -eq $true)
    {
        Set-ItemProperty -Path "HKCR:\CLSID\{04271989-C4D2-689D-E58A-84C94193AFF6}" -Name ‘(Default)’ -Value "doclib (unclassified)"
    }     

    # if ((Get-ItemProperty “HKLM:\Software\Policies\Microsoft\TESTING” -Name “r1” -ErrorAction SilentlyContinue) -ne $null){
    #      Set-ItemProperty “HKLM:\Software\Policies\Microsoft\TESTING” -Name “r1” -Value "2020"
    # }

    # if(($_CLSID = Get-Item -path 'HKCR\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}'))
    # {
    #     Write-Host $_CLSID
    # }    
}
else
{ 
    # Set the location to the registry
    Set-Location -Path "HKLM:\Software\Policies\Microsoft"

    # Create a new Key

    Get-Item -Path "HKLM:\Software\Policies\Microsoft" | New-Item -Name "OneDrive" -Force

    # Create new items with values
    New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\OneDrive" -Name "SharePointOnPremFrontDoorUrl" -Value "http://win-i1ns5qsofnv:31018" -PropertyType "String" -Force
    New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\OneDrive" -Name "SharePointOnPremPrioritization" -Value 1 -PropertyType "DWord" -Force
    New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\OneDrive" -Name "SharePointOnPremTenantName" -Value "Contoso" -PropertyType "String" -Force

    # Get out of the Registry
    Pop-Location
}
```

this part: always cannot modify the client's registry. does anyone have any idea on it?? Thanks

```
if((Test-Path "HKCR:\CLSID\{04271989-C4D2-689D-E58A-84C94193AFF6}" -ErrorAction SilentlyContinue) -eq $true)
        {
            Set-ItemProperty -Path "HKCR:\CLSID\{04271989-C4D2-689D-E58A-84C94193AFF6}" -Name ‘(Default)’ -Value "doclib (unclassified)"
        }
```

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-30*

Greeting SHUOH-8693,  

First of all, in order to narrow the scope of inspection, we need to clarify whether this problem is a GPO problem or a PS problem.  

Therefore, if you manually change the user registry, can this operation be successful?   

If it is not successful, it may be due to lack of permissions or setting errors.  

If it succeeds, it is the cause of the PS. We can check the error report to solve the problem.   

Looking forward to your reply.  

Best wishes,  

Young Yang
