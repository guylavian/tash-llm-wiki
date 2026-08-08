---
title: "Windows 2016 GPO with PowerShell cannot be performed more times"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/113666/windows-2016-gpo-with-powershell-cannot-be-perform
question_id: 113666
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-powershell", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Windows 2016 GPO with PowerShell cannot be performed more times

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/113666/windows-2016-gpo-with-powershell-cannot-be-perform (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,

I deploy a GPO with one PowerShell for our client's desktops and laptops, unfortunately I found out the GPO just only run once. I hope the result is when user's Computer login to the AD domain, the GPO will be performed every time. Our PowerShell script will do different job separately. does anyone have any idea on it?? or what kind of configuration I need to pay attention?? Thanks

-   I refer to the article on the internet (http://woshub.com/how-to-create-modify-and-delete-registry-keys-using-gpo/). It can work well just only once.

-   my PowerShell:    Start-Transcript -Path "$($env:windir)\Temp\odConfiguration.txt" -Force    $_Logfile = "$($env:windir)\Temp\odConfiguration.txt"  

    $_HKLMRootPath = "HKLM:\Software\Policies\Microsoft"  

    $_HKLMPath = "HKLM:\Software\Policies\Microsoft\OneDrive"  

    $_HKCRPath = "HKCR:\CLSID"  

    $_SharePointOnPremFrontDoorUrl = "https://doclib.test.cmmp.gov.hk"  

    $_SharePointOnPremTenantName = "Doclib - Unclassified"  

    $_OgcioOneDriveFolderName = "Doclib - Unclassified"    if((Test-Path $_HKLMPath -ErrorAction SilentlyContinue) -eq $true)  

    {  

    Write-Host (Get-ItemProperty -LiteralPath $_HKLMPath -Name $_ValueName).$_ValueName

```
if((Get-ItemProperty -LiteralPath $_HKLMPath -Name SharePointOnPremTenantName).$_ValueName -ne $_SharePointOnPremTenantName)
{
    Set-ItemProperty -Path $_HKLMPath -Name SharePointOnPremTenantName -Value $_SharePointOnPremTenantName -Type String
}

if((Get-ItemProperty -LiteralPath $_HKLMPath -Name SharePointOnPremFrontDoorUrl).$_ValueName -ne $_SharePointOnPremFrontDoorUrl)
{
    Set-ItemProperty -Path $_HKLMPath -Name SharePointOnPremFrontDoorUrl -Value $_SharePointOnPremFrontDoorUrl -Type String
}

New-PSDrive -Name HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT -ErrorAction SilentlyContinue

Get-ChildItem $_HKCRPath -rec -ea SilentlyContinue | foreach {

    $CurrentKey = (Get-ItemProperty -Path $_.PsPath)

    Write-Host ($(Get-Date -Format "o"), " ", $CurrentKey.PSParentPath)
    Write-Host ($(Get-Date -Format "o"), " ", $CurrentKey.PSChildName)

    \# 04271989-C4D2
    if (($CurrentKey.PSChildName -like "*04271989-C4D2*") -eq $true) {

       $_regPath = $_HKCRPath + "\" + $CurrentKey.PSChildName
       $_value = Get-ItemProperty -Path $_regPath

       Write-Host ($(Get-Date -Format "o"), " ",  $_regPath)

       Write-Host ($(Get-Date), " ",  $_value."(default)")

       try
       {
            Write-Host $(Get-Date -Format "o")
            Write-Host "Get ready on updating new registry value $_OgcioOneDriveFolderName"

            Set-ItemProperty -Path $_regPath -Name "(Default)" -Value $_OgcioOneDriveFolderName

            Write-Host "To UPDATE new registry value $_OgcioOneDriveFolderName # DONE"

            break
       }
       Catch [System.UnauthorizedAccessException]
       {   
            Write-Host ($(Get-Date -Format "o"), " ",  $Error[0])
       }
       Catch [System.IO.DirectoryNotFoundException]
       {    
            Write-Host ($(Get-Date -Format "o"), " ",  $Error[0])
       }
       Catch
       {    
            Write-Host ($(Get-Date -Format "o"), " ",  $Error[0])
       } 
    }
}
```

    }  

    else  

    {  

    # Set the location to the registry  

    Set-Location -Path $_HKLMRootPath

```
\# Create a new Key

Get-Item -Path $_HKLMRootPath | New-Item -Name OneDrive -Force

\# Create new items with values

New-ItemProperty -Path $_HKLMPath -Name SharePointOnPremFrontDoorUrl -Value $_SharePointOnPremFrontDoorUrl -PropertyType String -Force
New-ItemProperty -Path $_HKLMPath -Name SharePointOnPremPrioritization -Value 1 -PropertyType DWord -Force    
New-ItemProperty -Path $_HKLMPath -Name SharePointOnPremTenantName -Value $_SharePointOnPremTenantName -PropertyType String -Force

\# Get out of the Registry
Pop-Location
```

    }    Stop-Transcript

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-01*

Hello,    

Thank you so much for posting here.    

Frankly speaking, we are not professional with powershell. According to our description, as per my understanding, we deployed GPP to import a reg. file into Group Policy with several registry settings.     

Firstly we have deployed some registry settings. We then export these registry settings to a REG file. (If your reg file contains data from different registry hives (HKLM, HKCU, HK_CLASSES), you need to divide them into separate reg files.)    

Then we converted this REG file to the XML format with a PowerShell script. The XML file was copied in the File Explorer and pasted to the Registry section in the Group Policy editor.     

Last all registry settings imported will appear in the Group Policy console and then will be applied to the target computers in the domain.     

If there is any misunderstanding, please feel free to let me know.     

"unfortunately I found out the GPO just only run once. I hope the result is when user's Computer login to the AD domain, the GPO will be performed every time. Our PowerShell script will do different job separately."    

Our PowerShell script includes lots of registry settings, but some of the registry settings are not applied, right?     

For the computer Configuration, it will automatically apply when the computers start. For User Configuration, it will automatically apply when the users login. Or we could run "gpupdate /force" command to force the refresh.     

Sorry that we could not clearly understand "the GPO just only run once". Hope we could explain more about this.     

For any question, please contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
