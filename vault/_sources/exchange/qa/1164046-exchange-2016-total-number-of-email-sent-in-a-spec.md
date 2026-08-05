---
title: "Exchange 2016 - Total number of email Sent in a specific range time"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164046/exchange-2016-total-number-of-email-sent-in-a-spec
question_id: 1164046
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 - Total number of email Sent in a specific range time

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164046/exchange-2016-total-number-of-email-sent-in-a-spec (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dears

I'm looking to find the Total number of email Sent in a week.

I finally came to this powershell string:

```
$msgs=  Get-TransportServer | Get-MessageTrackingLog -Start "01/23/2023 00:00:00" -End "01/23/2023 23:59:59" -ResultSize unlimited | where{$_.EventId -LIKE "SEND*"}
$msgs.count
```

I checked with my Outlook Sent folder and only by using the SEND* (witch include SEND and SENDEXTERNAL operations) I get the correct number.

This count does not include Calendars invitation acceptance.

What do you think about this script? Any easier solution?

Can you test it and let me know?

Thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-23*

This will work also:

```
Get-ExchangeServer | Get-MessageTrackingLog -ResultSize unlimited -Start 01/22/2024 -Sender ******@domain.com -EventId send
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-31*

Dear,

Thanks for your reply!

I tested your solution and  got the same results as mine, so I'd say that both options are good!

Checking SEND* I got 5 messages with EventId SEND AND SENDEXTERNAL

Checking DELIVER I got the 3 INTERNAL emails

Thanks!

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-31*

Hi @A Ska ，

“Event: DELIVER“ is all mails sent internally and externally, “Event: SENDEXTERNAL” is the email that was successfully sent to the outside. You can get the total and subtract the number of messages sent to the outside to get the number of internal messages.

Here is a script to get the total number of messages, you can refer to the following:https://learn.microsoft.com/en-us/answers/questions/81779/how-to-check-total-mails(in-and-out)-of-one-month

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-26*

Hi @A Ska  ，

Your command will search for send events for all mailboxes, I recommend adding a sender condition.

For example:

```
$msgs=  Get-TransportServer | Get-MessageTrackingLog -Start "01/23/2023 00:00:00" -End "01/23/2023 23:59:59" -ResultSize unlimited -Sender "******@contoso.com"  | where{$_.EventId -LIKE "SEND*"}
$msgs.count
```

Or you can search the total number of sent items by selecting the sent time in the search box in Outlook client:

1.  click sent items and click search box with option “current folder”

2.  Click the drop-down list and select the SENT condition (if not, click Add more options to add)

3.  Then there is an items in the lower left corner of the client, showing the total count.

(This will include all outgoing messages, including meeting invitations and rejected messages.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
