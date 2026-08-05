---
title: "Issue with accessing accessing ECP in exchange2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1728775/issue-with-accessing-accessing-ecp-in-exchange2019
question_id: 1728775
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issue with accessing accessing ECP in exchange2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1728775/issue-with-accessing-accessing-ecp-in-exchange2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are not able to login to the Exchange 2019 ECP after logging to the ECP portal on both internal and external URL.

We have performed IIS reset, CAS update, recreated virtual directory, rebooted exchange servers also validated IP domain restriction nothing is preset, can someone help on this.

Only we have client access rule restriction. that is allowing the source from where I'm trying to connect.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-26*

Hi @Nandan NK，

Welcome to the Microsoft Technical Support Forum.

Based on your description, you are currently unable to log on to the Exchange 2019 ECP. 

I suggest that you try the following methods to troubleshoot the error: 

-  Clear your browser cache or try to access the ECP from another browser or incognito window. 

-  Make sure that the DNS configuration of the internal and external URLs is correct and can be resolved to the correct IP address. 

-  Make sure that the SSL certificate assigned to the ECP virtual directory is valid and has not expired. You can check this under the bindings of the ECP site in IIS Manager. 

-  Make sure that the client access rules are configured correctly. Sometimes they can inadvertently block access. Rules can be viewed and edited using the Exchange Management Shell. 

Get-ClientAccessRule | Format-Table Name, Action, Priority 

If necessary, you can temporarily disable client access rules to see if they are the cause: 

Disable-ClientAccessRule -Identity "RuleName"

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
