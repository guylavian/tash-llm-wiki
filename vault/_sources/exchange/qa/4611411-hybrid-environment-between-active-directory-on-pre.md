---
title: "Hybrid Environment between Active Directory On Premise - Azure Active Directory | SAM Account name character constraint limitation of 20 characters."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4611411/hybrid-environment-between-active-directory-on-pre
question_id: 4611411
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Volunteer Moderator"]
---
# Hybrid Environment between Active Directory On Premise - Azure Active Directory | SAM Account name character constraint limitation of 20 characters.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4611411/hybrid-environment-between-active-directory-on-pre (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

The Identity project that I am within my company, I understand the following to be true

-  That there is a constraint in the length of the SAM account name field.  (SAM account name, also called the "pre-Windows 2000 logon name," which takes the form domainuser (Active Directory attribute name: sAMAccountName) This constraint means that retail employees that have a firstname, middlname, surname combination that exceed the 20 character length will fail the joiner automation in AD Manager Plus. 

-  The SAM Account name limit is tied to the on-premise AD instance. 

-  Azure AD, the resulting digital identity that is generated in Azure AD, is not limited by character length. Email address & email address alias do & can exceed the character limit imposition of 20 characters tied to the SAM account name. 

The Questions for Microsoft are as follows:

-  Is the working understanding as documented above correct?

-  If there is a SAM account character restriction of 20 characters in length, is this a hard limit that cannot be changed?

In an ideal world, Retail would request a SAM account name to allow for 30 characters.

What are the options / compromises to configure AD to 

A - Create a SAM account from a username that exceeds 20 characters by truncating the name

B - Create a SAM account name, with the full email address name, as the user would like, in AAD

C - Have AD Manager create an exception report that can be sent to an administrator to use their manual judgement to create a SAM account from the user name in a restricted format & then manually create the email address (that exceeds the 20 character SAM account limit) so that the digital identity adheres to the full username. 

Supporting Artefacts 

-  Retail Account Long Names - please see a list of long names from Retail, that will require a digital identity.

-  Msft KB articles that may be of relevance

SAM-Account-Name attribute - Win32 apps | Microsoft Learn

“The SAMAccountName attribute is a logon name used to support clients and servers from previous version of Windows, such as Windows NT 4.0, Windows 95, Windows 98, and LAN Manager. The logon name must be 20 or fewer characters and be unique among all security principal objects within the domain.”

User profile attributes in Azure Active Directory B2C | Microsoft Learn

Display Name in Azure AD can be 256 characters

(I don’t believe that my organisation is using Azure Active Directory B2C, but we are do have a hybrid setup, AD on premise linked to AAD via AD Connect.

The questions are

-  Hybrid Environment between Active Directory On Premise - Azure Active Directory | is there an absolute finite constraint of 20 characters for the SAM Account name? 

-  Does this configuration mean that when we provision new user accounts, that are restricted to a [firstname.middlename.lastname]@com constraint of 20 characters for the persons name in [brackets] ?

-  What is the guidance from  Msft where we have members within the organisation that have [firstname.middlename.lastname] combination that exceed 20 characters?

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-04-28*

You may contact dedicated forum Microsoft Exchange Hybrid Management on Microsoft Q&A for further assistance. Here is the forum link: https://learn.microsoft.com/en-us/answers/tags/377/office-exchange-hybrid-management?page=2
