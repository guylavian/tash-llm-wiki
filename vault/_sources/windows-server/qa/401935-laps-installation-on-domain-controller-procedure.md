---
title: "laps installation on domain controller procedure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/401935/laps-installation-on-domain-controller-procedure
question_id: 401935
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# laps installation on domain controller procedure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/401935/laps-installation-on-domain-controller-procedure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I had found an article on installing LAPS and went through installing on a domain controller. I setup a test OU and put a few pc's in it and only ran commands so that the one OU and pc's in it were managed as a test. I did install the full LAPS on the DC (or all options I should say).  I then found an article that says don't install the GPO extension on the DC. I'm hoping this doesn't phase anything if I did not direct LAPS GP to point to our Domain Controllers OU and do not plan on it. I believe if it's not set to that OU things should be fine yet and it should not phase the domain admin password on the server end?  

Can someone correct  me? And if I need to revert this right now would be the time as I only have it on a few test computers ( and it is working).   

Just want to make sure nothing with domain password for admin will break.  

I am guessing the reason they say not to is so that incase you do point it at domain controller OU it will change admin password for domain? Or if someone can better explain this and help me I would appreciate it.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-21*

Hi，  

This should only be applied and working against this OU as you mentioned above.  

You can't manage the password outside of the specific OU.  

Fan

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-20*

@Pavel yannara Mirochnitchenko     @Anonymous   Hello and thank you both for posting some answers. We went ahead and removed the GPO Extension from the LAPS tool install on the DC. So now it just has management UI and of course the powershell and GPO Template etc.     

On top of this when we initially set it up we setup a test OU, put 2 test machines in it, did all commands against this particular OU for LAPS in powershell as instructions note for install.  Also created a sec group to have permissions to read and reset pass in attributes for LAPS pwd and expiration in AD and assigned that to the OU as well.  We setup Group policy and applied it to only this OU, no other OU's or workstations/servers/DC's etc.  This was to test functionality. We turned on the 2 GP features which was managed local admin pass and length and expiration of password in policy.     

This being said, this should only be applied and working against this OU.  Can we confirm that is the case based off of what I explained? The passwords on our test machines were in AD and as expected were created and stored in AD.     

I appreciate the responses!

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-05-20*

Password will be changed by LAPS only when the LAPS GPO is applied and the password policy is set there. If you just installed the laps client on DC, nothing yet will happen.
