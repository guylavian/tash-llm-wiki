---
title: "Powershell failing over HTTPS to Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/322619/powershell-failing-over-https-to-exchange-2019
question_id: 322619
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Powershell failing over HTTPS to Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/322619/powershell-failing-over-https-to-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an application that sends Powershell commands to Exchange 2016 over HTTPS. I have set up a new Exchange 2019 server, and Powershell from the same application to the Exchange 2019 server is failing with:  

New-PSession: Connecting to remote server myserver.domain.com failed with the following error message: The SSL connection cannot be established. Verify that the service on the remote host is properly configured to listen for HTTPS requests.  

I compared the Powershell virtual directories on each server, and confirmed that they are configured the same.  I verified that the PowerShell execution policy is set to RemoteSigned on both servers.  The new server has a valid SSL certificate. Does anyone have any ideas on what I'm missing?  

Thank you

## Answers

_No answers on this thread._
