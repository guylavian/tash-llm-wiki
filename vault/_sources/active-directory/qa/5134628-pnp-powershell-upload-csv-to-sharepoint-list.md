---
title: "PnP PowerShell - Upload CSV to SharePoint List"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5134628/pnp-powershell-upload-csv-to-sharepoint-list
question_id: 5134628
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# PnP PowerShell - Upload CSV to SharePoint List

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5134628/pnp-powershell-upload-csv-to-sharepoint-list (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I'm looking for some help with PnP PowerShell. I have a script which takes a CSV file and uploads each row as an item to SharePoint Online (see below). My question is, how do I get the script to skip items that already exist in the SharePoint Online list? Currently the script just uploads all rows within the CSV and creates some duplicates.

#Parameters<br>$SiteUrl = "{site}"$ListName = "iPhone"$CSVPath = "C:\Users{user}\Documents\PowerShell\Upload SharePoint items from CSV\iphoneexport.csv"#Get the CSV file contents$CSVData = Import-CsV -Path $CSVPath#Connect to siteConnect-PnPOnline $SiteUrl -Interactive#Iterate through each Row in the CSV and import data to SharePoint Online ListForEach ($Row in $CSVData){Write-Host "Adding Item $($Row.'Asset Number')"#Add List Items - Map with Internal Names of the Fields!Add-PnPListItem -List $ListName -Values @{"Title" = $($Row.'Asset Number');"User" = $($Row.User);};}

I'd be grateful for any advice anyone can give.

Many thanks,

Alex.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-27*

Hi Alex,

Thank you for querying in this forum.

I go through the post carefully. It seems like you want the PnP PowerShell script skip items that already exist in the SharePoint list so that it won't create duplicated items.

I would like to help, considering it may need to modify the script, to make sure you get dedicated assistance, I sincerely recommend you post the question in Microsoft Q&A Community, it is the specific channel handling this kind of queries, engineers and members in that community are proficient in the knowledge of PnP PowerShell, and they will also focus on your specific situation and provide specific suggestions.

Your patience and understanding are highly appreciated. Hope you are keeping safe and well.

Best regards,

Tina
