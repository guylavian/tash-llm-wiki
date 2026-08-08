---
title: "how to combine 2 ForEach in exchange shell and then export in one csv file."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1434861/how-to-combine-2-foreach-in-exchange-shell-and-the
question_id: 1434861
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-onedrive-business-platform-windows", "m365-office-office-sp-business-platform-windows", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# how to combine 2 ForEach in exchange shell and then export in one csv file.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1434861/how-to-combine-2-foreach-in-exchange-shell-and-the (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

-  I need to obtain the result of 2 foreach and export it to a single csv, I would appreciate your support.

```
#Connect SPO Service
Connect-SPOService -Url https://estrategicaperu-admin.sharepoint.com

 #Get all Site colections
    $Sites = Get-SPOSite -IncludePersonalSite $true -Limit all -Filter "Url -like '-my.sharepoint.com/personal/'"
    $UsageData = @()
    Foreach ($Site in $Sites)
    {
        Write-host $Site.URL
     
        #Get all Site Collection Administrators
        $SiteAdmins = Get-SPOUser -Site $Site.Url -Limit ALL | Where { $_.IsSiteAdmin -eq $True}
        foreach($Admin in $SiteAdmins)
        {
            Write-host $Admin.LoginName

            #Collect OneDrive usage data
            $UsageData += [PSCustomObject][ordered]@{
                URL              = $Site.URL
                SiteAdmin        = $Admin.LoginName
            }
        }
    }
 
catch {
    write-host "Error: $($_.Exception.Message)" -foregroundcolor Red
}

#Export the data to CSV Report
$UsageData | Format-table
$UsageData | Export-Csv -Path "C:\AzScripts\ListAdminOneDrive.csv" -NoTypeInformation
```

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-23*

Please run below PowerShell.

```
$AdminCenterURL = "https://tenant-admin.sharepoint.com"
$ReportOutput="C:\ListAdminOneDrive.csv"
  
Connect-SPOService -url $AdminCenterURL
  
#Get all OneDrive sites
$Sites = Get-SPOSite -IncludePersonalSite $true -Limit all -Filter "Url -like '-my.sharepoint.com/personal/'"
$OneDriveAdmins = @()     
#Get all OneDrive Administrators
Foreach ($Site in $Sites)
  {
     Write-host -f Yellow "Processing Site Collection:"$Site.URL
        
     $SiteAdmins = Get-SPOUser -Site $Site.Url -Limit ALL | Where { $_.IsSiteAdmin -eq $True}
 
     foreach($Admin in $SiteAdmins)
        {
           Write-host $Admin.LoginName

           $ExportItem = New-Object PSObject 
           $ExportItem | Add-Member -MemberType NoteProperty -Name "Url" -value $Site.URL
           $ExportItem | Add-Member -MemberType NoteProperty -name "Admin" -value $Admin.LoginName    
     
           #Add the object with the above properties to the Array  
           $OneDriveAdmins += $ExportItem  
   }
}

$OneDriveAdmins|Export-Csv $ReportOutput -NoTypeInformation
```

Result:

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-22*

I think you've already done most of the work. You don't need to collect the information in the $UseageData variable (in fact, you don't need that variable at all), just emit the PSCustomObject into the "success" stream.  Is there a reason you're sending the data to the Format-Table and a CSV?

```
#Get all Site colections
Sites = Get-SPOSite -IncludePersonalSite $true -Limit all -Filter "Url -like '-my.sharepoint.com/personal/'" |
    ForEach-Object{
        $URL = $_.URL       # remember for use in a nested Foreach-Object
        Write-Host $URL
     
        #Get all Site Collection Administrators
        Get-SPOUser -Site $Site.Url -Limit ALL | 
            Where-Object { $_.IsSiteAdmin -eq $True }|
                ForEach-Object{
                    Write-Host $_.LoginName

                    #Collect OneDrive usage data
                    [PSCustomObject][ordered]@{
                        URL       = $URL
                        SiteAdmin = $_.LoginName
                    }
                }
    } | Export-CSV "C:\AzScripts\ListAdminOneDrive.csv" -NoTypeInformation
```
