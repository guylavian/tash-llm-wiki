---
title: "how to setup Exchange Send Connect FQDN for redundant ISP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194340/how-to-setup-exchange-send-connect-fqdn-for-redund
question_id: 2194340
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-networking-other"]
---
# how to setup Exchange Send Connect FQDN for redundant ISP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194340/how-to-setup-exchange-send-connect-fqdn-for-redund (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have used Exchange for many years for our clients, but recently with Internet Outages increasing we are moving toward redundant/mixed media (fiber, COAX, 4G/5G) to ensure if one goes down, the client has Internet.  We are pretty much through the firewall changes, but did have a question how to support having the ability to change the FQDN for the Send Connector depending on which ISP is currently up and running?  Obviously we have gone to each of the two ISPs and setup reverse record (PTR) for the two MX records, but how do  you specify this for the FQDN for the send connector as it only supports a single host name.

Thanks in advance,

Brian Warner

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-22*

Thanks, Jill.  Like your suggestions and thoughts.  You are suggesting for #2 that we use;

Set-SendConnector

Right?  We can use something like:

(Invoke-WebRequest -uri "https://api.ipify.org/").Content

and set the FQDN based on this with a scheduled task, right?  Really wish there was something built into Exchange to handle this.

Thanks,,

Brian

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-22*

Hello,

Thank you for posting in Microsoft Community forum.

For send connectors in Exchange servers, typically only one fully qualified domain name can be specified, which may cause issues when switching ISPs.

To ensure that email sending is not interrupted due to a malfunction of a particular ISP, we recommend that you try the following methods:

-  Try switching manually. Set up two send connectors: create separate send connectors for each ISP, with each connector specifying a different FQDN and corresponding SMTP server. When a problem is detected with an ISP, manually disable the current send connector and enable the backup send connector.

-  Attempt to create a script for automated switching. Write a PowerShell script to detect the current active ISP and automatically switch the FQDN of the sending connector. Use Task Scheduler: Configure the script to run periodically or trigger when a network switch is detected.

-  Use load balancer devices or software that support SMTP to configure the FQNFNs of different ISPs. When an ISP is unavailable, the load balancer will automatically switch to a backup ISP.

The simplest implementation method is to automatically switch the FQDN through a script. Manual switching is suitable for small networks and temporary solutions, while load balancers are suitable for large enterprises and environments that require high availability. Choose a solution that suits your needs to ensure the continuity and reliability of email sending.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

﻿

Regards,

Jill Zhou
