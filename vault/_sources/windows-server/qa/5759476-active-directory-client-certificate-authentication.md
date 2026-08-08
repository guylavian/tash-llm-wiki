---
title: "Active Directory Client Certificate Authentication is missing from Features View"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5759476/active-directory-client-certificate-authentication
question_id: 5759476
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
answer_author_roles: ["Independent Advisor", "Q&A User"]
---
# Active Directory Client Certificate Authentication is missing from Features View

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5759476/active-directory-client-certificate-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My company is trying to setup PKI auth for our users.  We already have a CA and PKI certs for the users.   We are trying to setup PKI auth on our websites running on IIS on Server 2022.   We follow these instructions: https://learn.microsoft.com/en-us/iis/configuration/system.webserver/security/authentication/clientcertificatemappingauthentication

and

  https://learn.microsoft.com/en-in/answers/questions/2123709/how-to-use-client-certificate-in-iis-manager

However after we install "IIS Client Certificate Mapping Authentication" in Roles and Features, and reboot, we do not see the option under:  Connections:  Authentication:  Features View.

The only options that show are  Windows Authentication, Forms Authentication, ASP.Net Authentication, and Anonymous Athentication. 

Could some of our hardening be causing this option to not appear?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2026-02-04*

Domic,  Thank you for the quick reply.

Correct we are not using Windows 365 for Business.  I pasted the wrong link.  This is the link to the discussion I was following:  https://learn.microsoft.com/en-my/answers/questions/2123709/how-to-use-client-certificate-in-iis-manager

So using the command line I was able to get the correct IIS Client Certificate Mapping Authentication using the Powershell commands to add it.  It shows up at the server level in IIS under Authentication, not at the Default Web Page under Authentication.  But from Powershell I was able to add it at the Default Web Page level.    We also had configured SSL to required a certificate under bindings, and made sure a CA cert is assigned to our webport.

Previously our page just went to error 400 but now that has changed.. but not working just yet.

Something is still missing because the webpage for PKI auth is in a revolving loop now, where it never shows a PKI popup. (once we have this working will the users PKI in their browser pop-up to show which cert they are using to authenticate?)

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-02-03*

Hello [Carey Wharton],

  It is strictly a Windows Server 2022 / IIS configuration problem. Windows 365 Enterprise is a cloud‑based virtual desktop service, and Windows for Business refers to licensing and update channels for client operating systems. What you are dealing with here is a server‑side role service feature not surfacing correctly in IIS Manager.

When you install “IIS Client Certificate Mapping Authentication” through Server Manager > Add Roles and Features, the feature should register its module with IIS. If after reboot you only see Windows Authentication, Forms Authentication, ASP.NET Authentication, and Anonymous Authentication, it means the module did not register with IIS Manager. This can happen if the installation was incomplete, if the IIS Management Console feature was hardened or stripped, or if registry keys under HKLM\SOFTWARE\Microsoft\InetStp\Components were modified by your baseline.

The first place to check is whether the module DLL is present. Look under %windir%\System32\inetsrv\authmap.dll. If that file is missing, the feature did not install correctly. If it is present, open IIS Manager, go to Modules at the server level, and confirm that CertificateMappingAuthenticationModule is listed. If it is not, you can manually add it by editing applicationHost.config under %windir%\System32\inetsrv\config.

Hardening baselines can indeed cause this option to disappear. If your security baseline disabled or removed the IIS Management Console snap‑ins, the UI will not expose the feature even though the module is installed. In that case, you can still configure client certificate mapping authentication directly in the configuration files or via PowerShell using Set-WebConfigurationProperty.

So to summarize: this is a Windows Server 2022 IIS role service issue, not Windows 365 Enterprise or Windows for Business. Check that authmap.dll is installed, verify the module registration in IIS, and review your hardening baseline to ensure it has not removed the management UI components. If the module is installed but hidden, you can configure it manually in applicationHost.config.

I hope you've found something useful here. If it helps you get more insight into the issue, it's appreciated to accept the answer. Should you have more questions, feel free to leave a message. Have a nice day!

Domic Vo.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-02-03*

If the IIS Client Certificate Mapping Authentication feature is not appearing in the Features View after installation, it could be due to several reasons:

-  Installation Verification: Ensure that the feature was installed correctly. You can verify this by checking the installed features in the Server Manager under the Roles and Features section.

-  Server Role: Make sure that the IIS Web Server role is properly installed and that all required components are included. Sometimes, missing dependencies can prevent certain features from appearing.

-  Hardening Policies: If your server has been hardened, certain security policies may restrict the visibility or functionality of specific features. Review your security settings to ensure that they are not interfering with IIS features.

-  IIS Configuration: Check if the IIS configuration is correctly set up to display all authentication options. Sometimes, specific settings or configurations can hide certain features.

-  Reboot: Although you mentioned rebooting, ensure that the server was fully restarted after the installation of the feature, as some changes may require a complete reboot to take effect.

If these steps do not resolve the issue, consider checking the event logs for any errors related to IIS or the installation process, which might provide more insight into the problem.
