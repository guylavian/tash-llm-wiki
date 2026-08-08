---
title: "About the default app settings in GPOs in Windows Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1411427/about-the-default-app-settings-in-gpos-in-windows
question_id: 1411427
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# About the default app settings in GPOs in Windows Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1411427/about-the-default-app-settings-in-gpos-in-windows (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For example, if you add multiple lines to the following extension pdf in the configuration file,

<Association Identifier=".pdf" ProgId="MSEdgePDF" ApplicationName="Microsoft Edge" />

<Association Identifier=".pdf" ProgId="AcroExch.Document.2017" ApplicationName="Adobe Acrobat Reader 2017" />

<Association Identifier=".pdf" ProgId="Acrobat.Document.DC" ApplicationName="Adobe Acrobat" />

What is the application flow of the behavior?

Not limited to the above, but set the HTML extension etc. to multiple lines of separate apps

I think it will be the same if you install a separate app for each client、、、

-  Only the top is applied, and clients that are not included are not changed.

・ Check in order from the top and change it for the included clients

-  Since there are multiple lines, an error occurs and it is not changed for all clients.

I think it is one of them, but just in case, I will ask you here for confirmation as well.

Best regards.

## Answers

_No answers on this thread._
