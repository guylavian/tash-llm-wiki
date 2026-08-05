---
title: "O365 EWS w/ Impersonation UploadItems worked March 2024 - now 'access denied' error.  All other features work."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1657244/o365-ews-w-impersonation-uploaditems-worked-march
question_id: 1657244
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# O365 EWS w/ Impersonation UploadItems worked March 2024 - now 'access denied' error.  All other features work.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1657244/o365-ews-w-impersonation-uploaditems-worked-march (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I spent quite a few weeks earlier this year writing a PowerShell utility to copy mail between users in a O365 Tenant (including the ability to place copied mail in a unique 'root' folder tree).  After much trial and error I had a working script that did what I needed.  I use a mix of EWS and EWS managed API calls, I've resolved token (refresh), service, impersonation and Application API access issues.   Last used successfully 3/19/24.

The following week or 10 days later I revisited the code and found that all the features were still functioning - except UploadItems.  The response from that is now:  Access is denied. Check credentials and try again., The process failed to get the correct properties.

I tested my code against 4 of the Tenants I manage and found the same error for all of them.  They had all worked previously.   I've tested my Impersonation 'credentials' (tenantID, clientID, clientsecret) using EWSEditor - no issues.  I've spent the last 3 weeks going over everything - script and tenants - I'm not getting anywhere.   It feels like Microsoft changed something and didn't tell anyone.

Code snippets available upon request.  I didn't post the code because I'm not get any code failures - I just can't UploadItems to the target mailbox.

Your help greatly appreciated.  But I would also appreciate if you wouldn't reply with how-to links - this WAS working, I just need to know what changed and how to code for it.

Regards,

jbw

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-14*

Update:  I've discovered that when I change the SOAP Attribute "CreateAction" to "CreateNew" vs **UpdateOrCreate **(or Update) the UploadItems request is successful.  Now what I'm trying to understand is why the UpdateOrCreate and Update create actions are failing - the only difference is the latter action uses the passed Item Id and ChangeKey.  This code WORKED prior prior to March 2024 with UpdateOrCreate as the create action (CreateNew ignores the supplied Item Id and ChangeKey).

`$child = ($soapRequestXML.CreateElement("t:Item", "http://schemas.microsoft.com/exchange/services/2006/types"))`

`$child.SetAttribute("CreateAction", "CreateNew")`

`($soapRequestXML.SelectSingleNode("//m:Items", $nsmgr).AppendChild($child)) | Out-Null`

`$child = ($soapRequestXML.CreateElement("t:ParentFolderId", "http://schemas.microsoft.com/exchange/services/2006/types"))`

`$child.SetAttribute("Id", $DestFolder.Id.UniqueId)`

`$child.SetAttribute("ChangeKey", $DestFolder.Id.ChangeKey)`

`($soapRequestXML.SelectSingleNode("//t:Item[$i]", $nsmgr).AppendChild($child)) | Out-Null`

`$child = ($soapRequestXML.CreateElement("t:ItemId", "http://schemas.microsoft.com/exchange/services/2006/types"))`

`$child.SetAttribute("Id", $node.ItemId.Id)`

`$child.SetAttribute("ChangeKey", $node.ItemId.ChangeKey)`

`($soapRequestXML.SelectSingleNode("//t:Item[$i]", $nsmgr).AppendChild($child)) | Out-Null`

`$child = ($soapRequestXML.CreateElement("t:Data", "http://schemas.microsoft.com/exchange/services/2006/types"))`

`$child.InnerText = $node.Data`

`($soapRequestXML.SelectSingleNode("//t:Item[$i]", $nsmgr).AppendChild($child)) | Out-Null`

I'd love to get this resolved.   Usable in the current form, but I can see re-runs could be problematic.

Your help appreciated

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-18*

Vasil -

This is a registered App.  I'm already using "full_access_as_app" permissions and a Bearer token to authenticate the mailbox service.  I can create folders in the destination mailbox, find and read source and destination items, but the response on UploadItems is always 'access denied'.  This was working 4-5 weeks ago.  I've read the article referenced previously, but I'm not using a user account for authentication (and I tried assigning ApplicationImpersonation role to the app - but it didn't fix anything). 

Regards,

jbw

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-04-18*

Are you using the role? Microsoft is in the process of deprecating this: https://techcommunity.microsoft.com/t5/exchange-team-blog/retirement-of-rbac-application-impersonation-in-exchange-online/bc-p/4063002#M37971

Though as mentioned in the article, this should only happen starting from May, and should not affect existing assignments. Best open a support case to verify, or comment on the article above where the PM is fairly active.
