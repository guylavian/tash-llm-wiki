---
title: "Default Domain Controller Policy - Restricted Groups configured!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1120376/default-domain-controller-policy-restricted-groups
question_id: 1120376
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Default Domain Controller Policy - Restricted Groups configured!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1120376/default-domain-controller-policy-restricted-groups (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

I've recently inherited a, rather poorly maintained, Domain in which there are multiple (30+) domain groups added to the "restricted groups" Group Policy setting for the Default Domain Controllers Policy, which the DCs are attempting to process(its not being superseded with higher linked GPO etc).    

I'm have multiple entries in the Application log for Event 1202(SCECLI - Error code 0x4b8: An extended error has occurred), which makes sense as I've looked through the Winlogon.log and I can see its not happy with many of the attempts to apply the the restricted groups etc...    

I've never seen restricted groups used on Domain Controllers before and I believe its not recommended as Restricted groups should only be used to configure "Local Groups".... but is there anything I'm missing here? I've been working with AD for 20+ yrs and I'm quite experienced, but I just wanted to ask the question to confirm my thinking here(before I raise a change to remove the groups from the GPO)!    

Thanks    

Pete

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-13*

Hi,    

Thanks for the response Daisy :)    

I think my main concern is the "fear of the unknown" really....eg is there going to be a negative impact of removing the groups?! I think I'll need to test the scenario in my lab to be 100% sure. If I do then I'll update with my findings.    

Cheers,    

Pete

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-12-13*

Hello PeterTosney-3203,    

Thank you for posting in our Q&A forum.    

Q: I've never seen restricted groups used on Domain Controllers before and I believe its not recommended as Restricted groups should only be used to configure "Local Groups".... but is there anything I'm missing here?    

A: I think you are right. From the link below, I can see:    

Microsoft doesn't support using restricted groups in this scenario. Restricted Groups is a client configuration means, and can't be used with domain groups. Restricted Groups is designed specifically to work with local groups. Domain objects must be managed within traditional AD tools. We don't plan currently to add or support using restricted groups as a way to manage domain groups.    

Description of group policy restricted groups    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/description-of-group-policy-restricted-groups    

Meanwhile, we can know more information about restricted groups.    

https://social.technet.microsoft.com/wiki/contents/articles/20402.active-directory-group-policy-restricted-groups.aspx    

https://learn.microsoft.com/en-us/answers/questions/557831/domain-controller-builtinadministrators.html    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou    

===============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
