---
title: "Chapter 3. Themes - Red Hat Single Sign-On 7.5 Server Developer Guide"
type: reference
domain: keycloak
slug: rhsso-7-5-themes
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.5/html/server_developer_guide/themes
guide: server_developer_guide
version: 7.5
family: rhsso
documentKind: "Documentation"
abstract: "Red Hat Single Sign-On provides theme support for web pages and emails. This allows customizing the look and feel of end-user facing pages so they can be integrated with your applications. Figure 3.1. Login page with sunrise example theme 3.1. Theme types A theme can provide one or more types to customize different aspects of Red Hat Single Sign-On. The types available are: Account - Account manag…"
---

# Chapter 3. Themes - Red Hat Single Sign-On 7.5 Server Developer Guide

Chapter 3. Themes
Red Hat Single Sign-On provides theme support for web pages and emails. This allows customizing the look and feel of end-user facing pages so they can be integrated with your applications.
Figure 3.1. Login page with sunrise example theme
3.1. Theme types
A theme can provide one or more types to customize different aspects of Red Hat Single Sign-On. The types available are:
- Account - Account management
- Admin - Admin Console
- Email - Emails
- Login - Login forms
- Welcome - Welcome page
3.2. Configuring a theme
All theme types, except welcome, are configured through the Admin Console.
Procedure
- Log into the Admin Console.
- Select your realm from the drop-down box in the top left corner.
- Click Realm Settings from the menu.
Click the Themes tab.
NoteTo set the theme for the
master
Admin Console you need to set the Admin Console theme for themaster
realm.- To see the changes to the Admin Console refresh the page.
-
Change the welcome theme by editing
standalone.xml
,standalone-ha.xml
, ordomain.xml
. Add
welcomeTheme
to the theme element, for example:<theme> ... <welcomeTheme>custom-theme</welcomeTheme> ... </theme>
- Restart the server for the changes to the welcome theme to take effect.
3.3. Default themes
Red Hat Single Sign-On comes bundled with default themes in the server’s root themes
directory. To simplify upgrading you should not edit the bundled themes directly. Instead create your own theme that extends one of the bundled themes.
3.4. Creating a theme
A theme consists of:
- HTML templates (Freemarker Templates)
- Images
- Message bundles
- Stylesheets
- Scripts
- Theme properties
Unless you plan to replace every single page you should extend another theme. Most likely you will want to extend the Red Hat Single Sign-On theme, but you could also consider extending the base theme if you are significantly changing the look and feel of the pages. The base theme primarily consists of HTML templates and message bundles, while the Red Hat Single Sign-On theme primarily contains images and stylesheets.
When extending a theme you can override individual resources (templates, stylesheets, etc.). If you decide to override HTML templates bear in mind that you may need to update your custom template when upgrading to a new release.
While creating a theme it’s a good idea to disable caching as this makes it possible to edit theme resources directly from the themes
directory without restarting Red Hat Single Sign-On.
Procedure
-
Edit
standalone.xml
. For
theme
setstaticMaxAge
to-1
and bothcacheTemplates
andcacheThemes
tofalse
:<theme> <staticMaxAge>-1</staticMaxAge> <cacheThemes>false</cacheThemes> <cacheTemplates>false</cacheTemplates> ... </theme>
NoteBe sure to re-enable caching in production as it will significantly impact performance.
Create a directory in the
themes
directory.The name of the directory becomes the name of the theme. For example to create a theme called
mytheme
create the directorythemes/mytheme
.Inside the theme directory, create a directory for each of the types your theme is going to provide.
For example, to add the login type to the
mytheme
theme, create the directorythemes/mytheme/login
.For each type create a file
theme.properties
which allows setting some configuration for the theme.For example, to configure the theme
themes/mytheme/login
to extend the base theme and import some common resources, create the filethemes/mytheme/login/theme.properties
with following contents:parent=base import=common/keycloak
You have now created a theme with support for the login type.
- Log into the Admin Console to checkout your new theme
- Select your realm
- Click Realm Settings from the menu.
- Click on the Themes tab.
- For Login Theme select mytheme and click Save.
Open the login page for the realm.
You can do this either by logging in through your application or by opening the Account Management console (
/realms/{realm name}/account
).-
To see the effect of changing the parent theme, set
parent=keycloak
intheme.properties
and refresh the login page.
3.4.1. Theme properties
Theme properties are set in the file <THEME TYPE>/theme.properties
in the theme directory.
- parent - Parent theme to extend
- import - Import resources from another theme
- styles - Space-separated list of styles to include
- locales - Comma-separated list of supported locales
There are a list of properties that can be used to change the css class used for certain element types. For a list of these properties look at the theme.properties file in the corresponding type of the keycloak theme (themes/keycloak/<THEME TYPE>/theme.properties
).
You can also add your own custom properties and use them from custom templates.
When doing so, you can substitute system properties or environment variables by using these formats:
-
${some.system.property}
- for system properties -
${env.ENV_VAR}
- for environment variables.
A default value can also be provided in case the system property or the environment variable is not found with ${foo:defaultValue}
.
If no default value is provided and there’s no corresponding system property or environment variable, then nothing is replaced and you end up with the format in your template.
Here’s an example of what is possible:
javaVersion=${java.version}
unixHome=${env.HOME:Unix home not found}
windowsHome=${env.HOMEPATH:Windows home not found}
3.4.2. Add a stylesheet to a theme
You can add one or more stylesheets to a theme.
Procedure
-
Create a file in the
<THEME TYPE>/resources/css
directory of your theme. Add this file to the
styles
property intheme.properties
.For example, to add
styles.css
to themytheme
, createthemes/mytheme/login/resources/css/styles.css
with the following content:.login-pf body { background: DimGrey none; }
Edit
themes/mytheme/login/theme.properties
and add:styles=css/styles.css
To see the changes, open the login page for your realm.
You will notice that the only styles being applied are those from your custom stylesheet.
To include the styles from the parent theme, load the styles from that theme. Edit
themes/mytheme/login/theme.properties
and changestyles
to:styles=web_modules/@fortawesome/fontawesome-free/css/icons/all.css web_modules/@patternfly/react-core/dist/styles/base.css web_modules/@patternfly/react-core/dist/styles/app.css node_modules/patternfly/dist/css/patternfly.min.css node_modules/patternfly/dist/css/patternfly-additions.min.css css/login.css css/styles.css
NoteTo override styles from the parent stylesheets, ensure that your stylesheet is listed last.
3.4.3. Adding a script to a theme
You can add one or more scripts to a theme.
Procedure
-
Create a file in the
<THEME TYPE>/resources/js
directory of your theme. Add the file to the
scripts
property intheme.properties
.For example, to add
script.js
to themytheme
, createthemes/mytheme/login/resources/js/script.js
with the following content:alert('Hello');
Then edit
themes/mytheme/login/theme.properties
and add:scripts=js/script.js
3.4.4. Adding an image to a theme
To make images available to the theme add them to the <THEME TYPE>/resources/img
directory of your theme. These can be used from within stylesheets or directly in HTML templates.
For example to add an image to the mytheme
copy an image to themes/mytheme/login/resources/img/image.jpg
.
You can then use this image from within a custom stylesheet with:
body {
background-image: url('../img/image.jpg');
background-size: cover;
}
Or to use directly in HTML templates add the following to a custom HTML template:
<img src="${url.resourcesPath}/img/image.jpg">
3.4.5. Messages
Text in the templates is loaded from message bundles. A theme that extends another theme will inherit all messages from the parent’s message bundle and you can override individual messages by adding <THEME TYPE>/messages/messages_en.properties
to your theme.
For example to replace Username
on the login form with Your Username
for the mytheme
create the file themes/mytheme/login/messages/messages_en.properties
with the following content:
usernameOrEmail=Your Username
Within a message values like {0}
and {1}
are replaced with arguments when the message is used. For example {0} in Log in to {0}
is replaced with the name of the realm.
Texts of these message bundles can be overwritten by realm-specific values. The realm-specific values are manageable via UI and API.
3.4.6. Adding a language to a realm
Prerequisites
- To enable internationalization for a realm, see the Server Administration Guide.
Procedure
-
Create the file
<THEME TYPE>/messages/messages_<LOCALE>.properties
in the directory of your theme. Add this file to the
locales
property in<THEME TYPE>/theme.properties
. For a language to be available to users the realmslogin
,account
andemail
, the theme has to support the language, so you need to add your language for those theme types.For example, to add Norwegian translations to the
mytheme
theme create the filethemes/mytheme/login/messages/messages_no.properties
with the following content:usernameOrEmail=Brukernavn password=Passord
If you omit a translation for messages, they will use English.
Edit
themes/mytheme/login/theme.properties
and add:locales=en,no
-
Add the same for the
account
andemail
theme types. To do this createthemes/mytheme/account/messages/messages_no.properties
andthemes/mytheme/email/messages/messages_no.properties
. Leaving these files empty will result in the English messages being used. -
Copy
themes/mytheme/login/theme.properties
tothemes/mytheme/account/theme.properties
andthemes/mytheme/email/theme.properties
. Add a translation for the language selector. This is done by adding a message to the English translation. To do this add the following to
themes/mytheme/account/messages/messages_en.properties
andthemes/mytheme/login/messages/messages_en.properties
:locale_no=Norsk
By default message properties files should be encoded using ISO-8859-1. It’s also possible to specify the encoding using a special header. For example to use UTF-8 encoding:
# encoding: UTF-8 usernameOrEmail=....
3.4.7. Adding custom Identity Providers icons
Red Hat Single Sign-On supports adding icons for custom Identity providers, which are displayed on the login screen.
Procedure
-
Define icon classes in your login
theme.properties
file (for example,themes/mytheme/login/theme.properties
) with key patternkcLogoIdP-<alias>
. For an Identity Provider with an alias
myProvider
, you may add a line totheme.properties
file of your custom theme. For example:kcLogoIdP-myProvider = fa fa-lock
All icons are available on the official website of PatternFly4. Icons for social providers are already defined in base login theme properties (themes/keycloak/login/theme.properties
), where you can inspire yourself.
3.4.8. Creating a custom HTML template
Red Hat Single Sign-On uses Apache Freemarker templates to generate HTML. You can override individual templates in your own theme by creating <THEME TYPE>/<TEMPLATE>.ftl
. For a list of templates used see themes/base/<THEME TYPE>
.
Procedure
- Copy the template from the base theme to your own theme.
Apply the modifications you need.
For example, to create a custom login form for the
mytheme
theme, copythemes/base/login/login.ftl
tothemes/mytheme/login
and open it in an editor.After the first line (<#import …>), add
<h1>HELLO WORLD!</h1>
as shown here:<#import "template.ftl" as layout> <h1>HELLO WORLD!</h1> ...
- Back up the modified template. When upgrading to a new version of Red Hat Single Sign-On you may need to update your custom templates to apply changes to the original template if applicable.
3.4.9. Emails
To edit the subject and contents for emails, for example password recovery email, add a message bundle to the email
type of your theme. There are three messages for each email. One for the subject, one for the plain text body and one for the html body.
To see all emails available take a look at themes/base/email/messages/messages_en.properties
.
For example to change the password recovery email for the mytheme
theme create themes/mytheme/email/messages/messages_en.properties
with the following content:
passwordResetSubject=My password recovery
passwordResetBody=Reset password link: {0}
passwordResetBodyHtml=<a href="{0}">Reset password</a>
3.5. Deploying themes
Themes can be deployed to Red Hat Single Sign-On by copying the theme directory to themes
or it can be deployed as an archive. During development you can copy the theme to the themes
directory, but in production you may want to consider using an archive
. An archive
makes it simpler to have a versioned copy of the theme, especially when you have multiple instances of Red Hat Single Sign-On for example with clustering.
Procedure
- To deploy a theme as an archive, create a JAR archive with the theme resources.
Add a file
META-INF/keycloak-themes.json
to the archive that lists the available themes in the archive as well as what types each theme provides.For example for the
mytheme
theme createmytheme.jar
with the contents:- META-INF/keycloak-themes.json
- theme/mytheme/login/theme.properties
- theme/mytheme/login/login.ftl
- theme/mytheme/login/resources/css/styles.css
- theme/mytheme/login/resources/img/image.png
- theme/mytheme/login/messages/messages_en.properties
theme/mytheme/email/messages/messages_en.properties
The contents of
META-INF/keycloak-themes.json
in this case would be:{ "themes": [{ "name" : "mytheme", "types": [ "login", "email" ] }] }
A single archive can contain multiple themes and each theme can support one or more types.
-
To deploy the archive to Red Hat Single Sign-On, add it to the
standalone/deployments/
directory of Red Hat Single Sign-On and it will be automatically loaded.
3.6. Theme selector
By default the theme configured for the realm is used, with the exception of clients being able to override the login theme. This behavior can be changed through the Theme Selector SPI.
This could be used to select different themes for desktop and mobile devices by looking at the user agent header, for example.
To create a custom theme selector you need to implement ThemeSelectorProviderFactory
and ThemeSelectorProvider
.
3.7. Theme resources
When implementing custom providers in Red Hat Single Sign-On there may often be a need to add additional templates, resources and messages bundles.
The easiest way to load additional theme resources is to create a JAR with templates in theme-resources/templates
resources in theme-resources/resources
and messages bundles in theme-resources/messages
and drop it into the standalone/deployments/
directory of Red Hat Single Sign-On.
If you want a more flexible way to load templates and resources that can be achieved through the ThemeResourceSPI. By implementing ThemeResourceProviderFactory
and ThemeResourceProvider
you can decide exactly how to load templates and resources.
3.8. Locale selector
By default, the locale is selected using the DefaultLocaleSelectorProvider
which implements the LocaleSelectorProvider
interface. English is the default language when internationalization is disabled. With internationalization enabled, the locale is resolved according to the logic described in the Server Administration Guide.
This behaviour can be changed through the LocaleSelectorSPI
by implementing the LocaleSelectorProvider
and LocaleSelectorProviderFactory
.
The LocaleSelectorProvider
interface has a single method, resolveLocale
, which must return a locale given a RealmModel
and a nullable UserModel
. The actual request is available from the KeycloakSession#getContext
method.
Custom implementations can extend the DefaultLocaleSelectorProvider
in order to reuse parts of the default behavior. For example to ignore the Accept-Language
request header, a custom implementation could extend the default provider, override it’s getAcceptLanguageHeaderLocale
, and return a null value. As a result the locale selection will fall back on the realms’s default language.
