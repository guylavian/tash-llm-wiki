---
title: "No picture previews with OneDrive on Server 2019 with files on demand"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166123/no-picture-previews-with-onedrive-on-server-2019-w
question_id: 1166123
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-onedrive-business-platform-windows", "windows-business-windows-server-user-experience-user-experience-other"]
---
# No picture previews with OneDrive on Server 2019 with files on demand

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166123/no-picture-previews-with-onedrive-on-server-2019-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

Customer has a Citrix environment, Windows Server 2019 with OneDrive for Business, version 23.007.0109.0004 which is the latest at the time of writing. Environment is fully patched.  

For some reason, pictures in the OneDrive folder don't show the thumbnail/preview in Windows Explorer. I tried with Windows Photo viewer, MS Paint and Microsoft Photos as default app.

Now, when I disable files on demand, suddenly the preview shows and the thumbnail works. But this is not an option as it would require every user to fully download their OneDrive folder into their FSLogix profile.

When I enable files on demand, and choose 'Always keep on this device' for a certain picture folder, it still doesn't work. No thumbnail preview is being shown.

I checked with another customer, who is also on Server 2019 and for some reason it works there with files on demand enabled and Microsoft Photos as picture app. I also checked my W10 laptop, which also has files on demand enabled and it works there as well, even if the pictures are not downloaded yet.

I then installed an empty 2019 machine with no GPOs and just OneDrive on it. No go, no picture previews.

Any idea how to fix this? Or is this by design?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-02-03*

Well I did a new built with OneDrive 23.007.0109.0004 and suddenly it works now. With fod enabled and the file not even downloaded already shows the preview. I think it might have been a OneDrive bug because indeed it worked in folders outside of OneDrive, but unfortunately there are no release notes so I can't tell for sure.

Anyway, this is solved. Thanks for the help!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Double post

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hi,

Thank you for posting your query.

Kindly follow the steps provided below to resolve your issue.

OneDrive Files On-Demand helps you access all the files in your cloud storage in OneDrive without having to download them and use storage space on your computer.

When you turn on Files On-Demand, you’ll still see all your files as online-only files in File Explorer, but they won't take up space. When you’re connected to the Internet, you’ll be able to use the files like every other file on your device.

You can also select files and folders to be always available, even if you're offline. OneDrive will download them, and they'll take up space on your PC.

Go to this link for your reference and other troubleshooting procedures https://support.microsoft.com/en-us/office/save-disk-space-with-onedrive-files-on-demand-for-windows-0e6860d3-d9f3-4971-b321-7092438fb38e

Do not hesitate to message us if you need further assistance.

If the answer is helpful kindly click "Accept as Answer" and up vote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-02*

Hi @Martijn Kools

Thanks for your sharing.

By the way, since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others.", and according to the scenario introduced here: Answering your own questions on Microsoft Q&A, I would make a brief summary of this thread:

Issue Symptom:

No picture previews with OneDrive on Server 2019 with files on demand, enabling 'Always keep on this device', it still doesn't work.

Solution via Martijn Kools:

Try to update OneDrive to a new built with version 23.007.0109.0004

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
