---
title: "Active Directory Reset Password Over CMD Permissons"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199261/active-directory-reset-password-over-cmd-permisson
question_id: 2199261
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-user-logon-profiles"]
---
# Active Directory Reset Password Over CMD Permissons

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199261/active-directory-reset-password-over-cmd-permisson (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So here is my issue. I am running active directory and i need certain end users to be able to reset the password for users in the lets say EXAMPLE OU. So what i did was created a security group and delegated reset password permissions. However when i go to cmd and get users to run "Net user (username) (newpassword) /domain" it returns access denied 5. So i check permissions over and over again but no luck. Its only when i give the security group full permisson to edit properties of users in the OU it actually works. I need to know what permissions exactly will allow me to do this. My users must be able to usee the cmd command for our strange use case.  For obvious reasons i dont want to give them that permissions forever.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-13*

Hello Jake Cooper1,  

Thank you for your reply and update.  

The result of command "Net user /domain <username>" will show the information about the specific AD user account. Not sure if the two solutions apply to CMD reset password or not.  

However, I think you can test the solutions above in test lab, and after that check the result.  

Thanks for your time.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-12*

I saw this post could this be a fix?  

Hello all,  

I found a solution for this problem.  

The problem was placed directly is the registry of the domain controllers.  

There are 2 ways how you can solve it.

Solution 1: Create a policy which allows the specify groups or users to make a SAM request and link it to the whole domain OUs on the top level. So that all computers and users of all OUs gets it.

Here is the instruction for this policy setting:

Computer Configuration >> Windows Settings >> Security Settings >> Local Policies >> Security Options >> "Network access: Restrict clients allowed to make remote calls to SAM".

Select "Edit Security" to configure the "Security descriptor:".

Add the wished User or Group in "Group or user names:"

Select "Allow" for "Remote Access" in "Permissions for "Administrators".

Click "OK".

Make CMD: gpupdate /force on all domain computers and restart them.

Solution 2: Deleting existing policy or local registry settings for SAM request

-  Find the policy that specifies the SAM request (if already exists) and edit (allow the wished group or user) or delete it completely.

-  Open regedit.exe on all domain controllers at the same time and delete the registry key:

Registry Hive: HKEY_LOCAL_MACHINE  

Registry Path: \SYSTEM\CurrentControlSet\Control\Lsa\

Value Name: RestrictRemoteSAM

Value Type: REG_SZ  

Value: O:BAG:BAD:(A;;RC;;;BA)

-  Restart one of the domain contorllers and check if the registry key is still there. In general it should be completely removed and doesn't appear after reboot.

Info: This registry key restricts all normal users making a "net user /domain <username>" request.

-  Try the "net user /domain <username>" request as normal user (Make "gpupdate /force" and restart the computer running the request if needed)

BR,  

Yaroslav Kraus

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-12*

What the issue is we dont want the users having AD Users and computers installed so we ideally want to know what the permission is. Is there any set permissions for the net user command that it could happen to fall under?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-12*

Hello Jake Cooper1,  

Thank you for posting in Microsoft Community forum.  

In my test, if I delegate domain user (t2) to change password for other domain users.

1.I set it through "Delegation of Control Wizard" and check "Reset user passwords and force password change at next logon".  

  

2.I cannot check the option "User must change password at next logon" (the option is greyed out) when resetting password for domain users using t2 account.  

  

3.However, I can reset the password for domain users in the specific OU successfully using t2 via GUI (not CMD command).  

  

4.But when I reset password for domain users in specific OU using t2 via CMD command, it seems I get similar error message as you (below), am I right?  

![Image](https://learn-attachment.microsoft.com/api/attachments/6bac214d-7953-4a7b-afbe-a1c8140ce7d5?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/029e2b98-08ae-4b94-9bd5-6fd7bd67d52c?platform=QnA" title="filestore.community.support.microsoft.com" rel="ugc nofollow">  

It seems resetting password via CMD needs more permissions, currently, I cannot find what specific permissions for CMD (I have done test more than two hours).  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
