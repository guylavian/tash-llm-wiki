---
title: "Using GPO to restrict USB drives"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198002/using-gpo-to-restrict-usb-drives
question_id: 2198002
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Using GPO to restrict USB drives

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198002/using-gpo-to-restrict-usb-drives (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I setup up a GPO to restrict USB drives on my system to read only. I created a security group and allowed that group write access, but this is not working. What am I missing here?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-17*

Hello Neil_59,  

Thank you for your reply.  

Because you linked the GPO at the domain level and enabled the "Removable Disks: Deny write access", it means you deny all the domain users to write.  

And then you created a security group (the users in this group are in the domain) and added this under Delegation with "Write" access granted, it will not write, because denning permission take precedence over allowed permission.  

You can try to put the users in different OU and create different GPO to link to different OU.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-16*

Daisy,

Thanks for your attention to this, and sorry for the confusion. 

Here is what I am attempting to do:

-  Create a GPO to restrict Removable storage access to "Read Only" and enabling it under "User Configuration."

-  Next, I want to grant some users the ability to "Read and Write" and exempt them from the "Read Only" restriction

What I have done:

-  I created the GPO and linked it at the domain level 

-  I enabled the "Removable Disks: Deny write access, and disabled the "Deny read access." This worked exactly as it should

-  I created a security group and added this under Delegation with "Write" access granted. This is intended to bypass the "read only" access but it is not working.

I verified that the GPO is applying after every change. The only way to write to a Removable disk is to use the prompt for Admin authorization when the user attempts to write to the disk.

What am I missing here?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-15*

Hello Neil_59,  

Thank you for your reply.  

I'm sorry I'm a bit confused about your question.  

You do not want all the domain users including domain administrator to access, nor to write the USB drivers?  

OR  

You do not want all the domain users including domain administrator to access, but be able to write the USB drivers?  

OR  

on your system to read only, but on other systems to read and write? Did you want the GPO setting to apply to user or computer?  

OR  

Why did you created a security group and allowed that group write access, but this is not working?  

Where did you link the GPO (domain or one OU)?  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-14*

I setup up a GPO to restrict USB drives on my system to read only.

1.What gpo setting did you configure?   

2.Is it "Removable Disk: Deny read access" under User Configuration?

-  Removable Disk under User Configuration  

4.So you set it successfully, am I right? I mean it applies to users or computer

-  Yes, it tested successfully up to this point as long as the group "Authenticated User" was in the Security Filtering Scope Settings. When users attempted to write they are prompted for Admin permission, and if entered it would work. (if the Administrator is the one logged in, this will not work).  

I created a security group and allowed that group write access, but this is not working.  

1.What type of object did you add within this security group? User objects or Computer objects?

-  I added users objects in this group  

2.Are the objects in this security group the same as the objects with "Removable Disk: Deny read access"? Or they are different objects?

-  The objects are the same. Yes, I checked and the GPO is applied.

Still no results.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-08*

Hello Neil_59,  

Thank you for posting in Microsoft Community forum.

I setup up a GPO to restrict USB drives on my system to read only. 

1.What gpo setting did you configure?    

2.Is it "Removable Disk: Deny read access" under User Configuration?  

3.Or is it "Removable Disk: Deny read access" under Computer Configuration?  

4.So you set it successfully, am I right? I mean it applies to users or computers.

I created a security group and allowed that group write access, but this is not working.  

1.What type of object did you add within this security group? User objects or Computer objects?  

2.Are the objects in this security group the same as the objects with "Removable Disk: Deny read access"? Or they are different objects?  

For the same object, the priority of rejection is higher than that of allowed.

You can check if gpo is applied via gpresult.  

For checking Computer Configuration within gpresult, we can follow steps below.

Logon this machine using administrator account.

Open CMD (run as Administrator).

Type gpresult /h C:\gpo.html and click Enter.

Open gpo.html and check gpo setting under "Computer Details".

For checking User Configurations within gpresult, we can follow steps below.

Logon the machine using normal domain user account.

Create a folder named F1.

Open CMD (do not run as Administrator).

Type gpresult /h C:\F1\gpo.html and click Enter.

Open gpo.html and check gpo setting under "User Details".  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
