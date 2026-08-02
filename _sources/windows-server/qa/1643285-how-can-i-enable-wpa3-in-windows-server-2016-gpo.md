---
title: "How can I enable WPA3 in Windows Server 2016 GPO?\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1643285/how-can-i-enable-wpa3-in-windows-server-2016-gpo
question_id: 1643285
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# How can I enable WPA3 in Windows Server 2016 GPO?"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1643285/how-can-i-enable-wpa3-in-windows-server-2016-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone,

I'm reaching out because I'm encountering some difficulties implementing WPA3 on our Windows Server 2016. I've been trying to find the option in Group Policy Objects (GPO), but so far, I haven't been successful.

I've already updated our ADMX, but unfortunately, it hasn't resolved the issue.

Does anyone have any suggestions or insights on what steps I could take to resolve this? Any help would be greatly appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-05*

Hello

I understand that you’re trying to implement WPA3 on your Windows Server 2016 using Group Policy Objects (GPO). Unfortunately, based on the information I found, it appears that WPA3 configuration via GPO is not currently supported on Windows Server 2016.

However, you can try the following two options:

Upgrade to a newer version of Windows Server: It seems that the ability to create WPA3 settings via GPO is available in Windows Server 2022. However, even in this case, some users have reported issues when trying to view the GP report in the Group Policy Management Console.

Manual Configuration on Client Devices: If upgrading the server is not an option, you might consider manually configuring WPA3 on the client devices. For example, on Windows 10 devices, you can check if they support WPA3-Personal by running the command netsh wlan show drivers in the Command Prompt.
