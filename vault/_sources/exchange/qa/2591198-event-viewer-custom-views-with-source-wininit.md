---
title: "Event Viewer custom views with source Wininit"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2591198/event-viewer-custom-views-with-source-wininit
question_id: 2591198
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# Event Viewer custom views with source Wininit

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2591198/event-viewer-custom-views-with-source-wininit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Microsoft experts.

After trying to create a custom view in event viewer, one with source "Wininit", in order to capture all relative events, I noticed that even though the view is successfully created, it does not bring any results (i.e. it is empty) (OS Windows 7 64bit
 with SP1). Thinking that indeed the application log is not registering Wininit events, I tried adding a custom filter in the "Application" category with events with source "Wininit". The latter brings multiple results (information mainly, and one warning,
 I think)). So events with source "Wininit" are registered in the "Application" category

How do you think should I proceed from now on, in order to troubleshoot further? I checked system files with sfc /scannow to no avail. Also I found out that when I change the custom view to another source, for example "Winlogon", results are seen under
 the view, with the selected source - "Winlogon" now, so it works as it should.

Last but not least, I navigated to my registry key (HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\eventlog\Application\Wininit) and saw the differences between the two (HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\eventlog\Application\Wininit,
 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\eventlog\Application\Winlogon) without any ideas whatsoever on how to proceed.

I then supposed it might be a rights issue. So, I checked the security settings under the two registry branches and they are the same.

Now I am out of ideas, and searching the internet does not help at all.

Please indicate something, because reinstalling Windows is not an option. Also I checked this custom view (with source Wininit) in some other (friends') Windows 7 pcs, and it is working perfectly. What is possible wrong in my case?

Thanks in advance.

## Answers

_No answers on this thread._
