---
title: "How to delete Exchange folder using Powershell or otherwise"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1058540/how-to-delete-exchange-folder-using-powershell-or
question_id: 1058540
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# How to delete Exchange folder using Powershell or otherwise

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1058540/how-to-delete-exchange-folder-using-powershell-or (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One of our test domain M365 accounts has accumulated a large number of items in the `\Deleted Items` Exchange Online Folder. From OWA Trash and Recoverable Items for the user are clean.     

This seems to be causing most of the Exchange APIs we are using to grind to a halt.     

I'm looking for some advice on how to actually clean-up not just the items but also the folders in `\Deleted Items`. For removing the items we have been able to adapt some of the instructions in https://learn.microsoft.com/en-us/exchange/policy-and-compliance/recoverable-items-folder/clean-up-deleted-items?view=exchserver-2019 to clean-up items in folders that are also under `Deleted Items`. We have also tried the Graph API, but it is not able to see any of these folders.     

We are at a loss on how to delete the remaining folders which are now empty.     

Thank you for your help!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-07-21*

```
Add-type -assembly "Microsoft.Office.Interop.Outlook" | Out-Null
$oLFolders = "Microsoft.Office.Interop.Outlook.OlDefaultFolders" -as [type]
$outlook   = New-Object -ComObject Outlook.Application
$namespace = $outlook.GetNamespace("MAPI")
$deleted   = $namespace.Folders.Item('******@domain.com').Folders.Item("Deleted Items")
cls
while(1){
    $deleted.Folders | %{
        Write-Host $_.Name -fore Magenta
        $_.Folders | %{
            Write-Host "	"$_.Name -fore Cyan
            $_.Delete()
        }
        $_.Delete()
    }
    cls
}
```

I am using this, and it's quite effective.  

I am also pointing this to the Archive, which is "Online Archive - ******@domain.com"

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-22*

Thank you @Andy David - MVP       

The first link - https://community.spiceworks.com/topic/2181078-powershell-delete-a-folder-from-all-mailboxes-exchange-online-o365 was helpful. Once I adapted the script to use OAuth (EWS basic auth is now disabled), I was able to get that to work. Folders are now deleting.     

Did not try the other suggestions since they required local binaries that I could only get on a Windows machine.
