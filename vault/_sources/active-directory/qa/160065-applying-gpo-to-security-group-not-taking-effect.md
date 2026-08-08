---
title: "Applying GPO to Security Group not taking effect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/160065/applying-gpo-to-security-group-not-taking-effect
question_id: 160065
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Applying GPO to Security Group not taking effect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/160065/applying-gpo-to-security-group-not-taking-effect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've spent the past 40 hours trying to figure out what's causing this, so far no luck, I've head dozens of articles & different questions of this topic and not a single one has helped with this... Just showing the problem isn't going to help because I've done the same as everyone else, so I'll try to explain what I've done so if maybe I've missed something then someone can point it out.    

I make a new Organizational Unit called "Staff" under my forest.    

    

Then I make a security group called "Managers" & add a user under this group called "Ty".    

    

Then I go to the "Group Policy Management" tool (gpmc.msc).    

I right click the "Staff" unit, then "Create a GPO in this domain, and link it here" called "Manager Policy".    

    

I click the new GPO, go to the Delegation tab, select advanced, then select "Authenticated Users", I keep read on but remove the tick from "Apply group policy".    

Then I add the "Managers" group and check "Apply group policy" for it.    

    

Now I right click the "Manager Policy" and select Edit.    

    

I navigate to "User Rights Assignment" under "Computer Configuration" and define "Access this computer from the network" with "Everyone" & "Allow log on through Remote Desktop Services" with "HORIZONS\Managers".    

    

Once I have added the Policies, I open the command prompt and type "gpupdate /force".    

    

Then I check to see if its applied using "gpresult /r /scope computer" which displays that the GPO has not been applied.    

    

& to double check I try logging into the account in which I receive "The connection was denied because the user account is not authorized for remote login.".    

    

What am I doing wrong or missing? I've spent too long trying to do something that should be so straightforward...

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2020-11-12*

Hi,  

I think i figured out why the group policy didn't apply.  

Before going further, we’d better confirm the difference between Computer Configuration and User configuration.   

Computer Configuration in Group Policy is applied to computers, regardless of who logs on to the computers.   

User Configuration in Group Policy is applied to users, regardless of which computer they log on to.  

Computer Configuration  

http://technet.microsoft.com/en-us/library/cc736413(v=ws.10).aspx  

User Configuration  

http://technet.microsoft.com/en-us/library/cc781953(v=ws.10).as  

As you mentioned above ,the policy "User Rights Assignment" is a "Computer Configuration" it can be only linked to OUs containing computer objects.  

But the Organizational Unit called "Staff" contains no computers. So the policy would not apply.  

And in the security filter, if you remove the apply permission for the authenticated users , we have to put the computers (not users) into one security group and give it read and apply permission.  

Or keep the authenticated users read and apply permission, then you don't need to add any groups into the security filter.  

Last ,since it is a computer policy , when you update the policy by command , run the command as administrator ,or restart the computer.  

Hope it would be helpful.  

Best Regards,
