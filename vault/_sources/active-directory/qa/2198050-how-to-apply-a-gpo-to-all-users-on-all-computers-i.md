---
title: "How to apply a GPO to all users on all computers in Active Directory 2022?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198050/how-to-apply-a-gpo-to-all-users-on-all-computers-i
question_id: 2198050
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 2
qa_tags: []
---
# How to apply a GPO to all users on all computers in Active Directory 2022?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198050/how-to-apply-a-gpo-to-all-users-on-all-computers-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to set a default Wallpaper for all users, on all computers in a Windows Server 2022 AD environment, but I am getting strange results.

I am applying 03 settings:

```
// So I can access unauthenticated shared folders
Computer Configuration\Policies\Administrative Templates\Network\Lanman Workstation\Enable insecure guest logons : Enabled
    
// Create a Z drive on all computers mapped to a shared folder
User Configuration\Preferences\Windows Settings\Drive Maps : Z => \\some-ip\some-location
    
// Set the wallpaper from the shared folder
User Configuration\Policies\Administrative Templates\Desktop\Desktop\Desktop Wallpaper : Enabled, Wallpaper Name = Z:\wallpaper.jpg
```

When I sign in as `Administrator` to a computer from the `Domain Controllers` or `Computers` built-in folders, everything works well. If I use another user account it doesn't work, the background is black. I even added that account to all the groups that `Administrator` belongs to, with the same result.

When I sign in as `Administrator` to a computer from a non-built-in folder, the default background is used, it is like my GPO is not applied. If I use another account, the background is black, just like it failed to apply the GPO.

I am totally lost with it, please help. Note that all machines are Hyper-V Guests, and the shared folder is from the Hyper-v Host, all connected with Hyper-v Internal Switch.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-06*

Hello Alain Moune,  

Thank you for posting in Microsoft Community forum.  

Please check or troubleshoot some settings below:  

1.Where did you link this GPO (the domain or one OU)? If you link this GPO to one OU, please put all the user accounts and Administrator to the same OU.  

2.Check if all the domain users can access the shared folder with wallpaper picture.  

3.You can change Z:\wallpaper.jpg to \some-ip\some-location\wallpaper.jpg from the third setting and check if it helps.  

4.Check if you set any GPO filter (WMI filter and security filter).  

5.Check group policy result via gpresult.  

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
