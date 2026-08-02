---
title: "DCOM Interface Call fails with Kerberos"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1662443/dcom-interface-call-fails-with-kerberos
question_id: 1662443
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-cpp", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# DCOM Interface Call fails with Kerberos

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1662443/dcom-interface-call-fails-with-kerberos (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We try to move one of our current DCOM Applications that Impersonates a Client from NTLM over to Kerberos. So I tryed to get a minimal Example running.

I Init the Server and Client as follows:

```
CoInitializeSecurity(NULL, -1, NULL, NULL, RPC_C_AUTHN_LEVEL_DEFAULT, RPC_C_IMP_LEVEL_IMPERSONATE, NULL, EOAC_MUTUAL_AUTH, NULL);
```

Then I create the Remote Server from the Client via:

```
COSERVERINFO serverInfo;
ZeroMemory(&serverInfo, sizeof(COSERVERINFO));

COAUTHINFO athn;
ZeroMemory(&athn, sizeof(COAUTHINFO));

athn.dwAuthnLevel = RPC_C_AUTHN_LEVEL_PKT_PRIVACY;
athn.dwAuthnSvc = RPC_C_AUTHN_GSS_KERBEROS;
athn.dwAuthzSvc = RPC_C_AUTHZ_DEFAULT;
athn.dwCapabilities = EOAC_MUTUAL_AUTH;
athn.dwImpersonationLevel = RPC_C_IMP_LEVEL_IMPERSONATE;
athn.pAuthIdentityData = NULL;
athn.pwszServerPrincName = L"HOST/";

serverInfo.pwszName = L"";
serverInfo.pAuthInfo = &athn;
serverInfo.dwReserved1 = 0;
serverInfo.dwReserved2 = 0;

MULTI_QI qi = {&IID_ITestKerbAuth, NULL, S_OK};

HRESULT hr = CoCreateInstanceEx(CLSID_TestKerbAuth, NULL, CLSCTX_REMOTE_SERVER , &serverInfo, 1, &qi);
```

And after that I try to call the Interface:

```
if (SUCCEEDED(qi.hr)) {
    ITestKerbAuth* pMyInterface = reinterpret_cast(qi.pItf);
    hr = pMyInterface->TestCall();
    pMyInterface->Release();
}
```

If I Configure the Application Identity via dcomcnfg with a system Account, a Specific User Account or for the interactive User everything works fine. But if I try to set the Application Identity to Launching User, I get:

Error: 80070721 A security package specific error occurred.

The Initial logon to start the Server still succeeds, but all following calls to the Interface fail with the above mentioned Error. If I dont disable NTLM, DCOM is able to fallback to NTLMv2 to call the Interface.

I already tried to set a Service Specific SPN, enabled all the login for Kerberos, enabled logon auditing, tried to call with administrator Privileges, but still have no clue what exactly is wrong.

Can anyone provide any input on how to debug or troubleshoot this issue?

Thanks!

## Answers

_No answers on this thread._
