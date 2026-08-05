---
title: "Windows Laps password can be viewed by all users with Active Directory Users and Computers."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188982/windows-laps-password-can-be-viewed-by-all-users-w
question_id: 2188982
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Windows Laps password can be viewed by all users with Active Directory Users and Computers.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188982/windows-laps-password-can-be-viewed-by-all-users-w (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am testing Windows Laps to Implemented it in our environment in Active Directory and not using intune. I created a test OU, Disabled inheritance and Setup GPO. I have created two Groups one to view only and one that can reset the password. I have set the permissions on the test OU for these two groups. However I have found that any Tech that is not in one of those groups can still view the password for Windows Laps. I have verified Extended rights and do not see anything that would allow any to see the passwords.

Also I know only one user/group and encrypt and decrypt the password for laps. I tried creating a group and adding the two other groups to the decryption group which did not work. Any possible way to have more than one group decrypt the password?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-21*

Hi Neuvi,

I deleted the previous OU and testing a new OU. I pointed the GPO to the new OU and ran Set-LapsADComputerSelfPermission to the new OU. I have yet to give read and reset permissions to the OU and still can view the password. 

The confusing part is the policy settings are applying to the computer ie resetting after 1 day, complexity and length. I checked in registry on the local computer and the registry is set as well.  However when I run gpresult on the computers the gpo is not showing being applied. 

I assume the policy should appear in gpresults?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-21*

Hi Michael_542,

Thank you for posting in the Microsoft Community Forums.

Although you mentioned disabling inheritance, I would recommend checking OU inheritance and permissions.

Verify that the GPO settings are correctly applied to the target machine. You can use gpresult /r or gpresult /h gpresult.html to check if the policy is applied correctly.

Ensure that the administrative template (ADMX file) for LAPS is configured correctly and that there are no conflicting configurations in the policy settings.

Recheck the Extended Rights to make sure that only the group you specified has Read Password and Reset Password permissions. Using the ADSI Edit utility, navigate to the target OU, right-click Properties, view the Security tab, select Advanced and check Effective Access. Access” to see if any unexpected users have permissions.

For the issue of decrypting password groups, by default, LAPS is designed to allow only one user or group to encrypt and decrypt passwords.

Best regards

Neuvi Jiang
