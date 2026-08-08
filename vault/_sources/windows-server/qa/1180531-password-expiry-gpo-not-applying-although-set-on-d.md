---
title: "Password Expiry GPO not applying, although set on Default Domain Policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1180531/password-expiry-gpo-not-applying-although-set-on-d
question_id: 1180531
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
---
# Password Expiry GPO not applying, although set on Default Domain Policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1180531/password-expiry-gpo-not-applying-although-set-on-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

After spending some time trying to work out what the issue is, I decided to consult this Q&A forum, as I am at my wits' end.

I have configured a password expiry GPO on the Default Domain Policy, and set it to 'industry standard' in terms of max, min, password complexity, remember x passwords, etc... and this was following a few online guides pretty much saying the same thing. So, I know, as far as I know, what this GPO setting is good and should be working.

Even though the GPO is being applied (checked through gpresult /r and rsop) in terms of not being filtered out or denied, or not showing the settings on workstations, when doing a net user [username] /domain, it shows the user 's last password change but "password expires = never", when the GPO is set to expire after 90 days. 

A screenshot of the GPO:

I did this command:

Get-ADUser -filter {Enabled -eq $True -and PasswordNeverExpires -eq $False} –Properties "DisplayName", "msDS-UserPasswordExpiryTimeComputed" |  

Select-Object -Property "Displayname",@{Name="ExpiryDate";Expression={[datetime]::FromFileTime($_."msDS-UserPasswordExpiryTimeComputed")}}

I got results and everyone was showing as their password expiry as 01/01/1601, which, last time I checked, electricity had not yet been discovered!

As far as I know, the GPO is set up properly, in Default Domain Policy, the security filtering hasn't been touched, and the DDP is not being blocked/denied (as per gpresult /r result).

Have I missed something? I thought setting up a password policy was very easy...

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-16*

Hi,

Thank you for posting your query.

Kindly follow the steps provided below to resolve your query.

Make sure the GPO apply to the computers. To make sure just check inside your 2019 DC in the GPO's console do a report and target a remote computer to see if the setting is there.

It can happen if you changed the GPO value some time ago, but your user are on the field with older set of applying's GPO in example.

I would add if a test was done to expire the user password and the GPO was reverted back, it would not stop a user to be forced to reset his password if he got that GPO settings on his computer (or on a terminal server in example too)

Go to this link for your reference and additional troubleshooting procedures https://learn.microsoft.com/en-us/answers/questions/1025544/users-passwords-expire-even-though-gpo-set-to-neve

If the answer is helpful kindly click "ACCEPT AS ANSWER" and up vote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-15*

Hi JS

The value is: 512 UF_NORMAL_ACCOUNT

I know the password was changed, by the user (actually, the user is me using a test user account) as I made sure it did, thinking it might kick in and start the countdown clock. However, that didn't seem to do the trick. I can try again.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-02-14*

Anthony what is the value of Password last set attribute in AD? If it is never changed or set it will show the year 1601 I believe it is standard value. 

Check this https://learn.microsoft.com/en-us/windows/win32/adschema/a-pwdlastset

Hope this helps.

JS

==

Please accept as answer and do a Thumbs-up to upvote this response if you are satisfied with the community help. Your upvote will be beneficial for the community users facing similar issues.
