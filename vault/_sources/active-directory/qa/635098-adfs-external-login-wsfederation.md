---
title: "ADFS / external login / WsFederation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/635098/adfs-external-login-wsfederation
question_id: 635098
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-aspnet-core-other-l1", "developer-technologies-csharp", "microsoft-security-security-active-directory-federation-services"]
---
# ADFS / external login / WsFederation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/635098/adfs-external-login-wsfederation (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to login against ADFS 2016 using WsFederation in a ASP.NET Core Web App / c# . The application is redirecting correct to the to external login page and I am getting redirected back ok. But "GetExternalLoginInfoAsync()” does just return null whatever I do so I am stuck. Is there anyone can help to point out what to change / what I am missing or doing wrong. The relevant code s below.

```
public void ConfigureServices(IServiceCollection services)
{
  String connectionString = GetSqlServerConnectionString();

  services.AddMvc();
  services.AddSession(); // add session

  services.AddDbContext(options =>
    options.UseSqlServer(connectionString));

  services.AddDefaultIdentity(options => 
    options.SignIn.RequireConfirmedAccount = true)
       .AddEntityFrameworkStores();

  services.AddAuthentication().AddWsFederation(options =>
  {
    options.MetadataAddress = "https://..removed..";
    options.Wtrealm = "https://..removed..";
    options.Wreply = "https://..removed..";
  });

  services.AddControllersWithViews();
 }

public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
  if (env.IsDevelopment())
  {
    app.UseDeveloperExceptionPage();
  }
  else
  {
   app.UseExceptionHandler("/Home/Error");
   app.UseHsts();
  }
  app.UseHttpsRedirection();
  app.UseStaticFiles();
  app.UseRouting();
  app.UseAuthentication();
  app.UseAuthorization();
  app.UseSession();

  app.UseEndpoints(endpoints =>
  {
    endpoints.MapControllerRoute(
      name: "default",
      pattern: "{controller=Home}/{action=Index}/{id?}");
  });
```

}

```
public AuthenticationController(SignInManager signInManager)
{
  _signInManager = signInManager;
}

[HttpGet]
public IActionResult Get()
{
  var provider = "WsFederation";
  var redirectUrl = "..removed....";
  var properties = _signInManager.ConfigureExternalAuthenticationProperties(provider, redirectUrl);
  return Challenge(properties, provider);
}
```

```
public AdfsCallbackController(SignInManager signInManager)
{
  _signInManager = signInManager;
}

[HttpPost]
public async Task CallbackAsync()
{
  var info = await _signInManager.GetExternalLoginInfoAsync();

  if (info == null)
  {
    SLog.AddMessage("AdfsControllers.Post", "info is null", 5);
  }
  else
  {
    SLog.AddMessage("AdfsControllers.Post", info.ToString(), 5);
  }
    return base.Content("Hello", "text/html");
}
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-24*

Hi, @Anonymous      

First what is returned from the server looks ok - I can se my name in the information when that claim is added i ADFS.     

I have found some more things! The reason for info being null is most likely the following:    

"By default, the new middleware: Doesn't check every form post for sign-in messages. Only requests to the CallbackPath are checked for sign-ins. CallbackPath defaults to /signin-wsfed but can be changed via the inherited"    

So I changed it by adding: options.CallbackPath = "/adfscallback";    

But now I am getting the following error instead:    

System.Exception: An error was encountered while handling the remote login.    

 ---> System.Exception: No message.    

   --- End of inner exception stack trace ---    

   at Microsoft.AspNetCore.Authentication.RemoteAuthenticationHandler`1.HandleRequestAsync()    

   at Microsoft.AspNetCore.Authentication.AuthenticationMiddleware.Invoke(HttpContext context)    

   at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)    

So now I stuck in the middelware :(.    

Any suggestions about this?    

Med vänlig hälsning    

Carl-Johan
