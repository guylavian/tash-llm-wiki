---
title: "Setting up GPO for proxy settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1263144/setting-up-gpo-for-proxy-settings
question_id: 1263144
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Setting up GPO for proxy settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1263144/setting-up-gpo-for-proxy-settings (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to setup a GPO to only allow chosen users to be able to access only one website. On windows server 2019 I opened up the GPE created a new policy under my User OU and navigated to User Configuration > Preferences > Control Panel Settings > Internet Settings. Right-click and select New > Internet Explorer 10 and setup my proxy with 127.0.0.1 with port 80. I then added the only website I want users to access into the Exception list. I then added my user account into the scope However this did not work for me after running a gpupdate and testing after I logged in. 

As a note my server is Windows 2019 and the Workstations are Windows 11. I noticed the GPO path I used above on server 2019 is not found in the GPE path on the local machine itself so not sure how thats supposed to work if both paths dont match up. Any help with what I'm doing wrong would be appreciated

## Answers

_No answers on this thread._
