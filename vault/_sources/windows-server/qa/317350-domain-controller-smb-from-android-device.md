---
title: "Domain controller smb from android device"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/317350/domain-controller-smb-from-android-device
question_id: 317350
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Domain controller smb from android device

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/317350/domain-controller-smb-from-android-device (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi, I have windows server 2019 essentials installed with domain controller, i want to access my smb shares from my android device. I can log on and read the files, but i can't edit and upload files. (it does create a file of 0kb) I tried multiple android apps with smv v2/3 but none of them work. I found a similar topic: https://social.technet.microsoft.com/Forums/office/en-US/5e75841b-cceb-459a-8d6e-ca8c46d72501/windows-server-2012-domain-controller-smb-file-share?forum=winserverfiles but no awnser was given here. kind regards, Marco

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-03-17*

Hi,    

Thanks for posting in Q&A platform.    

Before we go further, may I know if Windows client has encountered the same issue?    

Please check if the NTFS permission for Android user is including Read & execute, Read and Write read in the shared file's properties.    

    

And then please check if the Android user has read/write permission.    

    

If the user has these permission but still cannot write and upload file, I would suggest you follow DSPatrick's suggest to enable some auditing to capture more for further troubleshooting.    

Best Regards,    

Sunny    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-03-17*

You may need to enable some auditing to capture more.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/apply-a-basic-audit-policy-on-a-file-or-folder    

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-17*

Thank you for your reply's.  

I enabled the auditing but see no extra logs.  

But i narrowed the problem down.  

The server is at a remote location, today i was at that location and connected directly to the network wifi i can upload files.  

For remote connection i use openvpn connection to the main router.  

So the problem is something with the VPN connection.  

I use a similar setup at a different location and there it does work trough VPN.  

So now i have to find out why upload to smb is blocked by VPN, does anybody have An Idea?  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-16*

I checked the Samba server log, but there are no logs.  

Are there others logs where i can look at?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-16*

Might check the event logs for clues.
