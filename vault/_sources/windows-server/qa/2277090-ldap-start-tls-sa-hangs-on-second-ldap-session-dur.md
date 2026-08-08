---
title: "ldap_start_tls_sA hangs on second LDAP session during persistent search on Windows Server 2022/2019?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2277090/ldap-start-tls-sa-hangs-on-second-ldap-session-dur
question_id: 2277090
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# ldap_start_tls_sA hangs on second LDAP session during persistent search on Windows Server 2022/2019?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2277090/ldap-start-tls-sa-hangs-on-second-ldap-session-dur (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm using the LDAP C API (`wldap32.dll`) in a Delphi app on Windows Server 2022 (also reproducible on Server 2019). The problem:

-  The first instance of my class connects to Active Directory with `ldap_start_tls_sA` and starts a persistent search (OID `1.2.840.113556.1.4.528`) to monitor changes, polling `ldap_result` every 2 seconds on a separate thread.

A second instance in the same process/thread tries to start its own TLS connection with `ldap_start_tls_sA`.

Issue: When the persistent search is active, the second `ldap_start_tls_sA` call hangs indefinitely. Wireshark shows TCP handshake completes, but the TLS handshake never starts. Eventually, the server sends a TCP RST.

This doesn’t happen on Windows 11 — both sessions work concurrently.

Diagnostics: Calling `ldap_abandon` on the first instance's persistent search message ID allows the second `ldap_start_tls_sA` to succeed.

What I tried:

Proper locking to avoid simultaneous calls to `ldap_result` and `ldap_start_tls_sA`.

Verified the first instance polls every 2 seconds without blocking long.

Tweaked Schannel registry settings (`EventLogging=7`, `ClientCacheTime=0`) and restarted OS.

Tested on Windows Server 2019 with same results; no issue on Windows 11.

Questions:

Is there a known limitation on Windows Server 2022/2019 for concurrent LDAP TLS connections during persistent searches?

Any recommended workarounds or configuration changes to avoid `ldap_start_tls_sA` blocking?

Could Schannel or LDAP caches behave differently across OS versions affecting this?

Thanks in advance for any insights!

```
Sample Code in Delphi:

//LDAPClient1 instance connects and registers for notifications successfully. LDAPClient2 gets stuck at ldap_start_tls_sA and control never returns back.

const
 
FILTER_ALL_RECORDS = 'ObjectClass=*'
CHANGE_NOTIFICATION_OID  = '1.2.840.113556.1.4.528';

//SSL CallBack function
function SSLCallBackVerifyServerCertificate(Connection: PLDAP;
  pServerCert: Pointer): ByteBool;
begin
    Result := True;
end;

//Connects with Active Directory
function TLDAPClient.Connect( const Host : string; Port : DWORD; const User: String; const Password: String ): Boolean;
var
RetVal, SRetVal: ULONG;
PLDAPMsg: PLDAPMessage;
ServerControl, ClientControl: PLDAPControlA;
begin
    Result := False;

    FDirSession := ldap_init(PChar(Host), PortNumber);
    
    if ( FDirSession <> nil ) then
    begin
        RetVal := ldap_Connect(FDirSession, nil);

        if RetVal = LDAP_SUCCESS then
    begin
            RetVal :=    ldap_set_option(FDirSession,LDAP_OPT_SERVER_CERTIFICATE,@SSLCallBackVerifyServerCertificate);

            PLDAPMsg := nil;
            ServerControl := nil;
            ClientControl := nil;

            // Start TLS negotiation
            RetVal := ldap_start_tls_sA(FDirSession, @SRetVal, @PLDAPMsg, ServerControl, ClientControl);
            if ( RetVal = LDAP_SUCCESS )
        RetVal := ldap_bind_s(FDirSession,PChar(User), PChar(Password), LDAP_AUTH_SIMPLE);
            Result := (RetVal = LDAP_SUCCESS);
    end;
    end;
end;

//Resisters for change notifications
function TLDAPClient.RegisterForNotifications(BaseDN : PChar; Scope : DWORD; ExtraAttribute : string): Cardinal;
var
ServerControl: LDAPControl;
ServerControlArray: array [0..1] of PLDAPControl;
PtrServerControl: ^PLDAPControl;
PtrClientControl: ^PLDAPControl;
MessageNumber: Cardinal;
Attributes: array[0..10] of PChar; 
begin
    ServerControl.ldctl_oid := CHANGE_NOTIFICATION_OID;
    ServerControl.ldctl_iscritical := TRUE;
    ServerControl.ldctl_value.bv_len := 0;
    ServerControl.ldctl_value.bv_val := nil;

    ServerControlArray[0] := @ServerControl;
    ServerControlArray[1] := nil;
    PtrServerControl:= @ServerControlArray;
    PtrClientControl:= nil;

    Attributes[0] := PChar(ExtraAttribute);
    Attributes[1] := PChar(AD_IS_DELETED);
    Attributes[2] := PChar(AD_USN_CHANGED); 
    Attributes[3] := PChar(AD_WHEN_CREATED);                          
    Attributes[4] := PChar(AD_WHEN_CHANGED);                          
    Attributes[5] := PChar(AD_USN_CREATED);                           
    Attributes[6] := nil;    
    Result := ldap_search_ext(FDirSession,BaseDN,Scope,FILTER_ALL_RECORDS,@Attributes,0,PtrServerControl^,PtrClientControl^,0,0,MessageNumber);  

//A dedicated thread is used to make a call to ldap_result periodically to check for the change notifications. 2 seconds max time is used for it to timeout if there is no change notification so that it does not block. Issue can be produced without it.                     
end;

procedure TForm1.ConnectButtonClick(Sender: TObject);
var
LDAPClient1, LDAPClient2 : TLDAPClient;
begin
    LDAPClient1 := TLDAPCient.Create();
    if ( LDAPClient1.Connect([Host Name], 389, [User Name], [Password] )
    LDAPClient1.RegisterForNotifications([Base DN], LDAP_SCOPE_ONELEVEL, 'objectGUID');
    
    LDAPClient2 := TLDAPCient.Create();
    if ( LDAPClient2.Connect([Host Name], 389, [User Name], [Password] )
    LDAPClient2.RegisterForNotifications([Base DN], LDAP_SCOPE_ONELEVEL, 'objectGUID');
end;
```

## Answers

_No answers on this thread._
