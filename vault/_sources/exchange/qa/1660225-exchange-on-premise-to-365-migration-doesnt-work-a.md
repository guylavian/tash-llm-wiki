---
title: "Exchange on-premise to 365 migration doesn't work anymore"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1660225/exchange-on-premise-to-365-migration-doesnt-work-a
question_id: 1660225
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange on-premise to 365 migration doesn't work anymore

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1660225/exchange-on-premise-to-365-migration-doesnt-work-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

Since a week our mailbox migration jobs won't complete anymore.

After a while they end with an error as seen below...

Status

Data migrated:

Migration rate:

Error: TimeoutErrorTransientException: The call to 'https://mydomain/EWS/mrsproxy.svc' timed out. Error details: The request channel timed out attempting to send after 00:00:00.0049846. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a longer timeout. --> The HTTP request to 'https://mydomain/EWS/mrsproxy.svc' has exceeded the allotted timeout of 00:00:00.0049846. The time allotted to this operation may have been a portion of a longer timeout. --> The request channel timed out attempting to send after 00:00:00.0049846. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allotted to this operation may have been a portion of a longer timeout. --> The HTTP request to 'https://mydomain/EWS/mrsproxy.svc' has exceeded the allotted timeout of 00:00:00.0049846. The time allotted to this operation may have been a portion of a longer timeout.

Notice that tiny timeout. that's half a milisecond which seems ridiculous low.

Strange thing is that I can access the EWS page from external without any problems and I get the same page as the last screenshot on this page.

https://www.codetwo.com/kb/how-to-find-ews-url/

I tried disabling en re-abling the proxy with the commands below just to be sure:

```
Get-WebServicesVirtualDirectory | Set-WebServicesVirtualDirectory -MRSProxyEnabled $false
Get-WebServicesVirtualDirectory | Set-WebServicesVirtualDirectory -MRSProxyEnabled $true
```

I removed the end point and when creating it with the checkbox ticked to verify it it hang at creating.

With the checkbox unticked it created right away but it still doesn't seem to work.

What else can I check to get this working again? (it used to work fine for 2+ years but sometime this error showed up and then I just had to restart the sync or worst case delete the migration task and recreate it)

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-26*

Hi @GVB,

According to the information above, you could refer to the followings:

-  Check again the on-premises infrastructure, especially proxy and firewall settings. Ensure your firewall settings to allow connections from O365. You can refer to Microsoft 365 URLs and IP address ranges - Microsoft 365 Enterprise | Microsoft Learn for more information.

-  You could check your network devices logs and IIS logs / HTTPProxy logs, usually if the timeout happens very quick (under 50 sec) it could probably be a network device that is blocking or closing the connection.

-  Also, check if exchange self-signed certificate is missing in the Exchange Servers.

You can refer scenario 1 in the document for more information: Troubleshooting Hybrid Migration Endpoints in Classic and Modern Hybrid - Microsoft Community Hub
