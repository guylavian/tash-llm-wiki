---
title: "Connecting a Web App Hosted in Azure to Exchange Online via Graph API"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1437914/connecting-a-web-app-hosted-in-azure-to-exchange-o
question_id: 1437914
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Connecting a Web App Hosted in Azure to Exchange Online via Graph API

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1437914/connecting-a-web-app-hosted-in-azure-to-exchange-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to build a connection from a custom web app hosted in Azure (with backend in App Function) to my company's Exchange Online account. 

The goal is to connect to one shared inbox of Exchange Online, check emails which came in the last e.g. 1 hour and download attachments from these emails. Is it possible to connect via Graph API? 

Should it be like: the web application via Graph REST API calls corporate Exchange Online and then get messaget and attachments for specific account? Is there any better architecture for achieve that?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-29*

Yes, it is possible using the Microsoft Graph API. However, you will need to have the appropriate permissions and authentication to do so.

Here are some steps you can follow to achieve your goal:

-  First, you will need to register an application in Azure Active Directory and grant appropriate permissions (application permissions would be prefered), which allows the app to read mail in all mailboxes without a signed-in user¹.

-  After you need to get the access token, you can use it to make requests to the Microsoft Graph API to access the shared inbox. You will need to specify the shared mailbox address in the URL, for example: https://graph.microsoft.com/v1.0/users/{sharedmailboxmailaddress}/messages. You can also use query parameters to filter the messages by date, for example: [https://graph.microsoft.com/v1.0/users/{sharedmailboxmailaddress}/messages?$filter=receivedDateTime ge 2023-03-02T00:00:00Z to get the messages received after March 2, 2023³.

-  To download the attachments from the messages, you will need to get the message ID and the attachment ID from the response, and then make another request to the following URL: https://graph.microsoft.com/v1.0/users/{sharedmailboxmailaddress}/messages/{messageid}/attachments/{attachmentid}/$value. This will return the binary content of the attachment, which you can save to a file.

below are some links which can help in process.

https://learn.microsoft.com/en-us/graph/api/message-get?view=graph-rest-1.0&tabs=http

https://learn.microsoft.com/en-us/answers/questions/1186134/how-can-i-fetch-emails-from-shared-email-address-%28.

https://learn.microsoft.com/en-us/graph/api/attachment-get?view=graph-rest-1.0&tabs=http

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-27*

Thank you very much for your valuable reply. I assume we can connect the same way to also individual inboxes, not only shared ones?
