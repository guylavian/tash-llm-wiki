---
title: "Export Exchange 2019 primary mailbox and archive mailbox total sizes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2264863/export-exchange-2019-primary-mailbox-and-archive-m
question_id: 2264863
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Export Exchange 2019 primary mailbox and archive mailbox total sizes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2264863/export-exchange-2019-primary-mailbox-and-archive-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Folks,

I have the script below which exports the TotalItemSize of primary and archive mailboxes for users taken from an input file. As you can see from the example output, the TotalItemSize shows the value in MB and bytes. What I would like to do is convert the TotalItemSize values to be in MB only i.e. do not include the bytes section.

"Alias","PrimaryMailboxSize","ArchiveMailboxSize"

"smith1","2.945 MB (3,087,594 bytes)","673 KB (689,202 bytes)"

My existing script is below. Note, I am not particularly tied to this script, so if you have something else which works, that would be fine too!

Any help would be appreciated!

Thanks,

Mark

```
# Import the CSV file
$mailboxes = Import-Csv "E:\Scripts\Mailbox-Migration\Master-User-List.csv"

# Create an array to store the results
$results = @()

# Loop through each email address
foreach ($mailbox in $mailboxes) {
    $alias = $mailbox.alias

    # Get primary mailbox size
    $primaryMailbox = Get-MailboxStatistics -Identity $alias
    $primarySize = $primaryMailbox.TotalItemSize

    # Get archive mailbox size (if enabled)
    $archiveMailbox = Get-MailboxStatistics -Identity $alias -Archive
    $archiveSize = $archiveMailbox.TotalItemSize

    # Create a custom object to store the results
    $result = [PSCustomObject]@{
        Alias = $alias
        PrimaryMailboxSize = $primarySize
        ArchiveMailboxSize = $archiveSize
    }

    # Add the result to the array
    $results += $result
}

# Export the results to a CSV file
$results | Export-Csv -Path "E:\Scripts\Mailbox-Migration\Get-Primary-and-Archive-Mailbox-Sizes\mailbox_sizes.csv" -NoTypeInformation

write-host
Write-host -ForegroundColor Green "Mailbox sizes have been exported to E:\Scripts\Mailbox-Migration\Get-Primary-and-Archive-Mailbox-Sizes\mailbox_sizes.csv"
```

## Answers

_No answers on this thread._
