---
title: "Error deploying GPO using AGPM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1620201/error-deploying-gpo-using-agpm
question_id: 1620201
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Error deploying GPO using AGPM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1620201/error-deploying-gpo-using-agpm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We encountered an error attempting to deploy a GPO via AGPM, with the following message:

```
Deploy GPO failed
The overall error was: The process cannot access the file because is being used by another process. Excption from HRESULT: 0x80070020
```

Could someone offer advice or recommendations?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-19*

Hi @Yanhong Liu  

Thank you for your answer but we still have the same issue. Any other suggestion ?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-18*

Hello Richard Y ,

Thank you for posting on the Microsoft Community Forum.

-  According to your error message prompt, you can try to restart the AGPM service. Sometimes, all you need to do is restart the AGPM service to fix the file locking issue. To do this, you can open the service console (services.msc), find the AGPM service, and click Restart.

-  Check if there are other users editing the GPO: Check the status of the GPO in the AGPM console and confirm that no other administrator is editing or checking out the GPO. The steps are as follows:

Open the Microsoft Advanced Group Policy Management (AGPM) console.

In the console tree, navigate to the forest and domain you're in, and then typically under the Change Control node.

Expand the Controlled GPOs folder or go directly to the specific GPO you want to check.

Look at the list of GPOs and there will be a status indication next to each GPO. If a GPO is checked out, its status will usually be displayed as "Checked Out" with the name of the user who checked out the GPO next to it.

Double-clicking on the GPO to be checked will open the properties window for that GPO. From here, you can view detailed checkout information in the General or Checkout tab, including the user account that checked out the GPO, the checkout time, and the checkout status.

If you find that another user has checked out the GPO, you will need to contact that user to check in or abandon the checkout so that you can make the required edits or deployments.

-  At the same time, you can also check the AGPM service port, by default, the AGPM service uses port 4600. Make sure that the port is not occupied by other applications.

I hope you the information above is helpful.

If you have any questions or concerns, please do not hesitate to let us know.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-16*

It seems that the error message you received indicates that the GPO file is being accessed by another process and the AGPM deployment process cannot access it. This issue occurs when the wizard in GPMC or the Import-GPO cmdlet tries to acquire an exclusive handle to some file of the GPO in the SYSVOL share, but that file is being accessed by another process. To resolve this issue, you can try specifying a different target domain controller (DC) with no or little user access. By default, the target DC used by GPMC or the Import-GPO cmdlet is the primary domain controller (PDC) Flexible Single Master Operation (FSMO) role of the domain. This behavior is by design. You can also check if the AGPM Service is running and start it if it is not.

References:

-  GPMC or Import-GPO cmdlet fails to restore a GPO from backup

-  Troubleshooting AGPM

-  Deploy a GPO
