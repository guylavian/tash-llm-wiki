---
title: "Exchange Online Powershell BasicAuthToOAuth not working with WSManConnectionInfo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1012161/exchange-online-powershell-basicauthtooauth-not-wo
question_id: 1012161
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online Powershell BasicAuthToOAuth not working with WSManConnectionInfo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1012161/exchange-online-powershell-basicauthtooauth-not-wo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our code currently uses WSManConnectionInfo class to connect to O365. We use basic auth and are trying to upgrade to modern auth. I turned off basic auth in my tenant. Following this guide here, https://www.michev.info/Blog/Post/2997/connecting-to-exchange-online-powershell-via-client-secret-fl..., I am able to connect successfully in PowerShell by getting an access token and using New-PSSession cmdlet. I use the following commands:    

```
Add-Type -Path 'C:\Program Files\WindowsPowerShell\Modules\AzureAD\2.0.2.140\Microsoft.IdentityModel.Clients.ActiveDirectory.dll'  
   
$authContext45 = New-Object "Microsoft.IdentityModel.Clients.ActiveDirectory.AuthenticationContext" -ArgumentList " https://login.windows.net/mytenant.onmicrosoft.com"  
$secret = Get-ChildItem cert://localmachine/my/thumbprint  
$CAC = [Microsoft.IdentityModel.Clients.ActiveDirectory.ClientAssertionCertificate]::new(appId,$secret)  
$authenticationResult = $authContext45.AcquireTokenAsync("https://outlook.office365.com",$CAC)  
  
$token = $authenticationResult.Result.AccessToken  
$Authorization = "Bearer {0}" -f $Token  
$Password = ConvertTo-SecureString -AsPlainText $Authorization -Force  
$Ctoken = New-Object System.Management.Automation.PSCredential -ArgumentList "OAuthUser@tenantGUID",$Password  
   
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/PowerShell-LiveId?BasicAuthToOAuthConversion=true -Credential
```

 $Ctoken -Authentication Basic -AllowRedirection -Verbose    

    Import-PSSession $Session  

However, when I try to use C# WSManConnectionInfo to do the same thing, I get this strange error whenever I try to open the runspace:    

System.Management.Automation.Remoting.PSRemotingTransportException HResult=0x80131501 Message=Connecting to remote server outlook.office365.com failed with the following error message : The WS-Management service cannot process the request. Cannot find the https://schemas.microsoft.com/powershell/Microsoft.Exchange session configuration in the WSMan: drive on the outlook.office365.com computer. For more information, see the about_Remote_Troubleshooting Help topic. Here is the code:    

```
public static Collection  GetUsersUsingOAuthPublic() {  
      var authContext = new AuthenticationContext("https://login.windows.net/mytenant.onmicrosoft.com");  
      X509Store certStore = new X509Store(StoreName.My, StoreLocation.LocalMachine);  
  
      certStore.Open(OpenFlags.ReadOnly);  
      X509Certificate2Collection certCollection = certStore.Certificates.Find(X509FindType.FindByThumbprint, certThumbprint, false);  
      certStore.Close();  
      var cac = new ClientAssertionCertificate(appId, certCollection[0]);  
      var authResult = authContext.AcquireTokenAsync("https://outlook.office365.com", cac);  
  
      var token = authResult.Result.AccessToken;  
      string auth = string.Format("Bearer {0}", token);  
      System.Security.SecureString password = new System.Security.SecureString();  
  
      foreach(char c in auth) {  
        password.AppendChar(c);  
      }  
  
      PSCredential psCredential = new PSCredential(string.Format("OAuthUser@{0}", tenantId), password);  
  
      WSManConnectionInfo connectionInfo = new WSManConnectionInfo(  
        new Uri("https://outlook.office365.com/powershell-liveid?BasicAuthToOAuthConversion=true"),  
        "https://schemas.microsoft.com/powershell/Microsoft.Exchange",  
        psCredential  
      );  
      connectionInfo.AuthenticationMechanism = AuthenticationMechanism.Basic;  
      connectionInfo.SkipCACheck = true;  
      connectionInfo.SkipCNCheck = true;  
  
      using(Runspace runspace = RunspaceFactory.CreateRunspace(connectionInfo)) {  
        return GetUserInformation(10, runspace);  
      }  
    }
```

I open the runspace like so:    

```
public static Collection  GetUserInformation(int count, Runspace runspace) {  
    using(PowerShell powershell = PowerShell.Create()) {  
      powershell.AddCommand("Get-Users");  
      powershell.AddParameter("ResultSize", count);  
      runspace.Open();  
      powershell.Runspace = runspace;  
      return powershell.Invoke();  
    }  
  }
```

An image of the exception:

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-17*

Why aren't you using the V2 module, which supports OAuth via CBA by default? https://learn.microsoft.com/en-us/powershell/exchange/app-only-auth-powershell-v2?view=exchange-ps    

Or even better, the V3 approach that removes the dependency on WinRM/WSMan altogether? https://www.michev.info/Blog/Post/3883/exchange-online-powershell-module-gets-rid-of-the-winrm-dependence    

Scroll down to the second part of the article to see how you can use the same method without even needing PowerShell.
