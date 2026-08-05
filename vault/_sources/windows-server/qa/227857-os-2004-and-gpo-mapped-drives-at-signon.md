---
title: "OS 2004 and GPO mapped drives at signon"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/227857/os-2004-and-gpo-mapped-drives-at-signon
question_id: 227857
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# OS 2004 and GPO mapped drives at signon

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/227857/os-2004-and-gpo-mapped-drives-at-signon (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Has anyone figured out GPO settings on 2004 to get our preferred mapped drives to connect on sign-on/startup?  

We haven't gone to 2004 solely because users cannot see the two mapped drives that all users need when signing on.  

This GPO has worked in all other OS's up to 2004, so we are hanging on to 1909 because of this.  

Any help would be greatly appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-14*

I can give this a look. I am not an admin of GPO policy, but missing GPO's keep me from moving forward to new OS's.  

Is this info specific to 2004? Seems like all previous OS versions of 10 have GPO applied for mapped drives except for 2004.  

Just as a curiosity, I added an entry in the registry to enable SMB2 and on the LAN I could see the mapped drives, but on WIFI I could not. I'm also not a Network admin to know what entails getting that going. I'm wondering if there is anything I can do in my images to get the drives to map. I made half success by getting them mapped while on the LAN.  

Does SMB3 come into play for that?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-14*

Hi,    

Thanks for posting in Microsoft MECM Q&A forum.     

Please navigate to User Configuration -> Preferences -> Windows Settings -> Drive Mappings to set the mapping drive policy in your GPO. Here are some good articles for your reference:    

How To Map Network Drives With Group Policy (Complete Guide)    

Using Group Policy Preferences to Map Drives Based on Group Membership    

Please note: The links are not from Microsoft, just for your reference. Thanks for your time.    

Best regards,    

Simon    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
