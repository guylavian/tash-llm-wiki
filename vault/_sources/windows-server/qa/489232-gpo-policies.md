---
title: "GPO Policies"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/489232/gpo-policies
question_id: 489232
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO Policies

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/489232/gpo-policies (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I hope someone is able to help.  

I am in the process of attempting to give a user USB access to devices on his personal Domain Laptop and have been asked to create a GPO.  

The GPO has been created and I have Disabled the System/Removable Storage Access option, linked to the correct OU and created a Security Group and added the user.   

I now the user is picking up the GPO as I have run a gpresult on his machine and it is being applied. However, he still has no access to the USB.   

I noticed there was another GPO which denies ALL Domain users access to any external storage device including USB. So I moved the newly created GPO above the GPO which denies ALL Domain users. Asked the user to do a gpupdate /force but he still does not have USB access.  

My question -   

-  Is there a way of finding out which policy is acutally overruling the policy I have created?  

-  Is there a way of finding out if the Policies inside a GPO are actually getting applied?  

Any help would be greatly appreciated.  

Regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-05*

Hi Hannah xiong,    

The user still seems to be getting the issue. I believe its to do with possibly the GPO policies timings.    

P.S.B.    

that is the order the user is picking up the GPO. In this instance what is taking precedence?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-26*

@Anonymous      

Thanks for this information there are some things I was not aware of and need to check up on.    

Once again this has answered my question and thanks very much for taking the time out to post.    

Regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-26*

Hello @czql5v  ，    

Thank you so much for posting here.    

According to our description, we configured the policy under User Configuration\Administrative Templates\System\Removable Storage Access. The policy "All Removable Storage classes: Deny all access" determines access to all removable storage classes.    

If we enable this policy setting, no access is allowed to any removable storage class.    

If we disable or do not configure this policy setting, write and read accesses are allowed to all removable storage classes.    

Since we disabled this policy, user should be able to access USB. But actually the user has no access to the USB.     

As stated, we checked the gpresult and the policy is being applied.     

Since there was another GPO which will deny all domain users to USB. To quick testing, we could disable this GPO by clicking Link Enabled so that the link is disabled.     

Normal state with Link Enabled:    

    

Link disabled:    

    

We could diable the link of this GPO and then do a gpupdate /force to see whether the user could have USB access.     

As for our questions,      

-  We could run gpresult /h to get the gpresult report. We could tell from the report which policy actually takes effect and gets applied.     

In general, the order in which Group Policy applies GPOs determines precedence. The order is site, domain, OU, and child OUs. As a result, GPOs in child OUs have a higher precedence than GPOs linked to parent OUs, which have a higher precedence than GPOs linked to the domain, which have a higher precedence than GPOs linked to the site.     

-  We could also check from the gpresult report that if policies inside a GPO are applied or not. For example, for user configuration, we could check the user details and then check the configured settings. Please also check the applied GPO lists as well.    

    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
