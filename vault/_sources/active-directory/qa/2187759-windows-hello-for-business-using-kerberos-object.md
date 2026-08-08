---
title: "Windows Hello for Business using Kerberos Object"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187759/windows-hello-for-business-using-kerberos-object
question_id: 2187759
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Windows Hello for Business using Kerberos Object

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187759/windows-hello-for-business-using-kerberos-object (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi guys,
We are trying to deploy Windows Hello for Business in our hybrid environment, but one of the stages we need to create a Kerberos Server object in our Domain Controller.(https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-passwordless-security-key-on-premises#create-a-kerberos-server-object)The PowerShell script uses Entra Connect Components.(Import-Module "C:\Program Files\Microsoft Azure Active Directory Connect\AzureADKerberos\AzureAdKerberos.psd1")  

But that isn't installed in my DC.Our Entra Connect is setup on another VM built for that purpose alone.My question is:Could I install Entra Connect on the DC just for the components or will Kerberos Object needs it running and configured?Alternatively, could I reference the location on another machine "\server\C..." or download the components needed from somewhere safe?Thanks in advance!
Fernando

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-30*

Hi Fernando B. Graca,

Thank you for posting on the Microsoft Community Forum.

From the description above, I understand that your question is about Entra.

Since there are no developers working with Entra on this forum. For quick and efficient handling of your problem, I recommend asking your question again in the Q&A forum, where a dedicated technician will give you a professional and efficient answer.

Here is the link to the Q&A forum.

Q&A - Microsoft Q&A

Click the "Ask a question" button at upper right corner to ask your question, and select "Entra " tag and other tags related to your productions.

I hope the above information is helpful.

If you have any questions or concerns, please feel free to let us know.

All the best

Neuvi Jiang
