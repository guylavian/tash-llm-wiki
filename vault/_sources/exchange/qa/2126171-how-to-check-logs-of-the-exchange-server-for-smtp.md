---
title: "How to check logs of the Exchange Server for SMTP connection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2126171/how-to-check-logs-of-the-exchange-server-for-smtp
question_id: 2126171
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to check logs of the Exchange Server for SMTP connection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2126171/how-to-check-logs-of-the-exchange-server-for-smtp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Since we need to connect for SMTP functionality but the connection failed and the vendor said the packet has been sent but there is no response from the Exchange server, we want to check the Exchange server logs and fix this issue.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-04*

You can use the ping command to test connectivity: ping 10.58.252.11. With that you can check if the server hosting the SMTP service (10.58.252.11) is reachable from your Exchange Server.  

You can also confirm that the SMTP service is running on the server with IP 10.58.252.11. You can use telnet to check if the SMTP port (25) is open: telnet 10.58.252.11 25.  

Other than that, to check Exchange logs, you can refer to the article below- Configure logging- https://learn.microsoft.com/en-us/exchange/mail-flow/transport-logs/configure-connectivity-logging?view=exchserver-2019  

Log structure and fields- https://learn.microsoft.com/en-us/exchange/mail-flow/transport-logs/connectivity-logging?view=exchserver-2019  

So enable the logging, locate them and analyze them. The log files are in CSV format and can be opened with any text editor or spreadsheet application. Each log entry includes details such as the date and time, session ID, source and destination IP addresses, and the SMTP commands exchanged.
