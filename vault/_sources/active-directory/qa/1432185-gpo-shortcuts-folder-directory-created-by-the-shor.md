---
title: "GPO - Shortcuts - Folder/Directory created by the Shortcut Functionality can't be deleted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1432185/gpo-shortcuts-folder-directory-created-by-the-shor
question_id: 1432185
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# GPO - Shortcuts - Folder/Directory created by the Shortcut Functionality can't be deleted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1432185/gpo-shortcuts-folder-directory-created-by-the-shor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Brothers and Sisters,

I trust this message finds you well.

I have created a shortcut with the following details:

The shortcut is an Edge link that opens a production web app.

The shortcut is located in a folder/directory that was automatically created by the Shortcut functionality.

-  Action: Replace

-  Name: SPM_4.26_TEST\SPM_Web_4.26_TEST_EDGE

-  Target Type: File System Object

-  Location: Desktop

-  Target Path: C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe

-  Arguments: http://10.9.88.240/WebServiceOptimPM/WebClientProtocolLabelPrinting.aspx

-  Start in: C:\Program Files (x86)\Microsoft\Edge\Application

This shortcut worked properly for about a year; however, the business no longer needs it. Therefore, I have used a delete action. The shortcut (SPM_Web_4.26_TEST_EDGE) is deleted, but the folder (SPM_4.26_TEST) is not. I have tried to delete it manually (test), but it always reappears on the desktop. I created a new GPO with a new testing user account, ensuring that there is no other GPO or setting creating the folder/directory.

Please find more information below:

1st Shortcut to Delete "SPM_Web_4.26_TEST_EDGE":

-  Action: Delete

-  Name: SPM_4.26_TEST\SPM_Web_4.26_TEST_EDGE

-  Target Type: File System Object

-  Location: Desktop

The shortcut (SPM_Web_4.26_TEST_EDGE) is deleted, but the folder (SPM_4.26_TEST) remains on the desktop.

I then created a 2nd shortcut to try to delete the folder on the desktop:

2nd Shortcut to Delete "SPM_4.26_TEST":

-  Action: Delete

-  Name: SPM_4.26_TEST

-  Target Type: File System Object

-  Location: Desktop

However, the folder "SPM_4.26_TEST" persists and cannot be deleted.

Can someone help me, please? Your assistance is greatly appreciated.

Thank you very much for all your help and support.

Peace

## Answers

_No answers on this thread._
