---
title: "windows update vs wsus gpo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5630761/windows-update-vs-wsus-gpo
question_id: 5630761
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# windows update vs wsus gpo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5630761/windows-update-vs-wsus-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I enabled Windows 10/11 clients to use internal Wsus server for Windows update via gpo but now clients show neither "install now" button nor "check update" button. 

It's possible to show both again before to set wsus reference?

Does It exist way to unlink temporarily Windows 10/11 client (with administrator rights, of course) from WSUS to access directly to Microsoft Windows Update servers ?

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2025-11-21*

I enabled Windows 10/11 clients to use internal Wsus server for Windows update via gpo but now clients show neither "install now" button nor "check update" button.
It's possible to show both again before to set wsus reference?

You have set a policy to remove access to view those buttons. When done properly, clients will see the check for updates button with an optional drop down for "check online" to query Windows Update servers directly, bypassing WSUS (default - removable with a specific group policy).

Review my 8 part blog series - part 4 are the GPO policies and part 5 is how to apply it for an inheritence setup.

https://www.ajtek.ca/wsus/how-to-setup-manage-and-maintain-wsus-part-5-linking-your-gpos-inheritance-is-your-friend/

Does It exist way to unlink temporarily Windows 10/11 client (with administrator rights, of course) from WSUS to access directly to Microsoft Windows Update servers ?

Answered above (except it's not requiring Admin rights - any user will be able to do it).

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-11-21*

Hello,

The behavior you are observing is likely due to a feature called "Dual Scan". Even when you configure a client to point to a WSUS server using the "Specify intranet Microsoft update service location" Group Policy Object (GPO), certain other policies can trigger the client to also scan Windows Update online.

This dual scanning is typically enabled automatically if you have configured any of the Windows Update for Business (WUfB) deferral policies, such as:

-  Select when Quality Updates are received

-  Select when Feature Updates are received

When Dual Scan is active, the Windows Update client will check both your internal WSUS server and the public Windows Update service for updates.

To ensure your client machines only get updates from your WSUS server and do not reach out to the internet, you have 2 options. 

Option 1: Disable Dual Scan Behavior

If you are using WUfB deferral policies alongside WSUS, you can explicitly disable dual scanning. This will force the client to only use your specified WSUS server.

-  Open the Group Policy Management Editor.

-  Navigate to: `Computer Configuration > Administrative Templates > Windows Components > Windows Update`.

-  Locate the policy named "Do not allow update deferral policies to cause scans against Windows Update".

-  Set this policy to Enabled.

By enabling this policy, you are telling the client not to scan Windows Update when deferral policies are configured, effectively stopping the dual scan behavior.

Option 2: Block All Connections to Windows Update Internet Locations

For a more stringent approach, you can block all communication to any external Windows Update services. This is a good option if you want to ensure no updates are ever pulled from the internet.

-  Open the Group Policy Management Editor.

-  Navigate to: `Computer Configuration > Administrative Templates > Windows Components > Windows Update`.

-  Find the policy "Do not connect to any Windows Update Internet locations".

-  Set this policy to Enabled.

Important Note: Enabling this policy may affect other functionalities that rely on connecting to public update services, such as the Microsoft Store.

After applying either of these GPO changes, remember to run `gpupdate /force` on the client machine and you may need to restart the Windows Update service for the changes to take immediate effect.

I hope this explanation and the provided solutions help you resolve the issue. Please let me know if you have any further questions.

If you find this information helpful, please "Accept Answer" to help other members of the community.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-11-21*

To temporarily unlink a Windows 10/11 client from a WSUS server and allow it to access the Microsoft Windows Update servers directly, you can modify the Group Policy settings that point the client to the WSUS server. Here are the steps you can follow:

-  Open the Group Policy Editor: You can do this by typing `gpedit.msc` in the Run dialog (Win + R).

-  Navigate to the Windows Update Policies: Go to `Computer Configuration -> Administrative Templates -> Windows Components -> Windows Update`.

-  Locate the WSUS Settings: Find the policy named Specify intranet Microsoft update service location.

-  Set the Policy to Not Configured: Change this policy to Not Configured or Disabled. This will allow the client to revert to using the public Windows Update service.

-  Force Group Policy Update: Open Command Prompt with administrator privileges and run the command `gpupdate /force` to apply the changes immediately.

-  Check for Updates: After the policy has been updated, you should see the Check for updates button in the Windows Update settings, allowing you to access the Microsoft Windows Update servers directly.

Please note that these changes will only be temporary, and once you re-enable the WSUS settings, the clients will again point to the WSUS server for updates.

References:

-  Use Windows Update client policies and WSUS together

-  Deploy Windows client updates using Windows Server Update Services (WSUS)

-  Configure Group Policy settings for automatic updates
