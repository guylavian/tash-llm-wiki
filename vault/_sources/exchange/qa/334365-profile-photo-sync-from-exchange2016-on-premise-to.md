---
title: "Profile Photo Sync from Exchange2016 on Premise to O365 Environment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/334365/profile-photo-sync-from-exchange2016-on-premise-to
question_id: 334365
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-teams-teams-business-other-l1", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Profile Photo Sync from Exchange2016 on Premise to O365 Environment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/334365/profile-photo-sync-from-exchange2016-on-premise-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,  

A moderator from answers.microsoft.com advised that I post my question here.  

Original Question:  

https://answers.microsoft.com/en-us/msoffice/forum/all/profile-photo-sync-from-exchange2016-on-premise-to/c25287b2-a41f-47cd-9e99-4b3c0294fc9e  

I hope someone can help me with the profile photo sync.  

The blog posts are either 5 years old or all about uploading to O365 Exchange.  

Which we are currently not using.  

Currently only some profile pictures are kept in AD (for CTI and Outlook).  

These pictures should of course also appear in Teams.  

The thumbnail resolution is sufficient for CTI and the local office applications.   

The resolution in Teams is unfortunately not good.  

For testing purposes, I uploaded a set-user photo with 648x648 pixels on our on-prem Exchange 2016 and waited for synchronization.  

A thumbnail is created in the user's AD object.  

The synchronization to Office365 is solved via the AD Azure Connector.  

Result:  

-  In OWA, the full resolution is available.   

-  In CTI and Excel only the small one (which is quite sufficient).  

-  Sharepint - No profile picture.  

-  365 Admin Center - No profile picture.  

-  In Teams and Teams Admin Center the resolution is a disaster and not usable.  

A Get-AzureADUserThumbnailPhoto shows 64x64 pixels - so not the 648x648 as desired.  

I have already seen that in the Azure-AD Connector can prevent the thumbnailPhoto attribute from being transferred.  

All posts continue to describe that you can upload the images directly to Office365... however to Exchange Online - Which we do not use.  

Does anyone have any advice for me on how to get the high res images into the Office365 environment via script?  

Most important here is Teams for now, but of course it would be good if the images were identical in all Office 365 parts.  

Our environment looks like this:  

On-Premise:  

-  Exchange 2016  

-  AD  

-  Outlook 2010/O365  

-  Azure AD Connect with Sync to O365  

O365:  

So far only MS Teams and OneDrive  

Just before the rollout of MS Teams for all employees  

Thanks in advance!  

Daniel  

Translated with www.DeepL.com/Translator (free version)

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-28*

The dimension of the image (in pixels) isn't (from what I remember) as important as the size of the file.    

Have you read this? user-photos-not-synced-to-exchange-online    

Assuming you have the image files you should be able to create and import a PSSession and use the Set-UserPhoto cmdlet. There are probably size limitations on the size of the image file and those may differ between the the AD and the applications that use the photos.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-28*

Assuming you don't allow users to upload photos themselves (which, based on my experience, is a very bad idea -- some of the stuff that showed up in the AD made it look like a dating site, or worse!), this might be a model to use:  

-  Get all user account IDs and ThumbNailPhoto data from the AD and create a directory (call it  "Today")  

-  Send the ThumbNailPhoto data to the AAD user  

-  In another directory (call it "Baseline"), create a file (name it with the user identity) that holds the hash value of the ThumbNailPhoto file.  

-  Tomorrow (or whatever you chose as a schedule), erase the data in the "Today" directory, and repeat step #1(but NOT step #2 and #3)  

-  For each user, generate a hash of today's ThumbNailPhoto and compare it to the hash for that user in the "Baseline" directory. If the hash is the same, do nothing. If the hash is different, move the ThumbNailPhoto to an "Update" directory. If the user isn't in your "Baseline" directory update the "Baseline" directory and add that ThumbNailPhoto to the "Update" directory.  

-  Send the ThumbNailPhotos in the "Update" directory to the AAD and then delete the contents of the "Update" directory.  

-  Repeat, starting at step #4.  

If you have multiple AD domains you'll have to do this for each one (unless the ThumbNailPhoto property is being stored in your Global Catalog). If all the Domain Controllers are local the update shouldn't be too hard to manage if you do it, say, once a week. If you have multiple domains and they're not local it would probably be a good idea to have the process run in each location to minimize network traffic.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-27*

Hello Andreas,  

thank you for the answer.  

I hope someone can shed some light on this totally incomprehensible profile picture issue.  

It would be totally helpful if you could choose one command for the whole O365 environment, apart from Exchange Online.  

Currently I feel that users have to manually upload the images. to Teams.  

:/  

PS:  

I don't really understand your last sentence... what do you mean?  

For me a profile picture is enough... but the resolution in Teams is really very bad.  

Translated with www.DeepL.com/Translator (free version)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-27*

Hello Andreas,  

thank you for the answer.  

I have already seen the article from petri.com, but there is a command used for Exchange Online, isn't it?  

We have all mailboxes on Exchange 2016 on Premise.  

Or am I misunderstanding something here?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-27*

Hi @Bölling, Daniel   ,    

maybe this is helpful (never tried this myself)?    

https://petri.com/update-user-photos-office-365-accounts    

----------    

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)    

Regards    

 Andreas Baumgarten
