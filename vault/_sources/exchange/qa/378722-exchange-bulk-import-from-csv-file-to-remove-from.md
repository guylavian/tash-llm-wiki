---
title: "Exchange Bulk import from .csv file to remove from Allow and then Allow."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/378722/exchange-bulk-import-from-csv-file-to-remove-from
question_id: 378722
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Bulk import from .csv file to remove from Allow and then Allow.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/378722/exchange-bulk-import-from-csv-file-to-remove-from (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Genius Peeps,

My name is Mehul Mehta i am working as a software developer in Nitech stainless Inc.com so my question is

Thought maybe I could turn here for some help! Does anyone know of a Powershell script I could run on our Exchange server for to the following:

1) We would initially want to clear all or current mobile devices from all the users

2) Then re-add their specific mobile device ID that we received from them to the ALLOW list

Is there some sort of .csv and script I can create to make this process fast?

We found the following scripts to remove all from ALLOW and to add to ALLOW

Clear all Allow  

Set-CASMailbox -Identity username -ActiveSyncAllowedDeviceIDs $null

Add to Allow  

Set-CASMailbox -Identity username -ActiveSyncAllowedDeviceIDs @{add='DeviceId'}

And maybe after running this script if theres also a quick way to show the results were made to the accounts? Using this command? Get-CASMailbox -Identity username | fl activesync*

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-06*

Hi @Nitech Inc   ,    

Have you ever tried this:     

```
Get-CASMailbox | Set-CASMailbox -ActiveSyncAllowedDeviceIDs $null  
      
 Import-Csv C:\list.csv |   
 ForEach{  
 try {  
 Set-CASMailbox -Identity $_.UserName -ActiveSyncAllowedDeviceIDs $_.DeviceId -ErrorAction Stop  
 Write-Output "Successfully Done $_" | Out-File "C:\added.csv" -Append  
 }  
 catch [System.Exception]   
 {  
 Write-Output "$_" | Out-File "c:\error.csv" -Append  
 }  
 Finally  
 {  
 }}
```

Since your issue is same with this thread: https://learn.microsoft.com/en-us/answers/questions/359416/exchange-bulk-import-from-csv-file-to-remove-from.html     

I think you could check it and if that doesn't meet your requirement, please let me know.    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
