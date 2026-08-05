---
title: "Installing Exchange 2016 into Exchange 2010 environment for migration to O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1285359/installing-exchange-2016-into-exchange-2010-enviro
question_id: 1285359
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Installing Exchange 2016 into Exchange 2010 environment for migration to O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1285359/installing-exchange-2016-into-exchange-2010-enviro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We want to install an Exchange 2016 server into an existing Exchange 2010 environment in order to create a hybrid configuration between the Exchange 2016 server and Office 365.  We will move mailboxes in batches from the Exchange 2010 server to the Exchange 2016 server, and then migrate them in batches up to Office 365:

-  Single domain, single forest with functional level Windows 2012

-  Single Exchange 2010 SP3 server w/Update Rollup 32

-  Office 365 tenant is already in place

-  Azure AD Connect is in place and syncing

-  Windows 2016 server provisioned for Exchange 2016 install

Question 1

I have found the following prereqs that need to be installed before running the Exchange 2016 install...are these accurate?

-  dotNet Framework 4.8

-  December 13, 2016 (KB3206632) security update

-  Visual C++ Redistributable Package for Visual Studio 2013

-  IIS URL Rewrite Module

-  Microsoft Unified Communications Managed API 4.0, Core Runtime 64-bit

Question 2

There is a long list of Windows 2016 Roles and Features that have to be installed for Exchange 2016.  Should these be installed before running the Exchange 2016 install, or will the GUI Exchange 2016 Setup wizard install them?

Question 3

Is it necessary to run the AD Schema prep and the AD prep before running the GUI Exchange 2016 Setup wizard, or will the GUI Exchange 2016 Setup wizard perform this prep?

thanks!

Paul

## Answers

_No answers on this thread._
