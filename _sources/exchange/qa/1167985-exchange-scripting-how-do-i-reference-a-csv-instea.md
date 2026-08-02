---
title: "Exchange scripting, How do I reference a .csv instead of a username"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1167985/exchange-scripting-how-do-i-reference-a-csv-instea
question_id: 1167985
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Exchange scripting, How do I reference a .csv instead of a username

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1167985/exchange-scripting-how-do-i-reference-a-csv-instea (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

What would be the correct format ( do I only need the userprinciplename?) as well as referencing the script.

For example, how would I give a list of users instead of one user at a time

Set-Mailbox -Identity "Debra Garcia" -MaxSendSize 25mb -MaxReceiveSize 35mb

Thank you in advance

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-02-07*

Hi @Stefan Diedericks  ,

You can also use the following command to loop through the user's userprinciplename in the CSV.

 

```
$UserList = Import-CSV C:\temp\users.csv

ForEach ($User in $UserList) {

Set-Mailbox -Identity $user. userprinciplename -MaxSendSize 25mb -MaxReceiveSize 35mb

}
```

You can create a CSV file by referring to the following:

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-06*

Assuming you have a "blabla.csv" file with column ID,UserPrincipalName,Email, you can do something like this:

`Import-CSV blabla.csv  | % { Set-Mailbox -Identity $_.ID -MaxSendSize 25mb -MaxReceiveSize 35mb }`

where we are referencing the first column of the CSV and for each of its values, running the Set-Mailbox cmdlet against the corresponding user. Thus, it's important to have proper values for the ID column, not only values that actually exists in the tenant, but such that uniquely identify a given user/mailbox. This is the reason why we usually recommend to use something like the UPN, or the objectID. Other values, such as an email address or even display name can also work, but don't guarantee uniqueness, and thus might cause the cmdlet to fail.

Anyway, this is how you can use for example an "Email" column - all you need to do is reference it:

```
Import-CSV blabla.csv  | % { Set-Mailbox -Identity $_.ID -MaxSendSize 25mb -MaxReceiveSize 35mb }
```

You don't need to have all three columns in the CSV either, that's just for the sake of example.
