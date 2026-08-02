---
title: "SMTP Exchange online Oauth implementation - Client Credential flow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1538272/smtp-exchange-online-oauth-implementation-client-c
question_id: 1538272
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-development-routing-development-other", "microsoft-security-ms-graph", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# SMTP Exchange online Oauth implementation - Client Credential flow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1538272/smtp-exchange-online-oauth-implementation-client-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys,
We are currently using Basic authentication in exchange online for SMTP and want to move to Oauth protocol.
We want to use the client credentials grant flow to achieve the same.
I read the following document:
	https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth
in which there is a section for:
	Use client credentials grant flow to authenticate SMTP, IMAP, and POP connections	https://learn.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth#use-client-credentials-grant-flow-to-authenticate-smtp-imap-and-pop-connections	
However,
In the document above it says This documentation uses the deprecated Outlook REST API scope. New applications should use the Graph REST API Endpoint instead.
I couldn't find a way to use Graph REST API Endpoint to achieve the same. On Azure portal after selecting the application, API permissions > Add a permission > Microsoft Graph > Here under Delegated permission i could find "SMTP.Send" but for this I will have to log in the user, which is not my case. I want to use Client credentials grant flow and I couldn't find anything related to SMTP in API permissions > Add a permission > Microsoft Graph > Application permissions.
Am i missing something here?
Please do help!!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-02-19*

That article is a bit of a mess and needs some cleanup. I can confirm that there are no application permissions within the Graph that you can use for this tasks, so the solution is to still use the Exchange Online resource (https://outlook.office365.com/.default) and the SMTP.SendAsApp permission.
