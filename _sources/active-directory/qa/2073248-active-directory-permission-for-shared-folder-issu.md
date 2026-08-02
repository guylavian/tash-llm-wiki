---
title: "Active Directory permission for shared folder issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2073248/active-directory-permission-for-shared-folder-issu
question_id: 2073248
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory permission for shared folder issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2073248/active-directory-permission-for-shared-folder-issu (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I am trying to make the permission so that the user cannot delete the Parent folder, but can delete all folders and files inside.

If I set the permission to Folder1 folder to "this folder, subfolders and files", and then give them full control but un-tick delete, it doesn't work- user is still able to delete parent folder (Folder1).

How can I set set such permissions?

Thank you in advance.

I've uploaded video of setting this permission so you can see what I've done: https://www.dropbox.com/scl/fi/3o02rccc6jkcnndnq697x/Shared-folder-permission-setting.mp4?rlkey=0mtdvqzmtwkge8kdsyi5fuahf&st=do6zrae6&dl=0

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-21*

Hello Vasileios,

I've set up the permissions exactly like you said, but I'm still able to delete Parent folder.

Here is a new video how I set up the permissions: https://www.dropbox.com/scl/fi/a23msg880o78wkpfx92ca/Permission-setting_21.9.24.mp4?rlkey=20bxag2svimthg1ycyky9jzxs&st=uqic5bv0&dl=0

Thank you in advance.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-20*

Hello

Thank you for posting in Q&A forum.

At the permission page, you can apply it to ' Subfolders and files only ' instead ' this folder, subfolders and files '

or user will have permission for this folder.

Best regards

Yanhong

=====================================

If the answer is helpful, please click "Accept answer" and upvote it

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-09-19*

Hello Vojta,

To achieve the goal where a user can delete the contents (files and subfolders) of a parent folder but cannot delete the parent folder itself, you'll need to modify the NTFS permissions carefully. Here's a detailed step-by-step guide to configuring the permissions correctly:

-  Set Permissions on the Parent Folder (Folder1)

The goal is to allow users to modify and delete items inside the parent folder, but not delete the parent folder itself. Follow these steps:

a. Right-click the Parent Folder (Folder1) and select Properties.

b. Navigate to the Security tab and click on Advanced.

c. Click on Disable inheritance and choose Convert inherited permissions into explicit permissions (this ensures you're working with explicit permissions only).

d. Under the Permissions Entries, click on Add to create a new rule for the user or group you want to set the permissions for.

e. In the new permissions dialog:

-  Choose the appropriate user or group.

-  Set the Type to Allow.

-  In the Applies to dropdown, select This folder only.

-  Check all the permissions except Delete and Delete Subfolders and Files.

This step ensures that the user cannot delete the parent folder (Folder1) but still has access to other folder operations.

-  Set Permissions for Subfolders and Files

To allow the user to modify and delete files and subfolders inside the parent folder:

a. Click Add again to create a second rule for the same user or group.

b. In the new permissions dialog:

-  Choose the appropriate user or group.

-  Set the Type to Allow.

-  In the Applies to dropdown, select Subfolders and files only.

-  Grant Full control.

This ensures that the user has full control over all the files and subfolders inside the parent folder, allowing them to delete everything inside but not the parent folder itself.

-  Test the Permissions

After setting the permissions:

-  Try deleting files and subfolders inside Folder1 to confirm the user can delete them.

-  Attempt to delete the parent folder (Folder1) itself. The user should get an "Access Denied" error, confirming they can't delete it.

Summary of Permissions:

Parent Folder (Folder1):

-  Allow all permissions except Delete and Delete Subfolders and Files for the user.

-  Applies to: This folder only.

      Subfolders and Files:

```
- Grant **Full Control** for the user.

   - Applies to: **Subfolders and files only**.
```

This setup should achieve the desired behavior where the user can manage all contents inside the folder, but cannot delete the parent folder itself.

I hope I help.
