---
title: "Exchange Bulk import from .csv file to remove deviceID from all users from Allow and then add their deviceID back to Allow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/359416/exchange-bulk-import-from-csv-file-to-remove-devic
question_id: 359416
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Bulk import from .csv file to remove deviceID from all users from Allow and then add their deviceID back to Allow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/359416/exchange-bulk-import-from-csv-file-to-remove-devic (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Genius Peeps,

Thought maybe I could turn here for some help! Does anyone know of a Powershell script I could run on our Exchange server for to the following:

1) We would initially want to clear all or current mobile devices from all the users

2) Then re-add their specific mobile device ID that we received from them to the ALLOW list

Is there some sort of .csv and powershell script I can create to make this process fast?

We found the following scripts to remove all from ALLOW and to add to ALLOW list

Clear all Allow  

Set-CASMailbox -Identity username -ActiveSyncAllowedDeviceIDs $null

Add to Allow  

Set-CASMailbox -Identity username -ActiveSyncAllowedDeviceIDs @{add='DeviceId'}

And maybe after running this script if there's also a quick way to bulk all the users again to show the results were made to the accounts? Using this command? Get-CASMailbox -Identity username | fl activesync*

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-04-22*

Hi @t0kyobanana   ,    

The script doesn't work for multiple DeviceId users?    

As I tested, the user test, it has three Ids and it could be added to the AllowedDeviceIDs successfully.    

    

And you should run the cmdlet like this:    

```
Set-CASMailbox -Identity username -ActiveSyncAllowedDeviceIDs DeviceID1,DeviceID2
```

    

Best regards,    

Lou

## Answer (community) — community member

*upvotes: 1 · updated: 2021-04-20*

@Anonymous   The script worked flawlessly!!! Thanks SO much! :) :) :) hehe I wouldn't mind seeking answers from you again in the future.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-04-16*

Hi @t0kyobanana   ,    

Yeah you can simply add this cmdlet to the top line of the script:    

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

Then it will first remove and then add.    

And sorry I don't know how you wanna the confirmed result be like, the result(done or undone) will be listed as the added.csv and error.csv. You could tell me more if that doesn't meet your requirement.    

This could add multiply ID for one user, just need your list.csv be like this(separate them with commas):    

    

Or the txt:    

    

The result will be like:    

    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-04-16*

Hi @t0kyobanana   ,    

Good day!    

If you wanna set all users' AllowedDeviceIDs to null, you could use:    

```
Get-CASMailbox | Set-CASMailbox -ActiveSyncAllowedDeviceIDs $null
```

And to add the DeviceIDs for a specific user, you can run this:    

```
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

The list.csv should be like:     

    

And the result:    

    

For the successfully added ones:    

    

If there are any error, you could found the error messages from the error.txt in the C:\ folder.    

    

Best regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
