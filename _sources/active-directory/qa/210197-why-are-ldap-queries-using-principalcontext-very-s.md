---
title: "Why are LDAP queries using PrincipalContext very slow since upgrading to Windows Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/210197/why-are-ldap-queries-using-principalcontext-very-s
question_id: 210197
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Why are LDAP queries using PrincipalContext very slow since upgrading to Windows Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/210197/why-are-ldap-queries-using-principalcontext-very-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We recently upgraded from Windows 2008 R2 to Windows Server 2019 and since the upgrade the piece of code below now takes over a minute to run when it previously took 1 to 2 seconds. Using netmon I can see that the server is making multiple DNS calls to locate the dc even though we specified the fully qualified name of the dc in the request. The network adapter on the server is configured to append 3 different DNS suffixes and calls are made using each suffix to determine the dc even though it is not necessary. If I remove ContextOptions.Negotiate and use ContextOptions.SimpleBind then these additional calls are not made. Unfortunately this is not a viable option. I also ran the same test on a Windows 2008 R2 server with the additional DNS suffixes as well and no calls are made to locate the dc so the call completes fast. I also used tracelog on both the windows 2008 R2 server and on the Windows 2019 server and compared them and the main difference is that the log from the Windows 2019 server contains the text “LDAP connection 0x7e86118 attempting to resolve 'FULLQUALIFIEDDCNAME.COM' using DC locator.” Why is it trying to locate the dc when I specified the fully qualified name of the dc??

Dim oPrincipalContext As New PrincipalContext(ContextType.Domain, Me.activeDirectoryHost & ":636", sDefaultSearchUserOU, ContextOptions.ServerBind Or ContextOptions.Negotiate Or ContextOptions.SecureSocketLayer, sDomain & "\" & sServiceUser, sServicePassword)  

Dim oUserContext As OurCustomUserPrincipalExtended = OurCustomUserPrincipalExtended.FindByIdentity(oPrincipalContext, sUserName)

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-29*

Hi Daisy  

I was able to reproduce this on a new (non-upgraded) Windows 2019 server. I added the 3 DNS suffixes to the network adapter, then I logged out, logged back on and then did bind using ldp.exe with negotiate and the UI hangs for over a minute.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-28*

Did you try adding additional DNS suffixes? I don't think this is an issue with the DC because I can bind to the same DC from a Windows 2008 R2 server and it's fast but if I bind to the same DC from a Windows 2019 server it's slow (both servers have the additional DNS suffixes). On the Windows 2019 Server I can see a lot of DNS requests to determine the ip of the DC even though I supplied the fqdn. I should also mention that the 2019 Server and 2008 R2 Servers that query the DC are not on the same domain as the DC. We also see this issue if we bind on port 389 w/o SSL when we use ContextOptions.Negotiate. If I use the ip instead of the fqdn then the call completes quickly and we don't see the additional DNS requests in the netmon log. Unfortunately you cannot use the ip when using SSL. From 2008 server using ldp.exe:  From the 2019 server using ldp.exe:

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-25*

Hi Daisy  

-  Yes we upgraded to Windows Server 2012 R2 and then to Windows Server 2019.  

-  Unfortunately I don't have access to a server that is a fresh install of Windows Server 2019 so I cannot verify.  

-  The domain controller is running on Windows Server 2019  

-  Yes if I point to other dcs I can still reproduce the issue  

-  You can reproduce using any ldap query from Windows Server 2019. The code below also reproduces this issue:  

Dim oPrincipalContext As New PrincipalContext(ContextType.Domain, Me.activeDirectoryHost & ":636", sDefaultGroupCompaniesOU, ContextOptions.ServerBind Or ContextOptions.Negotiate Or ContextOptions.SecureSocketLayer, sDomain & "\" & sServiceUser, sServicePassword)  

Dim oGroupPrincipal As GroupPrincipal = GroupPrincipal.FindByIdentity(oPrincipalContext, sGroupName)  

-  Yes server and domain controller are properly configured.  

-  This issue is reproducible on the Windows Server 2019 server using ldp.exe. The UI hangs for over a minute until the bind completes. Using ldp.exe on the Windows 2008 R2 server the bind is instantaneous.  

Thanks for the help!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-25*

Hello @hbuelow  ,

Thank you for posting here.

To better understand our question, please confirm the following informaton:  

1.Did you upgrade Windows server 2008 R2 to Windows server 2012 R2,then to Windows Server 2019?  

2.Do you have the same issue when running the same code on one newly installed Windows server 2019?  

3.Is the Windows server 2008 R2 or Windows Server 2019 you mentioned Domain Controller or member server?  

4.Did you have the same issue when running the same code on other DCs or other member servers?  

5.How can I test the code on one Windows server 2019 in my lab?  

6.Check if the server or domain controller is correctly configured with site and subnet?  

7.Would you please check if you have the same issue via UI on this server and other server?

Steps to check:  

1.Open CMD and type ldp.exe and click Enter.  

2.Click "connect" under Connect tab and provide the information based on your environment information.  

3.Click "bind" under Connect tab and provide the information based on your environment information.  

If anything is unclear, please feel free to let us know.

Best Regards,  

Daisy Zhou
