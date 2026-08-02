---
title: "Outlook Add-in deployment for Exchange - not allowed in desktop client"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1597144/outlook-add-in-deployment-for-exchange-not-allowed
question_id: 1597144
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-development-routing-development-other", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# Outlook Add-in deployment for Exchange - not allowed in desktop client

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1597144/outlook-add-in-deployment-for-exchange-not-allowed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I'm currently working on deploying an outlook add-in. However, at the last steps of the deployment, it seems as though we are hitting a wall - and I cannot fully understand what is happening from the documentation. We are deploying an add-in as .xml specification through the exchange admin panel, and adding it for all users. 

When the add-in is added through this panel, after a couple minutes it shows up for both online users (OWA), and outlook client. Here, very different things happen:

-  OWA: It works, the javascripts loads succesfully and it is able to process data from the outlook js api. 

-  Offline (Desktop): The add-in shows up, but we're unable to open it: "You cannot perform this action. Add-ins are not supported in this folder". 

I don't understand how this is possible. Why are the permissions different dependent on the client that we're using? From the documentation:

-  https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/delegate-access?tabs=windows%2Cjsonmanifest

-  https://learn.microsoft.com/en-us/javascript/api/requirement-sets/outlook/outlook-api-requirement-sets?view=common-js-preview&tabs=xmlmanifest#using-apis-from-later-requirement-sets

It appears that shared folders/ mailboxes are only supported for mailboxes which support higher API requirement set than is available on any Exchange on-premises implementation. Do the OWA and Desktop clients communicate to servers with different API versions?

FYI: Adding the SupportsSharedFolders element to the xml breaks us being able to add the add-in through the admin panel. 

FYI 2: The users are able to use a Salesforce add-in in the shared folders, so it doesn't seem to be the case that add-ins are totally impossible in the Desktop environment.
Kind regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-06-14*

Hi Cas Teeuwen

The Outlook Web App (OWA) and the Outlook desktop client can indeed behave differently. This is because they might be using different versions of the Outlook API. The OWA is always up-to-date with the latest API, while the desktop client’s API version depends on the installed version of Outlook and the Exchange server’s configuration. https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/understanding-outlook-add-in-permissions

Note: Adding this element can cause issues if the Exchange server or the Outlook client doesn’t support the necessary API requirement set. It’s also worth noting that an issue has been reported where the SupportsSharedFolders tag is not honored in certain scenarios. It’s important to try to check if the Salesforce add-in might be using different APIs or methods to achieve this.

`# If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".`
