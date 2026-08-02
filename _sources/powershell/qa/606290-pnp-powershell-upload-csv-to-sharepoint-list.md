---
title: "PnP PowerShell - Upload CSV to SharePoint List"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/606290/pnp-powershell-upload-csv-to-sharepoint-list
question_id: 606290
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-business-platform-windows", "m365-office-office-sp-development-routing", "windows-business-windows-server-user-experience-powershell"]
---
# PnP PowerShell - Upload CSV to SharePoint List

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/606290/pnp-powershell-upload-csv-to-sharepoint-list (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I'm looking for some help with PnP PowerShell. I have a script which takes a CSV file and uploads each row as an item to SharePoint Online (see below). My question is, how do I get the script to skip items that already exist in the SharePoint Online list? Currently the script just uploads all rows within the CSV and creates some duplicates.

Parameters

$SiteUrl = "{site}"

$ListName = "iPhone"

$CSVPath = "C:\Users{user}\Documents\PowerShell\Upload SharePoint items from CSV\iphoneexport.csv"

Get the CSV file contents

$CSVData = Import-CsV -Path $CSVPath

Connect to site

Connect-PnPOnline $SiteUrl -Interactive

Iterate through each Row in the CSV and import data to SharePoint Online List

ForEach ($Row in $CSVData)

{

```
Write-Host "Adding Item $($Row.'Asset Number')"

#Add List Items - Map with Internal Names of the Fields!

Add-PnPListItem -List $ListName -Values @{"Title" = $($Row.'Asset Number');

                        "User" = $($Row.User);

};
```

}

I'd be grateful for any advice anyone can give.

Many thanks,

Alex.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-28*

@Alex Hannah  ,    

We can check the item by CAML+ PNP PowerShell, if the Title in list already exists, it will be ignored, check as following:    

```
$Username='******@tenant.onmicrosoft.com'  
$Password = 'Doh76594'  
  
#region Credentials  
[SecureString]$SecurePass = ConvertTo-SecureString $Password -AsPlainText -Force   
[System.Management.Automation.PSCredential]$PSCredentials = New-Object System.Management.Automation.PSCredential($Username, $SecurePass)   
#endregion Credentials  
  
#connect to site  
$consite=Connect-PnPOnline -Url 'https://tenant.sharepoint.com/sites/Team1' -Credentials $PSCredentials  
  
$listName = "list1022"   
$FilePath= "C:\Temp\Test1028.csv"  
$CSVData = Import-CsV -Path $FilePath  
  
  
Import-Csv -Path $FilePath|%{  
  
    $checkitem = $null  
    $tarTitle= $_."Asset Number"  
    $tarUser = $_.User  
      
$caml=@"  
        
           
            $tarTitle   
           
      
"@  
  
   $checkitem= Get-PnPListItem -List $listName -Query $caml  
      
   if($checkitem){  
        Write-Host "this item exists:" $($tarTitle)  
   }else{  
        Write-Host "this item does not exist:" $($tarTitle)  
        Add-PnPListItem -List $ListName -Values @{"Title" = $($tarTitle);  
                         "Active" = $($tarUser );}  
   }  
}
```

Before:    

    

After:    

    

Simialr issue for your reference:    

https://social.msdn.microsoft.com/Forums/en-US/e0dac7d9-36fe-4c6d-bccc-13aa4474bc37/check-if-listitem-exist-using-pnp-powershell?forum=sharepointdevelopment    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
