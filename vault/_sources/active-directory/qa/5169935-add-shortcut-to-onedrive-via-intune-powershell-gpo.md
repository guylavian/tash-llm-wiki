---
title: "\"Add Shortcut to OneDrive\" via Intune / PowerShell / GPO etc"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5169935/add-shortcut-to-onedrive-via-intune-powershell-gpo
question_id: 5169935
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 47
qa_tags: []
---
# "Add Shortcut to OneDrive" via Intune / PowerShell / GPO etc

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5169935/add-shortcut-to-onedrive-via-intune-powershell-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I'm trying to migrate our company data from traditional shared drives, I'd like to be able to use the "add shortcut to OneDrive" in SharePoint document libraries to "map" each departments data into their OneDrive. Our users are particularly unskilled in IT as we a a large dairy and not part of their core skills. Is there a way to do this by policy via Intune, PowerShell or GPO? I can see a way to sync document libraries automatically, but we have very large document libraries and this is not practical, I'd much rather use the newer "Shortcut to OneDrive" method.

TIA

## Answer (community) — community member

*upvotes: 1 · updated: 2022-04-27*

Hi Daniel,

Thanks for posting in our community and I'm glad to support.

Based on the detailed description, we do understand you want to provide a better and more convenient way for users in your company to map SharePoint libraries to the local OneDrive side to access quickly. Feel free to correct me if I made any misunderstanding. And we'd like to share the following details and hope they can help in any way.

For the GPO in OneDrive, kindly check: Use OneDrive policies to control sync settings - OneDrive | Microsoft Docs

Third-party article: OneDrive | GPO: Configure team site libraries to sync automatically – Hans Brender's Blog

Meanwhile, with the help of MS Endpoint Configuration Manager during the deploying OneDrive process

Deploy OneDrive apps using Microsoft Endpoint Configuration Manager - OneDrive | Microsoft Docs

Hope the above information can offer a bit help or insights for your scenario. But I'm really sorry to convey as engineers in this community focus on support OneDrive product for end users. We do have limited experience and support resources about the admin deployment. It is sincerely suggested to post threads in the escalated communities below. Professional engineers and experts there will offer you a better user experience for IT pro/OneDrive development related scenarios.

Microsoft Q&A - search OneDrive GPO results (you can refer to the related tags to better post your own thread)

sample thread: GPO settings for OneDrive and Sharepoint Document Library - Microsoft Q&A

Microsoft Tech Community- OneDrive for Business 

sample thread: OneDrive - Configure team site libraries to sync automatically - Microsoft Tech Community

Your kind understanding are highly appreciated. Hope you a nice day!!

Best Regards,

Mia

Disclaimer: Microsoft provides no assurances and/or warranties, implied or otherwise, and is not responsible for the information you receive from the third-party linked sites or any support related to technology.
