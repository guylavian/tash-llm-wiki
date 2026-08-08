---
title: "Chapter 3. Themes - Red Hat build of Keycloak 26.2 Server Developer Guide"
type: reference
domain: keycloak
slug: rhbk-26-2-themes
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.2/html/server_developer_guide/themes
guide: server_developer_guide
version: 26.2
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Red Hat build of Keycloak provides theme support for web pages and emails. This allows customizing the look and feel of end-user facing pages so they can be integrated with your applications. Figure 3.1. Login page with sunrise example theme 3.1. Theme types A theme can provide one or more types to customize different aspects of Red Hat build of Keycloak. The types available are: Account - Account…"
---

# Chapter 3. Themes - Red Hat build of Keycloak 26.2 Server Developer Guide

Chapter 3. Themes
Red Hat build of Keycloak provides theme support for web pages and emails. This allows customizing the look and feel of end-user facing pages so they can be integrated with your applications.
Figure 3.1. Login page with sunrise example theme
3.1. Theme types
A theme can provide one or more types to customize different aspects of Red Hat build of Keycloak. The types available are:
- Account - Account Console
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
Change the welcome theme by using the
spi-theme-welcome-theme
option. For example:
bin/kc.[sh|bat] start --spi-theme-welcome-theme=custom-theme
3.3. Default themes
Red Hat build of Keycloak comes bundled with default themes in the JAR file keycloak-themes-26.2.15.redhat-00001.jar
inside the server distribution. The server’s root themes
directory does not contain any themes by default, but it contains a README file with some additional details about the default themes. To simplify upgrading, do not edit the bundled themes directly. Instead create your own theme that extends one of the bundled themes.
3.4. Creating a theme
A theme consists of:
- HTML templates (Freemarker Templates)
- Images
- Message bundles
- Stylesheets
- Scripts
- Theme properties
Unless you plan to replace every single page you should extend another theme. Most likely you will want to extend some existing theme. Alternatively, if you intend to provide your own implementation of the admin or account console, consider extending the base
theme. The base
theme consists of a message bundle and therefore such implementation needs to start from scratch, including implementation of the main index.ftl
Freemarker template, but it can leverage existing translations from the message bundle.
When extending a theme you can override individual resources (templates, stylesheets, etc.). If you decide to override HTML templates bear in mind that you may need to update your custom template when upgrading to a new release.
While creating a theme it’s a good idea to disable caching as this makes it possible to edit theme resources directly from the themes
directory without restarting Red Hat build of Keycloak.
Procedure
Run Keycloak with the following options:
bin/kc.[sh|bat] start --spi-theme-static-max-age=-1 --spi-theme-cache-themes=false --spi-theme-cache-templates=false
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
to extend thebase
theme and import some common resources, create the filethemes/mytheme/login/theme.properties
with following contents:parent=base import=common/keycloak
You have now created a theme with support for the login type.
- Log into the Admin Console to check out your new theme
- Select your realm
- Click Realm Settings from the menu.
- Click on the Themes tab.
- For Login Theme select mytheme and click Save.
Open the login page for the realm.
You can do this either by logging in through your application or by opening the Account Console (
/realms/{realm-name}/account
).-
To see the effect of changing the parent theme, set
parent=keycloak
intheme.properties
and refresh the login page.
Be sure to re-enable caching in production as it will significantly impact performance.
If you want to manually delete the content of the themes cache, you can do so by deleting the data/tmp/kc-gzip-cache
directory of the server distribution. It can be useful for instance if you redeployed custom providers or custom themes without disabling themes caching in the previous server executions.
3.4.1. Theme properties
Theme properties are set in the file <THEME TYPE>/theme.properties
in the theme directory.
- parent - Parent theme to extend
- import - Import resources from another theme
-
common - Override the common resource path. The default value is
common/keycloak
when not specified. This value would be used as value of suffix of${url.resourcesCommonPath}
, which is used typically in freemarker templates (prefix of${url.resoucesCommonPath}
value is theme root uri). - styles - Space-separated list of styles to include
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
to:styles=css/login.css css/styles.css
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
<img src="${url.resourcesPath}/img/image.jpg" alt="My image description">
3.4.6. Adding an image to an email theme
To make images available to the theme add them to the <THEME TYPE>/email/resources/img
directory of your theme. These can be used from within directly in HTML templates.
For example to add an image to the mytheme
copy an image to themes/mytheme/email/resources/img/logo.jpg
.
To use directly in HTML templates add the following to a custom HTML template:
<img src="${url.resourcesUrl}/img/image.jpg" alt="My image description">
3.4.7. Messages
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
3.4.8. Adding a language to a realm
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
By default, message properties files should be encoded using UTF-8. Keycloak falls back to ISO-8859-1 handling if it can’t read the contents as UTF-8. Unicode characters can be escaped as described in Java’s documentation for PropertyResourceBundle. Previous versions of Keycloak supported specifying the encoding in the first line with a comment like # encoding: UTF-8
, which is no longer supported.
3.4.9. Adding custom Identity Providers icons
Red Hat build of Keycloak supports adding icons for custom Identity providers, which are displayed on the login screen.
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
All icons are available on the official website of PatternFly4. Icons for social providers are already defined in base
login theme properties (themes/keycloak/login/theme.properties
), where you can inspire yourself.
3.4.10. Creating a custom HTML template
Red Hat build of Keycloak uses Apache Freemarker templates to generate HTML and render pages.
Although it is possible to create custom templates to change completely how pages are rendered, the recommendation is to leverage the built-in templates as much as possible. The reasons are:
- During upgrades, you might be forced to update your custom templates to get the latest updates from newer versions
- Configuring CSS styles to your themes allows you to adapt the UI to match your UI design standards and guidelines.
- User Profile allows you to support custom user attributes and configure how they are rendered.
In most cases, you won’t need to change templates to adapt Red Hat build of Keycloak to your needs, but you can override individual templates in your own theme by creating <THEME TYPE>/<TEMPLATE>.ftl
. Admin and account console use a single template index.ftl
for rendering the application.
For a list of templates in other theme types look at the theme/base/<THEME_TYPE>
directory in the JAR file at $KEYCLOAK_HOME/lib/lib/main/org.keycloak.keycloak-themes-<VERSION>.jar
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
- Back up the modified template. When upgrading to a new version of Red Hat build of Keycloak you may need to update your custom templates to apply changes to the original template if applicable.
3.4.11. Emails
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
Themes can be deployed to Red Hat build of Keycloak by copying the theme directory to themes
or it can be deployed as an archive. During development you can copy the theme to the themes
directory, but in production you may want to consider using an archive
. An archive
makes it simpler to have a versioned copy of the theme, especially when you have multiple instances of Red Hat build of Keycloak for example with clustering.
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
To deploy the archive to Red Hat build of Keycloak, add it to the providers/
directory of Red Hat build of Keycloak and restart the server if it is already running.
