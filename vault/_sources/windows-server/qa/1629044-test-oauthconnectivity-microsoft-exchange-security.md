---
title: "Test-OAuthConnectivity  Microsoft.Exchange.Security.OAuth.ValidationResultNodeId"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1629044/test-oauthconnectivity-microsoft-exchange-security
question_id: 1629044
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
---
# Test-OAuthConnectivity  Microsoft.Exchange.Security.OAuth.ValidationResultNodeId

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1629044/test-oauthconnectivity-microsoft-exchange-security (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

`your text`Hello,

Im trying for my exchange online tenant and exchange on-prem to connect but i get following error:

C:\Windows\System32>Test-OAuthConnectivity -Service EWS -TargetUri https://partner.outlook.cn/ews/exchange.asmx -Mailbox <mailbox> -Verbose | fl

RunspaceId  : 5db5f805-524c-4736-affd-559c08764bbc
Task        : Comprobando llamada API EWS en Oauth
Detail      : La configuración se cargó correctamente a las 01/01/0001 0:00:00 UTC. Esto sucedió hace 1064113542
              minutos.
              Se está borrando la caché del token porque "usar token de caché" se estableció en false.
              Registro Oauth saliente de Exchange:
              Id. de solicitud de cliente: 2b4c5550-886c-4cdb-abc4-aa3f86dac3e5
              Information:[OAuthCredentials:Authenticate] entering
              Information:[OAuthCredentials:Authenticate] challenge from
              'https://partner.outlook.cn/ews/Exchange.asmx' received: Bearer
              client_id="00000002-0000-0ff1-ce00-000000000000",
              trusted_issuers="00000001-0002-0000-c000-000000000000@", token_types="app_asserted_user_v1
              service_asserted_app_v1",
              authorization_uri="https://login.chinacloudapi.cn/common/oauth2/authorize",Basic Realm=""
              Information:[OAuthCredentials:GetToken] client-id: '00000002-0000-0ff1-ce00-000000000000', realm: '',
              trusted_issuer: '00000001-0002-0000-c000-000000000000@'
              Information:[OAuthCredentials:GetToken] Start building a token using organizationId ''
              Information:[OAuthTokenBuilder:GetAppToken] start building the apptoken
              Information:[OAuthTokenBuilder:GetAppToken] checking enabled auth servers
              Information:[OAuthTokenBuilder:GetAppToken] trusted_issuer does NOT include the auth server 'ACS -
              07f001bb-c2be-4be8-bf1a-d8d1e5b069c6' ( having DomainName :
              System.Collections.Generic.List`1[System.String] ):
              00000001-0000-0000-c000-000000000000@088d0fa4-f80c-4793-9180-c43cfea99614,
              Error:[OAuthTokenBuilder:GetAppToken] unable to continue building token; no locally configured issuer
              was in the trusted_issuer list, realm from challenge was also empty. trust_issuers was
              00000001-0002-0000-c000-000000000000@*
              Error:The trusted issuers contained the following entries '00000001-0002-0000-c000-000000000000@*'. None
              of them are configured locally.

```
Exchange detalles de respuesta:
          Mensaje de la respuesta HTTP:
          Excepción:
          System.Net.WebException: Anulada la solicitud: La solicitud fue cancelada. --->
          Microsoft.Exchange.Security.OAuth.OAuthTokenRequestFailedException: The trusted issuers contained the
          following entries '00000001-0002-0000-c000-000000000000@*'. None of them are configured locally.
             en Microsoft.Exchange.Security.OAuth.OAuthTokenBuilder.GetAppToken(String applicationId, String
          destinationHost, String realmFromChallenge, IssuerMetadata[] trustedIssuersFromChallenge, String
          userDomain)
             en Microsoft.Exchange.Security.OAuth.OAuthTokenBuilder.GetAppWithUserToken(String applicationId,
          String destinationHost, String realmFromChallenge, IssuerMetadata[] trustedIssuersFromChallenge, String
          userDomain, ClaimProvider claimProvider)
             en Microsoft.Exchange.Security.OAuth.OAuthCredentials.GetToken(WebRequest webRequest,
          HttpAuthenticationChallenge challengeObject)
             en Microsoft.Exchange.Security.OAuth.OAuthCredentials.Authenticate(String challengeString, WebRequest
          webRequest, Boolean preAuthenticate)
             en System.Net.AuthenticationManagerDefault.Authenticate(String challenge, WebRequest request,
          ICredentials credentials)
             en System.Net.AuthenticationState.AttemptAuthenticate(HttpWebRequest httpWebRequest, ICredentials
          authInfo)
             en System.Net.HttpWebRequest.CheckResubmitForAuth()
             en System.Net.HttpWebRequest.CheckResubmit(Exception& e, Boolean& disableUpload)
             en System.Net.HttpWebRequest.DoSubmitRequestProcessing(Exception& exception)
             en System.Net.HttpWebRequest.ProcessResponse()
             en System.Net.HttpWebRequest.SetResponse(CoreResponseData coreResponseData)
             --- Fin del seguimiento de la pila de la excepción interna ---
             en System.Net.HttpWebRequest.GetResponse()
             en Microsoft.Exchange.Monitoring.TestOAuthConnectivityHelper.SendExchangeOAuthRequest(ADUser user,
          String orgDomain, Uri targetUri, String& diagnosticMessage, Boolean appOnly, Boolean useCachedToken,
          Boolean reloadConfig)
```

ResultType  : Error
Identity    : Microsoft.Exchange.Security.OAuth.ValidationResultNodeId
IsValid     : True
ObjectState : New

## Answers

_No answers on this thread._
