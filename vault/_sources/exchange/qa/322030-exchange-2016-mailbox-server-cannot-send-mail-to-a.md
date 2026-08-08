---
title: "Exchange 2016 Mailbox Server cannot send mail to another 2016 Mailbox Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/322030/exchange-2016-mailbox-server-cannot-send-mail-to-a
question_id: 322030
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 Mailbox Server cannot send mail to another 2016 Mailbox Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/322030/exchange-2016-mailbox-server-cannot-send-mail-to-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently upgraded one of the Exchange Mailbox 2016 Servers with CU19 while the other one is still running on CU11. After upgrading the second mailbox server to CU19, first mailbox server (CU11) can't send mails to another mailbox server (CU19) and vice-versa. Getting "Exchange Auth Failure". When checked logs, getting "target machine actively refused the connection". Default receive connector is having "Exch. Server Auth." enabled. I am even able to TELNET both the mailbox servers from each other. No SMTP inspection enables on firewalls. Any ideas please?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-22*

Hi @RAJEEV GUJRAL   ,    

Are the two Exchange servers in the same domain?    

Can mailbox in these two Exchange servers send mail to external recipients or receive mail from external senders?    

Are there any non-delivery reports generated when the email fails to be sent? If so, please share the complete report with us, please noted that covering your personal information.    

Microsoft does not recommend deploying any firewall or network equipment between internal Exchange servers. Please make sure that all communications and traffic between your internal Exchange servers are not restricted, and make sure that you open all ports required by Exchange. In addition, if possible, please try to temporarily turn off the firewall to check whether the mail can be sent successfully.    

For more information you could refer to: Network ports for clients and mail flow in Exchange    

The following screenshot is the defaul settings of Default receive connector in exchange server, you can compare with the receive connector in your environment.    

    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
