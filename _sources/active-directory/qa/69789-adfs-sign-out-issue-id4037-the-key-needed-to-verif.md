---
title: "ADFS Sign Out Issue ID4037: The key needed to verify the signature could not be resolved from the following security key identifier"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/69789/adfs-sign-out-issue-id4037-the-key-needed-to-verif
question_id: 69789
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Sign Out Issue ID4037: The key needed to verify the signature could not be resolved from the following security key identifier

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/69789/adfs-sign-out-issue-id4037-the-key-needed-to-verif (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a homegrown webapp A and a 3rd party webapp B. Both are relying parties within our on-prem ADFS 4.0 server on a Windows 2019 Datacenter.  

Webapp A uses WS-Federation and webapp B probably uses SAML 2.0 but not 100% sure. Webapp A has no signature certificate. Webapp B has a valid signature certificate.  

A user can sign into webapp A and webapp B and sign out without any issues as long as this occurs in different browser sessions.  

But if users are in webapp A and open another browser tab to go to webapp B, and try to sign out from webapp A, they get an error "MSIS7054: The SAML logout did not complete properly."  

And ADFS Event Viewer shows the below exception:  

The Federation Service encountered an error while processing the SAML authentication request.   

Additional Data   

Exception details:   

Microsoft.IdentityModel.Protocols.XmlSignature.SignatureVerificationFailedException: ID4037: The key needed to verify the signature could not be resolved from the following security key identifier 'SecurityKeyIdentifier  

    (  

    IsReadOnly = False,  

    Count = 1,  

    Clause[0] = Microsoft.IdentityServer.Tokens.MSISSecurityKeyIdentifierClause  

    )  

'. Ensure that the SecurityTokenResolver is populated with the required key.  

   at Microsoft.IdentityModel.Protocols.XmlSignature.EnvelopedSignatureReader.ResolveSigningCredentials()  

   at Microsoft.IdentityModel.Protocols.XmlSignature.EnvelopedSignatureReader.OnEndOfRootElement()  

   at Microsoft.IdentityModel.Protocols.XmlSignature.EnvelopedSignatureReader.Read()  

   at System.Xml.XmlReader.ReadEndElement()  

   at Microsoft.IdentityServer.Protocols.Saml.SamlProtocolSerializer.ReadLogoutRequest(XmlReader reader)  

   at Microsoft.IdentityServer.Protocols.Saml.HttpSamlBindingSerializer.ReadProtocolMessage(String encodedSamlMessage)  

   at Microsoft.IdentityServer.Protocols.Saml.Contract.SamlContractUtility.CreateSamlMessage(MSISSamlBindingMessage message)  

   at Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolManager.Logout(HttpSamlMessage logoutMessage, String sessionState, String logoutState, Boolean partialLogout, Boolean isUrlTranslationNeeded, HttpSamlMessage& newLogoutMessage, String& newSessionState, String& newLogoutState, Boolean& validLogoutRequest)  

Webapp A is a dotnet core MVC app. Here is the sign out code:  

```
[Authorize]
public async Task SignOut()
{
    //redirect to /signoutcallback after signout
    await SignOutCustom("/signoutcallback");
}

[Authorize]
public async Task SignOutCustom(string redirectUri)
{
    await HttpContext.SignOutAsync("Cookies");
    var prop = new AuthenticationProperties { RedirectUri = redirectUri };

    //redirect to provided target
    await HttpContext.SignOutAsync("WsFederation", prop);
}

[AllowAnonymous]
public ActionResult SignOutCallback()
{
    if (User.Identity.IsAuthenticated)
    {
        // Redirect to home page if the user is authenticated.
        return RedirectToAction("Index", "Home");
    }

    return View();
}
```

## Answers

_No answers on this thread._
