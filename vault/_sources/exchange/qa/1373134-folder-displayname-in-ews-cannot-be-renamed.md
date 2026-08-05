---
title: "Folder DisplayName in EWS cannot be renamed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1373134/folder-displayname-in-ews-cannot-be-renamed
question_id: 1373134
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Folder DisplayName in EWS cannot be renamed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1373134/folder-displayname-in-ews-cannot-be-renamed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi! When I was browsing my EWS folders with EWSEditor, I found some of my folders' names are in wrong language, and they cannot be renamed or deleted.

The folders I wanted to rename were the following:

-  Reminders (提醒): used for storing reminders set from within EWS calendar events;

-  People I Know (我认识的人): actual use unknown but there is an identical folder named in the correct language coexist in EWS directory

-  Top of information store ➡️ Yammer Root ➡️

-  Inbound (传入)

-  Outbound (传出)

-  Feeds (源)

- 

```
-  which seem to be used by Yammer
```

```
These folders seem to have a property Distinguished folder which prevents them from being renamed or deleted. Is there a way to force rename (change display name value) or to recreate such folders and relate them to there uses? 

      Thanks in advance!

      ![2d49b78b-9aae-4428-847f-47dc23075b16](/api/attachments/916e84b7-770a-491f-9261-ac0fa2c6e422?platform=QnA)
```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-20*

Hi @Holger Huo  ,

Thanks for posting in our Q&A forum.

From your description I understand that you are having trouble renaming or deleting some of your folders in EWS. If there are any misunderstanding, feel free to let us know.

There are a few ways to rename a folder in EWS. One way is to use the Ews.RenameFolder method. 

Another way is to use the UpdateFolder operation. You can use this operation to rename a folder by using the FolderType object and setting the DisplayName property to the new name.

In this case, you can try creating new folders with the correct names and relating them to their uses. To create a single folder, you can send a CreateFolder operation request message. The CreateFolder operation request indicates that the parent folder is the Inbox, the DisplayName is “Custom Folder”, and the FolderClass element value is IPF.Note.

Please refer to this blog: https://www.rebex.net/secure-mail.net/features/ews-folders.aspx#rename

Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
