---
title: "Powershell script on Exchange server returns 800+ records out of 62000. Why?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/281934/powershell-script-on-exchange-server-returns-800-r
question_id: 281934
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Powershell script on Exchange server returns 800+ records out of 62000. Why?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/281934/powershell-script-on-exchange-server-returns-800-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I've used script below to extract all attachments from mailbox (needed to perform only once). It's a mailbox where reports was sent, so it contains only messages with specific name and attachment.  

And it returns only 800+ records out of 60+ thousands. Any advice how to modify it? I've tried to change ItemView from 1000 to 63000, nothing changed.

```
# Name of the mailbox to pull attachments from
$MailboxName = '******@domain.com'

# Location to move attachments
$downloadDirectory = 'E:\ToExport'

# Path to the Web Services dll
$dllpath = "E:\Exchange\V15\Bin\Microsoft.Exchange.WebServices.dll"
[VOID][Reflection.Assembly]::LoadFile($dllpath)

# Create the new web services object
$service = New-Object Microsoft.Exchange.WebServices.Data.ExchangeService([Microsoft.Exchange.WebServices.Data.ExchangeVersion]::Exchange2019)

# Create the LDAP security string in order to log into the mailbox
$windowsIdentity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
$sidbind = "LDAP://"
$aceuser = [ADSI]$sidbind

# Auto discover the URL used to pull the attachments
$service.AutodiscoverUrl($aceuser.mail.ToString())

# Get the folder id of the Inbox
$folderid = new-object  Microsoft.Exchange.WebServices.Data.FolderId([Microsoft.Exchange.WebServices.Data.WellKnownFolderName]::Inbox,$MailboxName)
$InboxFolder = [Microsoft.Exchange.WebServices.Data.Folder]::Bind($service,$folderid)

# Find mail in the Inbox with attachments
$Sfha = new-object Microsoft.Exchange.WebServices.Data.SearchFilter+IsEqualTo([Microsoft.Exchange.WebServices.Data.EmailMessageSchema]::HasAttachments, $true)
$sfCollection = new-object Microsoft.Exchange.WebServices.Data.SearchFilter+SearchFilterCollection([Microsoft.Exchange.WebServices.Data.LogicalOperator]::And);
$sfCollection.add($Sfha)

# Grab all the mail that meets the prerequisites
$view = new-object Microsoft.Exchange.WebServices.Data.ItemView(63000)
$frFolderResult = $InboxFolder.FindItems($sfCollection,$view)

# Loop through the emails
foreach ($miMailItems in $frFolderResult.Items){

    # Load the message
    $miMailItems.Load()

    # Loop through the attachments
    foreach($attach in $miMailItems.Attachments){

        # Load the attachment
        $attach.Load()

        # Save the attachment to the predefined location
        $fiFile = new-object System.IO.FileStream(($downloadDirectory + “\” + $attach.Name.ToString()), [System.IO.FileMode]::Create)       
                $fiFile.Write($attach.Content, 0, $attach.Content.Length)
        $fiFile.Close()
    }
 }
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-21*

Have a look here: what-is-the-maximal-size-of-an-itemview-in-ews  

You'll have to loop over the FindItems using $frFolderResult.MoreAvailable until no more results are returned.
