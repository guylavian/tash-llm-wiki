---
title: "How to check the Exchange Server log for SMTP connection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2126100/how-to-check-the-exchange-server-log-for-smtp-conn
question_id: 2126100
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to check the Exchange Server log for SMTP connection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2126100/how-to-check-the-exchange-server-log-for-smtp-conn (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Support Team,

Since we need to connect for SMTP functionality but the connection failed and the vendor says the packet has been sent but there is no response from the Exchange server, we want to check the Exchange server logs and fix this issue.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-04*

Hi, @Kenneth Dias

Thanks for posting your question in the Microsoft Q&A forum.

According to your description, you have encountered an SMTP connection failure, and the image information you provided shows "Unable to connect to SMTP host". You can try the following steps to see if the problem can be solved:

-  Try to use Telnet to test SMTP communication on the Exchange server. Enter telnet in the command prompt to open a Telnet session, enter set localecho, and enter the target SMTP server, source domain, sender, and recipient email addresses in order. Then check the success and error messages in the Telnet session.

Refer to: https://learn.microsoft.com/en-us/exchange/mail-flow/test-smtp-telnet?view=exchserver-2019#step-3-use-telnet-on-port-25-to-test-smtp-communication

-  Try to use the ping command `ping 10.58.252.11` to test whether the SMTP server at 10.58.252.11 is accessible from your Exchange server.

-  In EAC, you can check the configuration connection log: Select Server > Server, select the mailbox server to configure, and then click "Edit" > "Transport Log" > "Connection Log" > "Enable Connection Log". If enabled, the log file is usually located under "%ExchangeInstallPath%TransportRoles\Logs".

Refer to: Configure connectivity logging in Exchange Server | Microsoft Learn

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who have encountered similar problems and are looking for solutions. Thank you.

Best,

Jeanne
