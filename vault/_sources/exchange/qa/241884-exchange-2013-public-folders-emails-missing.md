---
title: "Exchange 2013 Public Folders - emails missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/241884/exchange-2013-public-folders-emails-missing
question_id: 241884
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2013 Public Folders - emails missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/241884/exchange-2013-public-folders-emails-missing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My office saves project associated emails from all our staff in separate subfolders under the Public Folders of Exchange for each project.  Staff generally will keep the emails in their personal Inbox and occasionally move a bunch of the emails to the associated Public Folder subfolder.  It was brought to my attension that when one of the staff moved their emails from their inbox to the public folder that the emails disappeared in the public folder.  They saw the system process the move (it took a little time) but when they went to the public folder the folder was empty.  I checked other folders and the ones I checked have lost some of their older emails.  You would think it is file retention but I have checked all of the public folder settings.  Everything is set to unlimited storage and never delete.  We have been doing this for many years with no issues of old emails in project folders.  I don't know what has changed.  I am not an IT person.  Architect by trade but know enough to get myself in trouble.  Any assistance on what to check and how to get these missing emails back would be greatly appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-25*

Just to confirm the age limit and deleted item retention, run the following command in EMS:    

```
Get-publicfolder \pfolder1|fl *age*,*deleted*  
Get-Organizationconfig |fl *DefaultPublicFolderAgeLimit*,*DefaultPublicFolderMovedItemRetention*
```

Does the issue occur with all users or one specific user, all folders or one folder? Can he re-produce the issue?    

Do a test with the problematic folder/user, after he moving the items, stop any users moving items into/out the folder, check the the issue happen again, and run the following command to check the LastModificationTime value:    

```
Get-PublicFolderItemStatistics -Identity "\Marketing\2010\Pamphlets" | Format-List
```

To recover the items, try the "recover deleted items" in Outlook, if it's missing, follow the KB and have a try:    

    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-22*

Are you sure you Checked the aging limits on those specific folders? If the items are expired and deleted, you can't recover them.    

You may have something specific set    

If the user actually saw the messages being moved, I have never heard of that. If the aging limits are not the issue, then someone may have actually moved the items manually or you arent getting the full story here.
