---
title: "Exchange Management Shell not connecting after Installed Exchange Server CU 23 update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/428097/exchange-management-shell-not-connecting-after-ins
question_id: 428097
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Management Shell not connecting after Installed Exchange Server CU 23 update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/428097/exchange-management-shell-not-connecting-after-ins (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I am Rubiat,  

Few months ago, I was updated Exchange Server 2013 CU 23. After installation done, I couldn't connect to exchange management shell to revert maintenance mode. I have 4 mailbox servers. Two servers in DC site and another 2 in DR site. The problematic server is in DR site and rest of the servers are ok after CU 23 installed. When I open exchange management shell, it takes few seconds and then prompt an error and then connect to another server management shell which is in my DR site.   

The prompt error is "Connecting to remote server failed with the following error message : The WinRM client cannot process the request. It cannot determine the content type of the HTTP response from the destination computer. The content type is absent or invalid. For more information, see the about_Remote_Troubleshooting Help topic."  

I have tried almost all basic solutions like recycle MsExchangePowerShellAppPoll, webconfig file checking, directory path checking etc. Now, please provide me an appropriate solution to fix it. It is very urgent for me.   

Note: Problematic server is still in maintenance mode.  

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-10*

Hi,    

Have you tried taking the problematic server out of maintenance mode with the other server's EMS?     

    Set-ServerComponentState "EX01" -Component ServerWideOffline -State Active -Requester Maintenance  

    Set-ServerComponentState "EX01" -Component HubTransport -State Active -Requester Maintenance  

Or run EMS via windows powershell:    

```
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn
```

Then restart MSExchangeTransport and MSExchangeFrontEndTransport service on the problematic server.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
