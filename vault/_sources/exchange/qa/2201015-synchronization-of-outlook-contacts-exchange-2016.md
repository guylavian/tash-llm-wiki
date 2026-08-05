---
title: "synchronization of outlook contacts / exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2201015/synchronization-of-outlook-contacts-exchange-2016
question_id: 2201015
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# synchronization of outlook contacts / exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2201015/synchronization-of-outlook-contacts-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We need to automatically synchronize contacts into our outlook (on premise / exchange 2016).

Those contacts are created into our CRM and we can extract them with an API.

How to create them into outlook?

We do not want to use csv import, and we need them to be linked to sales employees, and not all the employees.

How to do it please?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-05*

Hi,

We are not using dynamics, but another CRM, which provides API, so I can easily retrieve contacts, and store them in a csv file.

My question is how can we mass upload this CSV file into outlook, on a daily basis? we are on a on premise version of exchange 2016.

So far, the only way I have found is to manually upload the csv via the import function.

This is not possible to do it because:

-  this function will link contact to a unique employee

-  this import is manual

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-05*

Hi @Gauthier BANDEL (Société LCI),

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, your issue is syncing contacts from CRM to outlook.

If you use Dynamics 365, when you use server-side sync, Dynamics 365 contacts and activities (including emails, appointments, contacts, and tasks) are synchronized to your specified email system (such as Exchange). More information about server synchronization can be found in the documentation: Connect to Exchange Server (on-premises) - Power Platform | Microsoft Learn

In addition, using Microsoft Dynamics CRM for Outlook makes it easier to synchronize CRM information with Outlook mail, Personal Planner and Contacts. For more details, please refer to the link: Microsoft Dynamics CRM For Outlook: Why & How To Get Started

Please note that the URLs provided above are three-way links. The content and updates of the web pages are not under the control of Microsoft and are provided for informational purposes only. Microsoft is not responsible, directly or indirectly, for any errors, inaccuracies or mistakes in the information provided. Please understand that. Please ensure that you adopt it with a full understanding of its risks.

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.
