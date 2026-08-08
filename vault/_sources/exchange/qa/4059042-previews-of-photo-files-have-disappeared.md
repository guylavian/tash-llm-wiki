---
title: "Previews of photo files have disappeared."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4059042/previews-of-photo-files-have-disappeared
question_id: 4059042
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 5
qa_tags: []
---
# Previews of photo files have disappeared.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4059042/previews-of-photo-files-have-disappeared (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Microsoft file manager used to show a miniature preview of individual photo file.  Now I've lost that feature.  I have to scroll thru all the photos in a folder to find the one I want.  All I see is an icon with different shades of blue.  There appears to be a white moon also.  Maybe a stylized mountain rising from the bottom border.  Can I get my file preview back so can easily navigate and select the photo I want?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-21*

Hello, GaroldGarber

Welcome to Microsoft Community.

There are a few potential solutions to restore the file preview feature in Microsoft file manager: 

-  Clear Thumbnail Cache: Windows uses thumbnail images to display previews of pictures. If the thumbnail cache is corrupted, it may prevent pictures from appearing in the browse files window. You can try rebuilding the thumbnail cache by following these steps:

a. Press Win + E to open File Explorer.

b. Click on the "View" tab at the top of the window.

c. In the "Show/hide" section, check the box for "Hidden items."

d. Navigate to the following folder: C:\Users\YourUsername\AppData\Local\Microsoft\Windows\Explorer (replace "YourUsername" with your actual username).

e. Delete all files with the prefix "thumbcache" (e.g., thumbcache_32.db, thumbcache_96.db, etc.).

f. Restart your computer and try browsing for new pictures again.

-  Change Folder Options: In File Explorer, go to the "View" tab and click on "Options" and then "Change folder and search options." Under the "View" tab, make sure that the option for "Always show icons, never thumbnails" is unchecked. 

-  Update Graphics Drivers: Sometimes, the issue may be related to outdated or corrupted graphics drivers. Try updating your graphics drivers from the manufacturer's official website to see if it resolves the problem. 

-  Perform a system file check (How to Use System File Checker in Windows - Microsoft Support) to ensure that your Windows installation is not corrupted.

Yuhao Li

Microsoft Community Technical Support
