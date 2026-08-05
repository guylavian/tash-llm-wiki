---
title: "My exchange 2016 cannot use outlook(autodiscover cannot work)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1389393/my-exchange-2016-cannot-use-outlook-autodiscover-c
question_id: 1389393
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# My exchange 2016 cannot use outlook(autodiscover cannot work)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1389393/my-exchange-2016-cannot-use-outlook-autodiscover-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear,

recently I had outlook issue, I cannot config outlook to connect to my exchange.

I tried the Microsoft connection test and the failure log as below:

因为从 Unknown 收到 HTTP 404 - 404 响应，所以发生

 Web 异常。 

HTTP 响应头: 

Connection: close 

Content-Length: 315 

Content-Type: text/html; charset=us-ascii 

Date: Thu, 12 Oct 2023 05:18:04 GMT 

Server: Microsoft-HTTPAPI/2.0

while when I tried the url https://autodiscover.mydomain.com/autodiscover/autodiscover.xml, i could get the blow:

however, when I tried to access https://mail.mydomain.com/autodiscover/autodiscover.xml, after login, it can access successfully.

i also tried to check the DNS, and I have setup autodiscover.mydomain.com as alias and point to mail.mydomain.com.

so how do I repair it?

many thanks in advance.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-13*

Hi @老马

First of all, there is some information that needs to be confirmed. Does this problem occur to one user or does it occur to all users? And  does this happen within the domain or outside the domain?  In addition, you can use Test Email Autoconfiguration to check the specific situation first. The specific steps are as follows:

-  Start Outlook.

-  Press and hold the Ctrl key, right-click the Outlook icon in the notification area, and then click Test E-mail AutoConfiguration.

-  Verify that the correct email address is in the E-mail Address box.

-  In the Test E-mail AutoConfiguration window, click to clear the Use Guessmart check box and the Secure Guessmart Authenticaton check box.

-  Click to select the Use AutoDiscover check box, and then click Test.

When your test is completed, please copy and paste the results to better troubleshoot the next step. For more information, please refer to this document: Mailboxes - Test E-mail AutoConfiguration

If the current Outlook cannot be opened because no account can be configured and thus you cannot use Test Email Autoconfiguration, you can refer to this document first to create an empty configuration file without an account. For details, please refer to Use Outlook without an email account - Microsoft Support

Typically, if it is inside the domain, clients connected to the domain can use the SCP object directly to find the Autodiscover service. You can use the Get-ClientAccessService | fl autodiscoverserviceinternaluri command to confirm that the fqdn in the URL is the correct exchange server. If it is an external environment, the CNAME record needs to be added in the public network DNS environment, not the intranet DNS, pointing to the mailbox server fqdn that can be accessed from the public network. For more information, please refer to this document: Autodiscover service in Exchange Server | Microsoft Learn

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

 

Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
