---
title: "[Migrated from MSDN Exchange Dev]Auditing for owner logins"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/145812/migrated-from-msdn-exchange-dev-auditing-for-owner
question_id: 145812
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Auditing for owner logins

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/145812/migrated-from-msdn-exchange-dev-auditing-for-owner (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.    

Hi!    

I have the following scenario:    

I need to register the IP address that accessed a particular mailbox and the access will be done through an outlook client, so I enabled auditing on the mailbox in question and configured it to register the “MailboxLogin” action for Owner:    

Set-Mailbox -Identity "Ben Smith" -AuditEnabled $true    

Set-Mailbox -Identity "Ben Smith" -AuditOwner MailboxLogin -AuditEnabled $true    

But according to the article below, this configuration does not work for NTLM and Kerberos (which is my case):    

"Auditing for owner logins to a mailbox works only for POP3, IMAP4, or OAuth logins. It doesn't work for NTLM or Kerberos logins to the mailbox."    

https://learn.microsoft.com/en-us/exchange/policy-and-compliance/mailbox-audit-logging/mailbox-audit-logging?view=exchserver-2016    

So far I have not been able to register the IP that accesses this particular mailbox, this is my goal, so if anyone has any idea how to register this information, please let me know.    

Best regards,    

Renato.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-04*

Hi @RENATO MAIA   ,  

According to my research, you can obtain the IP address of the Outlook client to log in to the mailbox in the following ways.  

-  We could login to our mailbox through outlook client, then we check the security log in the event viewer on DC or computer with Exchange server installed. If there have the Event Id 4024, it means you are successfully logged in. We can refer to the "Source Network Address" parameter to view the client's IP.  

Source Network Address [Type = UnicodeString]: IP address of machine from which logon attempt was performed.  

For more information: 4624(S): An account was successfully logged on.  

  

-  If you want to view the previous login records. We open the IIS log, we could see the specific user access time, user name ,client ip address and logon status through IIS logs. In order to better analyze the IIS log, we can use Excel to analyze the IIS log. The parameter c-ip represents the client IP address.  

IIS Log: C:\inetpub\logs\LogFiles.  

-  Open the file in notepad.  

-  Remove the first entry from #Software to #Fields: in order to only keep the field definitions at the beginning of the file.  

-  Search for #  

-  Remove any entries you'll find of the following type to only get in the log file the first field definitions and a list of requests as above:    #Software: Microsoft Internet Information Services 8.0  

    #Version: 1.0  

    #Date: 2013-09-11 14:05:06  

    #Fields: date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) cs(Referer) sc-status sc-substatus sc-win32-status time-taken  

5) Once you've done this, save the file and open it using Excel.  

For more specific steps, you can refer to: How to use Excel to analyse IIS Logs

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-30*

Additional Information.  

I have microsoft exchange 2016 on premise and we don't have a hybrid environment.  

To find the audit logs for the "MailboxLogin" action, I used this command:  

Search-MailboxAuditLog -Identity "Ben Smith" -LogonTypes Owner -ShowDetails -StartDate 10/26/2020 -EndDate 10/29/2020 | Where-Object {$_.Operation -eq "MailboxLogin"}  

But without success.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-30*

Hi ,    

According to my research, in the Exchange server, only Mailbox audit log can record who logs in to the mailbox and the client’s IP address.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
