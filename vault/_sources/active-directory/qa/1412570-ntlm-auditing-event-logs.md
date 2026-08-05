---
title: "NTLM Auditing - Event logs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1412570/ntlm-auditing-event-logs
question_id: 1412570
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# NTLM Auditing - Event logs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1412570/ntlm-auditing-event-logs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently enabled autiting of NTLM events. I am just trying to understand the output from the security log Microsoft\NTLM logs view.

I am seeing multiple events with the same device listed in Secure Channel name with different workstations.

Which is the item I need to be concerned about? the S-Channel or Workstation?

The event looks something like this.  So, I might have 50 events from the same S-Channel name but differing workstation names

Domain Controller Blocked Audit: Audit NTLM authentication to this domain controller.

Secure Channel name: Server-1

User name: Bob

Domain name: Mydomain

Workstation name: Server-2

Secure Channel type: 2

Audit NTLM authentication requests within the domain mydomain that would be blocked if.. 

I've tried a couple of different PS scripts I found online to interrogate these logs, neither work. one only lists the same S-Channel name in every item the other returns nothing.

example: (lists the same entry repeatdly)  

$Events = Get-WinEvent -Logname security -FilterXPath "Event[System[(EventID=4624)]]and Event[EventData[Data[@Name='LmPackageName']='NTLM V1']]" | Select-Object `

@{Label='Time';Expression={$_.TimeCreated.ToString('g')}},

@{Label='UserName';Expression={$_.Properties[5].Value}},

@{Label='WorkstationName';Expression={$_.Properties[11].Value}},

@{Label='LogonType';Expression={$_.properties[8].value}},

@{Label='ImpersonationLevel';Expression={$_.properties[20].value}}

$Events | Out-GridView

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2023-11-03*

Hi,

You need to append a backtick (`) character to each line of a command if it's split into multiple lines. Please see if this works.

```
$Events = Get-WinEvent -Logname security -FilterXPath "Event[System[(EventID=4624)]]and Event[EventData[Data[@Name='LmPackageName']='NTLM V1']]" | Select-Object `
@{Label='Time';Expression={$_.TimeCreated.ToString('g')}}, `
@{Label='UserName';Expression={$_.Properties[5].Value}}, `
@{Label='WorkstationName';Expression={$_.Properties[11].Value}}, `
@{Label='LogonType';Expression={$_.properties[8].value}}, `
@{Label='ImpersonationLevel';Expression={$_.properties[20].value}}
$Events | Out-GridView
```

Best Regards,

Ian Xue

If the Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
