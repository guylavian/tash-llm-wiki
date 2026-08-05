---
title: "Setting up GPO for proxy settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1263139/setting-up-gpo-for-proxy-settings
question_id: 1263139
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Setting up GPO for proxy settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1263139/setting-up-gpo-for-proxy-settings (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to create a GPO in AD using Windows server 2019 so I can block all websites except for just one for my chosen users. I'm told that it can be done through creating a GPO to edit the proxy settings. I created a policy in GPE on my user OU by going to User Configuration > Preferences > Control Panel Settings > Internet Settings. Right-click and select New > Internet Explorer 10. I then setup my proxy as 127.0.0.1 with port 80. I then added the only website I want the users to access in the exceptions list. However this did not work after testing a login. But if I manually open the proxy settings on the machine itself and setup the proxy through the GUI then it works.

As note I am using server 2019 and most of our Workstations are Windows 11. I noticed that the GPO path above that I am using to create my GPO on the domain is not found on the local Gpedit.msc on the machine thats using Windows 11 so I'm not sure if this is going to work. So far I have been unsuccessful. Any thoughts on how I can get this to work?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-28*

Hello

Thank you for your question and reaching out.

-  Would first suggest you to download and update latest ADMX GPO files supported for Windows 11 on your AD server.

https://www.microsoft.com/en-us/download/104593

https://www.microsoft.com/en-us/download/details.aspx?id=103506

-  After applying it rung gpresult /h C:\tempt\gpresult.html   to verify it gets applied.

--If the reply is helpful, please Upvote and Accept as answer--
