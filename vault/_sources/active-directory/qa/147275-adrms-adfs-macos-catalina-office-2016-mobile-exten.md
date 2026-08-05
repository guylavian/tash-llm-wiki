---
title: "ADRMS + ADFS + MacOS catalina + office 2016 + Mobile Extension not work"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/147275/adrms-adfs-macos-catalina-office-2016-mobile-exten
question_id: 147275
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ADRMS + ADFS + MacOS catalina + office 2016 + Mobile Extension not work

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/147275/adrms-adfs-macos-catalina-office-2016-mobile-exten (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've followed steps on microsoft website and finished configuration of ADFS + ADRMS + Mobile Extensions.

But it does not work properly. I opened a rms protected file on MacOS catalina. It directly prompts a window saying I don't have rights to open the file and doesn't ask me to enter account and password. I've import the root CA to MacOS.

My environment: MacOS catalina 10.15.6, Windows Server 2016, Office 2016 15.36, Mobile Extensions 1.0.114.322

I checked the word logs. It says:

10/31/2020 09:30:00.476 com.microsoft.Word  

0x700009b86000 com.microsoft.Word  

RMS Proxy Wrapper ia3wf  

Information RMS Method log {"msg":"GetPolicyWithSerializedPolicy Error: Error Domain=Authentication Code=401 \"(null)\" UserInfo={AuthenticationParametersKey={\n authority = \"https://adfs-svc.pin.com/adfs/oauth2/authorize\";\n resource = \"api.rms.rest.com\";\n scope = \"\";\n}}"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.476 com.microsoft.Word  

0x700009b86000 com.microsoft.Word  

RMS Proxy Wrapper ia3wh  

Information RMS Method log {"msg":"GetPolicyWithSerializedPolicy AuthParams: {\n authority = \"https://adfs-svc.pin.com/adfs/oauth2/authorize\";\n resource = \"api.rms.rest.com\";\n scope = \"\";\n}"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.476 com.microsoft.Word  

0x700009b86000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00] ADAL API call [Version - 2.5.0]", "AdditionalInformation": "In function: -[ADAuthenticationContext initWithAuthority:validateAuthority:cacheDelegate:error:], file line #95"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.477 com.microsoft.Word  

0x700009b86000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00] ADAL API call [Version - 2.5.0]", "AdditionalInformation": "In function: -[ADAuthenticationContext(Internal) initWithAuthority:validateAuthority:tokenCache:error:], file line #43"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.491 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

RMS Proxy Wrapper ic75l  

Information RMS Method log {"msg":"Cannot find ADAL token cache: MicrosoftOfficeRMSCredential"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.491 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

RMS Proxy Wrapper ibwen  

Information RMS Method log {"msg":"Calling acquireTokenWithResource:"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.491 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

RMS Proxy Wrapper ic75z  

Information RMS Method log {"msg":"Calling dispatchAuthBlock:"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.492 com.microsoft.Word  

0x700009b86000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00] ADAL API call [Version - 2.5.0]", "AdditionalInformation": "In function: -[ADAuthenticationContext acquireTokenWithResource:clientId:redirectUri:promptBehavior:userIdentifier:extraQueryParameters:completionBlock:], file line #391"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.492 com.microsoft.Word  

0x700009b86000 com.microsoft.Word  

IdentityADALClient ic28m  

Information [ADALLibrary]s_adalLogger {"Message": "ADALInfo.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] ##### BEGIN acquireToken (authority = https://adfs-svc.pin.com/adfs, resource = api.rms.rest.com, clientId = d3590ed6-52b3-4102-aeff-aad2292ab01c, idtype = OptionalDisplayableId) #####", "AdditionalInformation": "userId = (null)"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.492 com.microsoft.Word  

0x700009b86000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00] ADAL API call [Version - 2.5.0]", "AdditionalInformation": "In function: +[ADTokenCacheKey keyWithAuthority:resource:clientId:error:], file line #66"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.500 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

RMS Proxy Wrapper ic75l  

Information RMS Method log {"msg":"Cannot find ADAL token cache: MicrosoftOfficeRMSCredential"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.500 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00] ADAL API call [Version - 2.5.0]", "AdditionalInformation": "In function: +[ADTokenCacheKey keyWithAuthority:resource:clientId:error:], file line #66"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.500 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

RMS Proxy Wrapper ic75l  

Information RMS Method log {"msg":"Cannot find ADAL token cache: MicrosoftOfficeRMSCredential"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.501 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00] ADAL API call [Version - 2.5.0]", "AdditionalInformation": "In function: +[ADTokenCacheKey keyWithAuthority:resource:clientId:error:], file line #66"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.501 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

RMS Proxy Wrapper ic75l  

Information RMS Method log {"msg":"Cannot find ADAL token cache: MicrosoftOfficeRMSCredential"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.501 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00] ADAL API call [Version - 2.5.0]", "AdditionalInformation": "In function: +[ADTokenCacheKey keyWithAuthority:resource:clientId:error:], file line #66"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.501 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

RMS Proxy Wrapper ic75l  

Information RMS Method log {"msg":"Cannot find ADAL token cache: MicrosoftOfficeRMSCredential"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.501 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] Requesting authorization code.", "AdditionalInformation": "Requesting authorization code for resource: api.rms.rest.com"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.589 com.microsoft.Word  

0x700009b03000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] -webAuthShouldStartLoadRequest:", "AdditionalInformation": "host: adfs-svc.pin.com"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.589 com.microsoft.Word  

0x700009b03000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] +[ADURLProtocol canInitWithRequest:] handling host", "AdditionalInformation": "host: adfs-svc.pin.com"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.591 com.microsoft.Word  

0x700009b86000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] +[ADURLProtocol canInitWithRequest:] handling host", "AdditionalInformation": "host: adfs-svc.pin.com"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.591 com.microsoft.Word  

0x700009b03000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] +[ADURLProtocol canonicalRequestForRequest:]", "AdditionalInformation": "host: adfs-svc.pin.com"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.592 com.microsoft.Word  

0x700009668000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] -[ADURLProtocol startLoading]", "AdditionalInformation": "host: adfs-svc.pin.com"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.609 com.microsoft.Word  

0x700009b03000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] session:task:didReceiveChallenge:completionHandler", "AdditionalInformation": "nsurlauthenticationmethodservertrust. Previous challenge failure count: 0"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.646 com.microsoft.Word  

0x700009c09000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] +[ADURLProtocol canInitWithRequest:] ignoring handling of host", "AdditionalInformation": "host: (null)"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.647 com.microsoft.Word  

0x7000099fd000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] -webAuthShouldStartLoadRequest:", "AdditionalInformation": "host: (null)"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.647 com.microsoft.Word  

0x7000099fd000 com.microsoft.Word  

IdentityADALClient ic28m  

Information [ADALLibrary]s_adalLogger {"Message": "ADALInfo.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] -webAuthDidCompleteWithURL:", "AdditionalInformation": "urn:ietf:wg:oauth:2.0:oob?error=access_denied&error_description=MSIS9605%3a+The+client+is+not+allowed+to+access+the+requested+resource.&state=YT1odHRwcyUzQSUyRiUyRmFkZnMtc3ZjLnBpbi5jb20lMkZhZGZzJnI9YXBpLnJtcy5yZXN0LmNvbQ&client-request-id=8c83058e-1e62-42c0-b309-41234ff593a2"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.650 com.microsoft.Word  

0x7000099fd000 com.microsoft.Word  

IdentityADALClient ic28n  

Information [ADALLibrary]s_adalLogger {"Message": "ADALVerbose.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] -[ADURLProtocol stopLoading]", "AdditionalInformation": "host: adfs-svc.pin.com"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.672 com.microsoft.Word  

0x700009b86000 com.microsoft.Word  

IdentityADALClient ic28k  

Information [ADALLibrary]s_adalLogger {"Message": "ADALError.", "ErrorCode": 211, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00] Error raised: (Domain: \"ADOAuthServerErrorDomain\" Code: AD_ERROR_SERVER_AUTHORIZATION_CODE ProtocolCode: \"access_denied\" Details: \"MSIS9605: The client is not allowed to access the requested resource.\"", "AdditionalInformation": null}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.672 com.microsoft.Word  

0x7000099fd000 com.microsoft.Word  

IdentityADALClient ic28m  

Information [ADALLibrary]s_adalLogger {"Message": "ADALInfo.", "ErrorCode": 0, "ADALMessage": "ADAL 2.5.0 Mac 10.15.6 [2020-10-31 09:30:00 - 8C83058E-1E62-42C0-B309-41234FF593A2] ##### END ##### BEGIN acquireToken (authority = https://adfs-svc.pin.com/adfs, resource = api.rms.rest.com, clientId = d3590ed6-52b3-4102-aeff-aad2292ab01c, idtype = OptionalDisplayableId) ##### failed { domain: ADOAuthServerErrorDomain code: 211 protocolCode: access_denied errorDetails: MSIS9605: The client is not allowed to access the requested resource.} #####", "AdditionalInformation": null}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.672 com.microsoft.Word  

0x7000099fd000 com.microsoft.Word  

RMS Proxy Wrapper ia3ug  

Information RMS Method log {"msg":"ADAL --> Failed"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:00.672 com.microsoft.Word  

0x7000099fd000 com.microsoft.Word  

RMS Wrapper ibw5u  

Error RMSWrapper returned an error {"HRESULT": 0x-2147418113, "Error.code": 211, "Error.domain": "ADOAuthServerErrorDomain"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:02.143 com.microsoft.Word  

0x700009c09000 com.microsoft.Word  

Word View ickcq  

Information ActiveTime {"totalActiveTime": 2.618974, "totalActiveTimeInReflow": 0.000000, "totalActiveTimeInFocusMode": 0.000000}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:02.144 com.microsoft.Word  

0x700009c09000 com.microsoft.Word  

TimerScope ian14  

Information {"ID": "word.active", "Instance": 7, "Action": "Stop", "Result": 2619615}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

10/31/2020 09:30:03.060 com.microsoft.Word  

0x700009c09000 com.microsoft.Word  

TimerScope ian13  

Information {"ID": "word.active", "Instance": 8, "Action": "Start"}  

2AC37544-EF5A-4D71-9A5F-9BA2E2FCF25C  

and the MSProtection log:

{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: Secure clock file was updated successfully.",  

"ScenarioId" : "",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "WARNING",  

"ThreadId" : 775,  

"Message" : "main thread: Cached policy was not found in the database for key: QB2PvzzpUs0kkkj6+Bu25orLUqYV4LoDQGXg8BfdiAY= and user: (null)",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: Could not find a cached policy for (null)",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: Cached key for the policy not found",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: Cached key for the policy is not found.",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: Getting the challange for PL.",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "ERROR",  

"ThreadId" : 775,  

"Message" : "main thread: Could not fetch cached authInfo from the InMemoryStore",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: A valid cached discoveryServiceURL was found",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: Could not find a cached consent domain",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 8199,  

"Message" : "work thread: Changing URL to: https://dc3.pin.com/my/v1/servicediscovery?service=https://dc3.pin.com/\_wmcs/licensing",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : "9487B57F-9230-42AD-A27B-90D6EB27A02C"  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 20999,  

"Message" : "work thread: Secure clock file was updated successfully.",  

"ScenarioId" : "",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 20999,  

"Message" : "work thread: Proceeding to request authorization, if necessary",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : "8EAD35F5-E94B-4DE8-989A-2D7FC805BF9C"  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: __102+[MSAuthInfo authInfoWithIdentityStoreKey:asyncControl:contextLogger:consentCallback:completionBlock:]_block_invoke completion block is called. [line 186]",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: authInfoWithEmail result: authorizationServer: https://adfs-svc.pin.com/adfs/oauth2/authorize, resource: api.rms.rest.com",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: __93+[MSAuthInfo authInfoWithPublishLicense:userId:asyncControl:consentCallback:completionBlock:]_block_invoke.60 completion block is called. [line 95]",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: Got challenge for URL in PL. Requesting access token ....",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: Error: while getting the userPolicy for PL",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: -[DiagnosticsManager tryToSendLogsToServiceWithError:contextLogger:completionBlock:] completion block is called. [line 64]",  

"ScenarioId" : "",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},{  

"TraceLevel" : "INFO",  

"ThreadId" : 775,  

"Message" : "main thread: __117+[MSUserPolicy userPolicyWithSerializedPolicy:userId:authenticationCallback:consentCallback:options:completionBlock:]_block_invoke completion block is called. [line 102]",  

"ScenarioId" : "7EEC4B5B-21A3-4B94-9030-73F77BF4C82E",  

"Timestamp" : "2020-10-31T09:30:00",  

"CorrelationId" : ""  

},  

Can someone help me figure this out? I've been doing this for weeks... still dk what's wrong...

## Answers

_No answers on this thread._
