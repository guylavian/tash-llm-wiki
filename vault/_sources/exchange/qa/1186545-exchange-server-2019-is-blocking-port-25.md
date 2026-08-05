---
title: "Exchange Server 2019 is blocking port 25?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186545/exchange-server-2019-is-blocking-port-25
question_id: 1186545
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server 2019 is blocking port 25?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186545/exchange-server-2019-is-blocking-port-25 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have setup a windows server 2022 with Exchange 2019 and am unable to send out email because outgoing port 25 is blocked.

I have done the following:

Stopped the firewall (Windows Defender) completely

Uninstalled virus protection

Updated the LAN driver to the latest Intel driver

Checked the OS several different ways for corruption

None of that has mattered.

NMAP shows that port 25 is open on the new server from my home office, but closed when I go from the new server to my home office Exchange Server.

Further, telnet testing shows I can connect to the new server from my home office but I can connect from the new server to my Home Office Exchange Server on port 25 nor to portquiz.net.

Can you think of any way or reason that Windows Server 2022 or Exchange Server could be blocking port 25?  Or any other testing I could do?

Vultr.com says they have removed the default SMTP block from my account.  They claim the port is open.

Thanks in advance for your help.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-06*

Do you run Windows antivirus programs on Microsoft Exchange servers, you could follow this article to Check AV exclusion state. Can you send out mails? Have you ever updated windows?

You could try to restart server and check if this issue continues.

I found a similar thread for your reference.  

Also check this article for more insight - https://www.alitajran.com/isp-blocks-smtp-port-25/

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-06*

Hi @Craig M,

unable to send out email because outgoing port 25 is blocked.

Just wondering what makes you believe that the outgoing port 25 is blocked on your side?

Besides, could you run the get-messagetrackinglog cmdlet to check the mail flow on a failed message?

 

```
Get-TransportService|Get-MessageTrackingLog -MessageSubject  -Sender  -Recipients  |ft timestamp,EventID,ClientHostname,ServerHostname,Source,ConnectorID -autosize
```

 Such as:

 Furthermore, to view the usage of Port 25, please try:  

- 

- 

-  Open EMS with administrator in Exchange server, then run below cmdlet:  

```
netstat -aon|findstr "25"
```

  

- 

-  Then run below command with PID to find the application, for example:  

```
tasklist|findstr "1852"
```

- 

-  At last please login EAC and locate to Receive Connector under Mail flow, open "Default FrontEnd <server name>", then double check the settings as below:

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-03-05*

Can you provide Netstat -an result and also check if in the Windows Firewall - Inbound Rule for Port 25 is allowed?
