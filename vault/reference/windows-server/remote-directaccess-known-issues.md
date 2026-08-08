---
title: "DirectAccess Known Issues"
type: reference
domain: windows-server
slug: remote-directaccess-known-issues
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/directaccess/DirectAccess-Known-Issues
family: remote
documentKind: "troubleshooting-known-issue"
abstract: "This topic provides a link to Microsoft Technical Support documents for DirectAccess in Windows Server 2016."
---

# DirectAccess Known Issues

# DirectAccess Known Issues

> [!div class="nextstepaction"]
> <a href="https://vsa.services.microsoft.com/v1.0/?partnerId=7d74cf73-5217-4008-833f-87a1a278f2cb&flowId=DMC&initialQuery=31806260" target='_blank'>Try our Virtual Agent</a> - It can help you quickly identify and fix common DirectAccess issues.

## DNS registration of DirectAccess client IPv6 addresses

Starting with the Windows 10 May 2020 Update, a client no longer registers its IP addresses on DNS servers configured in a Name Resolution Policy Table (NRPT).
If DNS registration is needed, for example **Manage Out**, it can be explicitly enabled with this registry key on the client:

Path: `HKLM\System\CurrentControlSet\Services\Dnscache\Parameters`<br/>
Type: `DWORD`<br/>
Value name: `DisableNRPTForAdapterRegistration`<br/>
Values:<br/>
`1` - DNS Registration disabled (default since the Windows 10 May 2020 Update)<br/>
`0` - DNS Registration enabled
