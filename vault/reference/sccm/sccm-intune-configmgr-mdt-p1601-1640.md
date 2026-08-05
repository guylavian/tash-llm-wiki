---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1601-1640"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1601-1640
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1601-1640
family: sccm
documentKind: "doc"
abstract: "XML <Validator <Validator DLL=\"\" Description=\"Must follow a pre-defined pattern\" Type=\"Microsoft.Wizard.Validation.RegEx\" Name=\"NamedPattern\"> <Param Description=\"Enter the message you want displayed when the text in this field doesn't match the pattern:\" Name=\"Message\" DisplayN"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1601-1640

<!-- p.1601 -->

        XML

        <Validator
        <Validator DLL="" Description="Must follow a pre-defined pattern"
        Type="Microsoft.Wizard.Validation.RegEx" Name="NamedPattern">
           <Param Description="Enter the message you want displayed when the
        text in this field doesn't match the pattern:" Name="Message"
        DisplayName="Message"/>
           <Param Description="The name of a pre-defined regular expression
        pattern. Must be Username, ComputerName, or Workgroup"
        Name="NamedPattern" DisplayName="Named Pattern"/>
        </Validator>

        ２ Warning

        All Validator elements should include the Message parameter. Specify all
        other parameters as required by the validator. For example, in the previous
        excerpt, the NamedPattern parameter is used to specify a parameter for the
        name of a predefined regular expression pattern.

   5. Copy the UDI Wizard Designer configuration file created in the previous step to
     the installation_folder\Bin\Config folder (where installation_folder is the folder in
     which you installed MDT).

   6. Copy the DLL for your custom task to the
     installation_folder\Templates\Distribution\Tools\ platform folder (where
     installation_folder is the folder in which you installed MDT and platform is x86 for
     the 32-bit version or x64 is for the 64-bit version).

UDI Wizard Reference

Wizard Page Components
You can use any of several prebuilt components to build your custom pages.

Creating Component Instances
The UDI Wizard uses class factories to create new instances of objects for you. These
factories are registered with a factory registry, using a string as the key to the factory.
For example, the WmiRepository component is identified by the string
"Microsoft.Wizard.WmiRepository," which is available in the IWmiRepository header file
as ID_WmiRepository.

<!-- p.1602 -->

Assuming that you have written your page as a subclass of WizardPageImpl, you can
create a new instance of a WmiRepoistory like this:

  C++

  PWmiRepository pWmi;
  CreateInstance(Container(), ID_WmiRepository, &pWmi);

The CreateInstance function is a type-safe template function for creating new instances
of components. PWmiRepository is a smart pointer, so it handles reference counting for
you.

Creatable Components
There is a set of components that you can register with the registry. The first set of
components is always registered, because the main UDI Wizard executable file provides
it. The other two sets of components are provided in "optional" DLLs. For these
components to be available, the DLL must be listed in the DLLs section of the .config
XML file. Your code does not need to know which executable contains a specific
component.

The list of component IDs for components (the component name is the same as the ID
but without the initial ID_) registered with the factory registry (defined in
OSDSetupWizard) is shown in Table 3.

Table 3. Component IDs

                                                                               ﾉ   Expand table

 ID                            Description

 ID_ACPowerTask                (ITask, IWizardComponent) A preflight task that ensures that your
                               computer is not running on battery alone

 ID_AppDiscoveryTask           (ITask, IWizardComponent) A specialized task for discovering
                               which software items you have installed on your computer

 ID_BackgroundTask             (IBackgroundTask, IWizardComponent) Can be used to run a
                               task on another thread

 ID_CopyFilesTask              (ITask, IWizardComponent) A task to copy one or more files

 ID_FormController             (IFormController) You will most like not need to create an
                               instance yourself, as your page receives its own instance

<!-- p.1603 -->

 ID                              Description

 ID_InvalidCharactersValidator   (IValidator) Ensures that no text field contains characters from a
                                 list provided to the validator

 ID_Logger                       (ILogger) You will most like not need to create an instance
                                 yourself, as your page receives a pointer to the shared instance

 ID_NonEmptyValidator            (IValidator) A validator that ensures that no field is empty

 ID_PasswordValidator            (IValidator) A validator that ensures that no two text fields have
                                 the same content

 ID_Regex                        (IRegEx) Evaluates regular expressions, looking for matches

 ID_RegExValidator               (IValidator) A validator that validates against a regular expression
                                 or a known pattern

 ID_SimpleStringProperties       (IStringProperties, ISimpleStringProperties) Provides a simple
                                 way to send properties to tasks without using XML

 ID_ShellExecuteTask             (ITask, IWizardComponent) Execute an external program

 ID_SummaryBag                   (ISummaryBag) Available indirectly from your page via the Form
                                 method

 ID_TaskManager                  (ITaskManager, IBackgroundCallback, IWizardComponent)
                                 Manages running a set of tasks and the UI

 ID_WmiRepository                (IWmiRepository, IWizardComponent) Allows you to run
                                 Windows Management Instrumentation (WMI) queries

 ID_IXmlDocument                 (IXmlDocument) Provides a façade for reading and writing XML
                                 documents

The defined OSDRefreshWizard.dll, shared pages, and other control components are
shown in Table 4 and Table 5.

Table 4. Directory Controls

                                                                                  ﾉ    Expand table

 ID             Description

 ID_Directory   (IDirectory) A façade for obtaining directory information from the file system

Table 5. Defined SharedPages.dll

<!-- p.1604 -->

                                                                                ﾉ    Expand table

 ID                       Description

 ID_ADHelper              (IADHelper) Provides a façade for a limited set of features in Active
                          Directory® Domain Services (AD DS)

 ID_CpuInfo               (ICpuInfo) Determines whether your CPU is 32 or 64 bit

 ID_DomainJoinValidator   (IDomainJoinValidator) Has some methods for checking whether a set
                          of credentials is allowed to join a domain

 ID_DriveList             (IDriveList, IBindableList, IWizardComponent) Uses WMI to obtain a
                          list of drives on your computer

 ID_WiredNetworkTask      (ITask) A tasks that checks whether you are connected to the network
                          with a hard-wired (instead of wireless) network adapter

Control Components
You interact with the controls on your page through the GetControlWrapper template
function, which provides access to one of the types of components listed in Table 6.

Table 6. Components

                                                                                ﾉ    Expand table

 Dialog control types        Description

 CONTROL_CHECK_BOX           (ICheckBox) A façade for working with check box controls

 CONTROL_COMBO_BOX           (IComboBox) A façade for combo box controls

 CONTROL_GENERIC             (IControl) Allows you to work with most types of controls to
                             control enable and visible state

 CONTROL_LIST_VIEW           (IListView) A façade providing access to the features of a list view
                             control

 CONTROL_PROGRESS_BAR        (IProgressBar) A façade for working with the position of a progress
                             bar control

 CONTROL_RADIO_BUTTON        (IRadioButton) A façade for working with radio button controls

 CONTROL_STATIC_TEXT         (IStaticText) A façade that provides read/write permission to the
                             text of a control, such as a label or text box

 CONTROL_TREE_VIEW           (ItreeView) A façade for working with a tree view control

<!-- p.1605 -->

Image List Component
This component is a façade for an ImageList control on your page. You create an image
list via the IListView or ITreeView interface.

FormController Component
The wizard creates this component for you and passes it to your page. You access it
from your page using the Form method, which the WizardPageImpl base class
implements.

InvalidCharacterValidator Component
This is a type of validator that you can include on a page. The ID is
ID_InvalidCharactersValidator (defined in IValidator.h), which has a text value of
"Microsoft.Wizard.Validation.InvalidChars."

This validator looks for a single property (a Setter element in the .config file) called
InvalidChars, which is a list of characters that are not allowed. It checks the characters in
a text box; if the text contains any characters from this list, the component reports
failure.

NonEmptyValidator Component
This is a type of validator that you can include on a page. The ID is
ID_NonEmptyValidator (defined in IValidator.h), which has a text value of
"Microsoft.Wizard.Validation.NonEmpty."

This validator reports failure if the text box (or any other control that supports
IStaticText) has an empty string value.

PasswordValidator Component

This is a type of validator that you can include on a page. The ID is
ID_PasswordValidator (defined in IValidator.h), which has a text value of
"Microsoft.Wizard.Validation.Password."

This validator works with two different text controls (controls that support IStaticText)
and reports failure if they do not contain the same values. In other words, it fails if the
Password and Confirm Password text boxes do not match.

<!-- p.1606 -->

Because this validator requires two controls, it needs more setup than other validators.
The setup might look something like this:

  C++

  Form()->AddToGroup(IDC_EDIT_PASSWORD, IDC_EDIT_PASSWORD2);
  PValidator pValidator;
  Form()->AddValidator(IDC_EDIT_PASSWORD, ID_PasswordValidator, pMessage,
  &pValidator);
  PStaticText pPassword2;
  GetControlWrapper(View(), IDC_EDIT_PASSWORD2, CONTROL_STATIC_TEXT,
  &pPassword2);
  pValidator->SetProperty(0, pPassword2);

First, you define the Confirm Password control as a "child" of the Password control. That
way, if the form controller disables the Password control, it will also disable the Confirm
Password control. Next, add a password validator to the form. Finally, provide the
password validator with the interface to the Confirm Password control.

Because of the requirement for two controls, you must use code to set up this validator
rather than the .config XML file.

RegExValidator Component
This is a type of validator that you can include on a page. The ID is ID_RegExValidator
(defined in IValidator.h), which has a text value of "Microsoft.Wizard.Validation.RegEx."

This validator compares the contents of a text control (one that supports IStaticText) to
a regular expression and fails if the text does not match the regular expression.

Alternatively, you can use this validator with a predefined named pattern. To use a
regular expression, the XML must contain a setter property called Pattern. If you want to
use a named pattern instead, use a setter called NamedPattern set to one of the values
in Table 7.

Table 7. Named Pattern Setters

                                                                               ﾉ   Expand table

 Pattern          Description

 Username         Verifies that the text is either of the form domain\user or user@domain

 ComputerName     The name must be between 1 and 15 characters long and cannot include a set
                  of characters (such as : and ?)

<!-- p.1607 -->

 Pattern          Description

 Workgroup        The name must be between 1 and 15 characters long and cannot contain a set
                  of characters (such as =, +, and ?)

FactoryRegistry Component
This component keeps track of all class factories and services. It implements the
IFactoryRegistry interface and is available indirectly through your page's Container
method. In addition, the registry loads extension DLLs. After it loads a DLL, the registry
looks for an exported function called RegisterFactories. You must implement this
function and in it register the class factories for your pages, tasks, and validators (and
any other class factories you want to register). Here is an example from the sample
project:

  C++

  extern "C" __declspec(dllexport) void RegisterFactories(IFactoryRegistry
  *factories)
  {
  Register<LocationPageFactory>(ID_LocationPage, factories);
  }

Logger Component
This component is available to your page via the Logger method (implemented by
WizardPageImpl). You use this method to write entries to the log file. The contents of
the log file are useful for diagnosing issues users might have running the UDI Wizard.

PropertyBag Component
The property bag is a container for memory variables. It is available from your page
using Container()->Properties(). Memory variables are useful for passing temporary
data among different pages.

TSVariableBag and TSRepository Components

The TSVariableBag component allows you to read and write task sequence variables. It
keeps the values in memory until the user selects Finish (by default). You can access the
TSVariable bag via the page's TSVariables method (implemented by the

<!-- p.1608 -->

WizardPageImpl base class). These components log all reads and writes of task
sequence variables.

WmiRepository Component

This component provides a façade for working with WMI queries. You can call the
CreateInstance helper function with ID_WmiRepository to obtain an instance of this
component, which supports the IWmiRepository interface. This component returns
result records via the IWmiIterator interface.

Wizard Page Helper Classes
You can create custom UDI wizard pages using built-in helper classes provided with the
UDI SDK. Table 8 lists the helper classes that you can use to create custom wizard pages.

Table 8. Helper Classes

                                                                                    ﾉ   Expand table

 Helper class              Description

 ClassFactoryImpl Class    This is a useful base class for creating a class factory that you can then
                           register with the factory registry.

 Interface Template        Use this template class when you want to build a component that
 Class                     implements more than one interface.

 Path Helper Class         This class provides common file/directory operations.

 Pointer Template Class    This class provides reference counting for lifetime management in COM
                           components. It is important to release interfaces when you are done
                           with them. This template class handles the lifetime automatically.

 PUnknown Class            This class is a smart pointer specifically for the IUnknown interface. For
                           all other interfaces, use the Pointer template class.

 StringUtil Helper Class   This class provides helper methods that make it easier to work with
                           strings.

 SubInterface Template     This base class makes it easier to implement a component that supports
 Class                     an interface that itself inherits from another interface.

 UnknownImpl               This class handles most of the details of creating a COM component.
 Template Class

 WizardComponent           This base class is used for creating components that need access to the

<!-- p.1609 -->

 Helper class            Description

 Template Class          wizard services, such as component creation and logging.

 WizardPageImpl          This base class should be used as the base class for all custom wizard
 Template Class          pages

ClassFactoryImpl Class
This is a useful base class for creating a class factory that you can then register with the
factory registry.

The following is an excerpt from the LocationPage.h file in the sample project to define
the ClassFactoryImpl class.

  C++

  #pragma once

  #include "ClassFactoryImpl.h"

  class LocationPageFactory :public ClassFactoryImpl
  {
  protected:
      IUnknown *CreateNewInstance();
  };

The following is an excerpt from the LocationPage.cpp file in the sample wizard page
used to define the class factory for the page.

  C++

  IUnknown *LocationPageFactory::CreateNewInstance()
  {
      return static_cast<IWizardPage *>(new LocationPage);
  }

Interface Template Class

Use this template class when you want to build a component that implements more
than one interface—for example:

  C++

  classLocationPage :public Interface<IFieldCallback,

<!-- p.1610 -->

  WizardPageImpl<IDD_LOCATION_PAGE>>

This code creates a base class chain that supports both IFieldCalback and the interfaces
that WizardPageImpl supports (which happens to be IWizardPage).

Path Helper Class

This class provides common file/directory operations:

  C++

  static inline std::wstring GetModulePath(HINSTANCE hModule)

It also returns the full path to the .exe or .dll file with the instance handle that you
provide to this method:

  C++

  static inline std::wstring GetModuleFilename(HINSTANCE hModule)

The class returns the full path and file name of the .exe and .dll file with the instance
handle that you provide to this method:

  C++

  static inline std::wstring GetDirectoryName(LPCWSTR fullName)

. . . or just the path while stripping the file name:

  C++

  static inline std::wstring GetFileName(LPCWSTR fullName)

Given a path with a file name, the path helper class returns the file name only:

  C++

  static inline std::wstring Combine(LPCWSTR path, LPCWSTR name)

Finally, the class returns a new string that is the combined path and file name (or
another path).

<!-- p.1611 -->

Pointer Template Class
This class is defined in Pointer.h. Because COM components use reference counting for
lifetime management, it is important that you always release interfaces when you are
done with them. Microsoft provides a template class that handles the lifetime
automatically. For example, if you want a smart pointer for an XML interface, you could
write something like this:

  C++

  Pointer<IXMLDOMNode> pNewChild
  pXmlDom->CreateNode(NODE_ELEMENT, L"MyElement", L"", &pNewChild);

The first line defines the smart pointer. The second line shows retrieving a smart pointer
via another call. The & operator always releases an existing interface if it contains one
and returns the address for the internal pointer. Once you have retrieved a pointer like
this, the Pointer instance calls Release for you when the variable goes out of scope.
Microsoft recommends that you use smart pointers instead of calling AddRef and
Release manually.

In addition, the Pointer smart pointer class calls QueryInterface to retrieve other
interfaces for you. For example, when the factory registry creates a new instance of a
component, it has code like this:

  C++

  PWizardComponent pComp = pUnknown;
  if (pComp != nullptr)
      pComp->SetContainer(m_pContainer);

The first line calls QueryInterface behind the scenes to request the IWizardComponent
interface. The resulting smart pointer will equal nullptr if the component does not
support that interface.

PUnknown Class
This class is a smart pointer specifically for the IUnknown interface. For all other
interfaces, use the Pointer template class.

StringUtil Helper Class

This class is defined in Utilities.h and provides helper methods that make it easier to
work with strings:

<!-- p.1612 -->

     C++

     static inline int CompareIgnore(LPCWSTR first, LPCWSTR second)

This method compares two strings while ignoring case (see Table 9).

Table 9. StringUtil Helper Class

                                                                      ﾉ   Expand table

 Returns                Description

 0                      Strings match, ignoring case

 <0                     First < second

 >0                     First > second

Here is an example:

     C++

     static inline std::wstring Format(LPCWSTR input, int index, LPCWSTR value)
     static inline std::wstring Format(LPCWSTR input, int index, DWORD value)

These methods are a bit like the Microsoft .NET Format methods in the sense that
parameters are in the form of {0}. However, they do not perform any formatting of the
input—just substitution:

     C++

     static inline std::wstring Printf(std::wstring format, I val)
     static inline std::wstring Printf(std::wstring format, I val1, J val2)
     static inline std::wstring Printf(std::wstring format, I val1, J val2, K
     val3)
     static inline std::wstring Printf(std::wstring format, I val1, J val2, K
     val3, L val4)

These are wrappers around the StringCchPrintf that return a wstring so you do not have
to allocate memory for strings or buffers yourself.

SubInterface Template Class

<!-- p.1613 -->

This base class makes it easier to implement a component that supports an interface
that itself inherits from another interface. For example, the ICheckBox interface inherits
from IControl. Here is how this class is used to define the CheckBoxWrapper:

  C++

  classCheckBoxWrapper :public SubInterface<IControl, UnknownImpl<ICheckBox> >

The base interface is the first parameter, while the derived interface is the second
parameter.

UnknownImpl Template Class
This class is defined in UnknownImpl.h and handles most of the details of creating a
COM component. Here is an example of how you would use this base class:

  C++

  classDirectory :public UnknownImpl<IDirectory>

This code defines a class that supports the IDirectory interface.

WizardComponent Template Class

This class is defined in IWizardComponent.h and is a useful base class for creating
components that need access to the wizard services, such as component creation and
logging.

As an example, here is how the CopyFilesTask component is defined:

  C++

  classCopyFilesTask :public WizardComponent<ITask>
  {
      ...

The parameter for this template class is the "main" interface you want to use for your
component, which in the case of tasks is ITask. Using WizardComponent means that
your component supports both the interface your provide (ITask in this example) and
IWizardComponent.

Whenever you use the class factory registry to create a new component, the registry
calls the component's IWizardComponent->SetContainer method to provide your

<!-- p.1614 -->

component access to the wizard services.

WizardPageImpl Template Class
Use this class as the base class for your custom pages—for example:

  C++

  class LocationPage :public WizardPageImpl<IDD_LOCATION_PAGE>

The parameter is the resource ID for your dialog box template.

Wizard Page Interfaces
The UDI Wizard uses interfaces to access the different controls on your page. Within you
page, you use the GetControlWrapper function to retrieve a control wrapper. Here is an
example:

  C++

  PStaticText pFormat;
  GetControlWrapper(View(), IDC_CHECK_PARTITION, CONTROL_STATIC_TEXT,
  &pFormat);

Here, PStaticText is a smart pointer to the IStaticText interface. Smart pointers
automatically call the COM Release() method when they go out of scope or you pass
the address of a variable (like &pFormat) to a method.

IADHelper Interface

  C++

  __interfaceIADHelper : IUnknown
  {
      HRESULT Init(ILogger *pLogger);
      HRESULT ValidLogon(LPCTSTR userName, LPCTSTR password, LPCTSTR domain);
      HRESULT HasAccess(LPCTSTR username, LPCTSTR password, LPCTSTR domain,
  LPCTSTR computerName, LPCTSTR accountDomain);
  };

HRESULT Init(ILogger *pLogger)

<!-- p.1615 -->

Initialize this component, passing it to the logger so that it can log information.

HRESULTValidLogon(LPCTSTR userName, LPCTSTR password,
LPCTSTR domain)

This method verifies whether a set of credentials is valid, as shown in Table 10.

Table 10. HResultValidLogon

                                                                                 ﾉ   Expand table

 HResult      Description

 S_OK         Credentials are valid

 S_FALSE      Credentials are not valid

 E_FAIL       Could not locate the domain controller; check logs for details

HRESULT HasAccess(LPCTSTR username, LPCTSTR password,
LPCTSTR domain, LPCTSTR computerName, LPCTSTR
accountDomain)

This method verifies whether a set of credentials has read/write access to the computer
object in AD DS, as shown in Table 11.

Table 11. HResult HasAccess

                                                                                 ﾉ   Expand table

 HRESULT     Description

 S_OK        The user has access

 E_FAIL      The user does not have access. Check the log file for additional information.

IBackgroundTask Interface

  C++

  __interface IBackgroundTask : IUnknown
  {
      HRESULT Init(ITask *pTask, int id, IBackgroundCallback *pCallback);
      void Start(void);

<!-- p.1616 -->

         BOOL Running(void);
         HRESULT Wait(DWORD waitMilliseconds);
         HRESULT Terminate(DWORD exitCode);
         HRESULT GetExitCode(LPDWORD pCode, HRESULT *pHresult);
         HRESULT Close(void);
  };

Overview

The Progress page uses this class to run tasks on a separate thread. You can also use
this class whenever you want to perform operations on a separate thread. Tasks are any
class that supports the ITask interface.

This interface is implemented by the ID_BackgroundTask
("Microsoft.Wizard.BackgroundTask") component, defined in the IBackgroundTask.h
interface.

HRESULT Init(ITask *pTask, int id, IBackgroundCallback *pCallback)

This interface initializes the component, as shown in Table 12.

Table 12. HRESULT Init

                                                                                 ﾉ   Expand table

 Parameter    Description

 pTask        Pointer to the class that contains the code you want to run on another thread

 Id           A number you can use in the callback's Finished method to tell which task finished
              running; useful if you start several tasks with the same callback method

 pCallback    A class that implements the Finished method, which is called whenever a task
              finishes running; the call to the Finished method will be on the background thread,
              not the UI thread

void Start(void)

This method starts the task on a background thread and returns the elements shown in
Table 13.

Table 13. Return Background Thread

<!-- p.1617 -->

                                                                                    ﾉ    Expand table

 Returns                Description

 E_INVALIDARG           The task is already running, so you cannot start it right now.

 E_FAIL                 There was a problem starting the thread.

 S_OK                   The thread was started.

BOOL Running()

This method returns TRUE if the background task is currently running and FALSE if it is
not running.

HRESULT Wait(DWORD waitMilliseconds)

This method waits until either the thread stops running or the number of milliseconds
has elapsed.

HRESULT Terminate(DWORD exitCode)

This method kills the thread that is running (see Table 14 and Table 15). This process
may take a short amount of time to finish after this method returns.

Table 14. HRESULT Terminate Exit Code

                                                                                    ﾉ    Expand table

 Parameter     Description

 exitCode      The exit code that will be sent to the Finished callback method, which will also be
               available from the GetExitCode method.

Table 15. Termination Codes

                                                                                    ﾉ    Expand table

 Returns           Description

 E_FAIL            The call to terminate failed.

 S_OK              The request to terminate the thread succeeded.

<!-- p.1618 -->

HRESULT GetExitCode(LPDWORD pCode, HRESULT *pHresult)

Use this method to get the results of running the task on the background thread (see
Table 16).

Table 16. Result Codes

                                                                                   ﾉ   Expand table

 Parameter   Description

 pCode       Pointer to a DWORD that will be set on return or nullptr if you do not need the
             return value. On exit, this parameter is set to STILL_ACTIVE if the thread is running,
             the code returned by the task's Execute method, or the value passed to the
             Terminate method if you called that method.

 pHresult    Pointer to an HRESULT that will be set on return or nullptr if you do not need the
             HRESULT value.

HRESULT Close(void)

This method releases the background thread. It returns E_INVALIDARG if the thread is
currently running and S_OK otherwise.

ICheckBox Interface

  C++

  __interface ICheckBox : IControl
  {
      void Check(BOOL check);
      BOOL IsButtonChecked();
  };

void Check(BOOL check)

Set the checked state of the check box. When the method is TRUE, the check box is
selected; when the method is FALSE, the check box is cleared.

BOOL IsButtonChecked()

This method reports the current check state of a check box.

<!-- p.1619 -->

IComboBox Interface

  C++

  __interface IComboBox : IControl
  {
      HRESULT Bind([in] IBindableList *pList);
      HRESULT Select(int index);
      int Selected(void);
      void Add([in] LPCTSTR caption);
      HRESULT GetText([out, retval] LPBSTR pText);
      void Clear();
  };

Overview

This interface is implemented by the CheckBoxWrapper component. You retrieve an
instance of this component using the GetControlWrapper helper function with the type
CONTROL_COMBO_BOX.

HRESULT Bind([in] IBindableList *pList)

Use this method when you have a data source that implements the IBindableList
interface. The list box initializes the contents with the captions from this list.

HRESULT Select(int index)

Select the item in the combo box at the index.

int Selected(void)

This method returns the index of the selected item or -1 if nothing is selected.

void Add([in] LPCTSTR caption)

Manually add an item to the combo box.

HRESULT GetText([out, retval] LPBSTR pText)

Retrieve the string of the currently selected item in the combo box.

void Clear()

<!-- p.1620 -->

Remove all the items from the combo box.

IControl Interface

  C++

  __interface IControl : IUnknown
  {
      HRESULT SetEnable(BOOL enable);
      BOOL IsEnabled(void);
      HRESULT SetVisible(BOOL visible);
  };

Overview

This interface is implemented by the ControlWrapper component. You retrieve an
instance of this component using the GetControlWrapper helper function with the type
CONTROL_GENERIC.

HRESULT SetEnable(BOOL enable)

Enable or disable the control.

BOOL IsEnabled(void)

Returns TRUE if the control is enabled, FALSE if it is not.

HRESULT SetVisible(BOOL visible)

Show or hide the control.

ICpuInfo Interface

  C++

  __interface ICpuInfo : IUnknown
  {
      BOOL Is64Bit(void);
  };

Overview

<!-- p.1621 -->

You obtain this interface by creating a new ID_CpuInfo component. The single method
reports whether the CPU is 32 or 64 bit. Note that if you have a 32-bit operating system
on a 64-bit computer, this method returns TRUE, because it is only reporting the width
of the CPU (not the operating system).

IDirectory Interface

  C++

  __interface IDirectory : IUnknown
  {
      BOOL FileExists(LPCWSTR name);
      BOOL FindFirst([in] LPCWSTR name);
      HRESULT FoundName([out, retval] LPBSTR name);
      DWORD FoundAttributes(void);
      BOOL FindNext(void);
      void FinishFind(void);
  };

Overview

The Directory component, which you create using ID_Directory, provides a façade for
working with directories in the file system.

BOOL FileExists(LPCWSTR name)

This method returns TRUE if a file with the name you provide exists.

BOOL FindFirst([in] LPCWSTR name)

This method finds a first match for the name you provide. It supports wildcard
characters and returns both file and directory names. The method returns TRUE if a
match was found, FALSE otherwise.

HRESULT FoundName([out, retval] LPBSTR name)

This method retrieves the name of the file found with a call to FindFirst or FindNext.

DWORD FoundAttributes(void)

This method returns the attribute for the most recent found file or directory. You can use
code as follows to test whether it is a directory:

<!-- p.1622 -->

  C++

  pDirectory->FoundAttributes() & FILE_ATTRIBUTE_DIRECTORY

BOOL FindNext(void)

Find the next. This method returns TRUE if another match was found, FALSE otherwise.

void FinishFind(void)

This method releases resources used for the Find operation.

IDomainJoinValidator Interface

  C++

  __interface IDomainJoinValidator : IUnknown
  {
      HRESULT Init(ILogger *pLogger, IWizardPageContainer *pContainer,
  IStaticText *pUsername, IStaticText *pPassword, IStaticText *pComputerName);
      HRESULT IsUsernameValid(LPCWSTR domainName);
      BOOL CanModifyComputerAdEntry(LPCWSTR domainName);
  };

Overview

You obtain an instance of this interface using the ID_DomainJoinValidator value to the
CreateInstance template function.

HRESULT Init(ILogger *pLogger, IWizardPageContainer
*pContainer, IStaticText *pUsername, IStaticText *pPassword,
IStaticText *pComputerName)

Initialize the instance, as shown in Table 17.

Table 17. HRESULT Init - Instance Initialization

                                                                       ﾉ   Expand table

<!-- p.1623 -->

 Parameter         Description

 pLogger           The logger instance, which is available to your page via the page's Logger
                   method

 pContainer        Passes the results from your page's Container method

 pUsername         The text box that contains the user name to be validated

 pPassword         The text box that contains the password to be validated

 PComputerName     The text box that contains the name of the computer that will eventually be
                   joined to the domain

HRESULT IsUsernameValid(LPCWSTR domainName)

This method uses the IADHelper->ValidLogon method to do the work. See that method
for details.

BOOL CanModifyComputerAdEntry(LPCWSTR domainName)

Verify whether the user has rights to modify the computer entry. Most of the work is
done by IADHelper->HasAccess. If this method returns FALSE, check the log file for
details.

IDriveList Interface

  C++

  __interface IDriveList : IUnknown
  {
      HRESULT Init(IWmiRepository *pWmi);
      HRESULT SetWhereClause(LPCTSTR whereClause);
      HRESULT SetMinimumDriveSize(__int64 size);
      HRESULT Update(void);
      HRESULT AddProperty(ENUM_DISK_QUERY_SECTION section, LPCTSTR propName,
  LPCTSTR propNameReturned);

        size_t Count(void);
        HRESULT GetProperty(size_t index, LPCTSTR propName,            LPVARIANT value);
        HRESULT GetCaption(size_t index, LPBSTR pCaption);
  }

HRESULT Init(IWmiRepository *pWmi)

<!-- p.1624 -->

Call this method before you call any other components. You will need to create a new
WmiRepository before you call this method.

HRESULT SetWhereClause(LPCTSTR whereClause)

This method allows you to add text that will appear as a "where" clause in the query. For
example, the following line returns only USB drives:

  C++

   pDrives->SetWhereClause(L"WHERE InterfaceType='USB'");

HRESULT SetMinimumDriveSize(__int64 size)

Set the minimize drive size, in bytes, for drives that will be returned from the query.

HRESULT Update(void)

Execute the query. The drive list available after calling this method is sorted by drive
letter.

HRESULT AddProperty(ENUM_DISK_QUERY_SECTION section,
LPCTSTR propName, LPCTSTR propNameReturned)

This method adds the names of additional properties that you want to make available in
the query results. Call this method before calling Update. Table 18 shows three of the
useful properties.

Table 18. HRESULT AddProperty: Useful Properties

                                                                              ﾉ   Expand table

 Section                       Property        Description

 DISKQUERY_LOGICALDISK         Size            The size, in bytes, represented as a string

 DISKQUERY_DISKPARTITION       DiskIndex       The disk number as an integer, starting with 0

 DISKQUERY_LOGICALDISK         VolumeName      The volume label

size_t Count(void)

<!-- p.1625 -->

The number of records the query returns. Call Update before you call this method.

HRESULT GetProperty(size_t index, LPCTSTR propName,
LPVARIANT value)

This method retrieves the value of a property from the query results, as shown in Table
19.

Table 19. HRESULT GetProperty

                                                                                ﾉ    Expand table

 Parameter      Description

 Index          Zero-based index to the result record

 propName       Name of the property, such as "Size"

 Value          On return, this parameter contains a variant value of the property

HRESULT GetCaption(size_t index, LPBSTR pCaption)

This method retrieves the caption for a record which is the same as the Caption
property.

IImageList Interface

  C++

  __interface IImageList
  {
      HRESULT CreateImageList(int width, int height, UINT flags);
      HImageList GetImageList(void);
      int AddImage(HInstance hInstance, int resourceId);
  };

Overview

This interface is implemented by the ImageList component. You retrieve an instance of
this component from the IListView interface.

HRESULT CreateImageList(int width, int height, UINT flags)

<!-- p.1626 -->

Create a new image list, which this component manages. Call this method only once.

HImageList GetImageList(void)

This method returns the handle for the image list in case you need to perform other
operations on the image list.

int AddImage(HInstance hInstance, int resourceId)

Add a new image to the image list from a resource, as shown in Table 20.

Table 20. HRESULT IImageList Interface

                                                                             ﾉ    Expand table

 Parameter      Description

 hInstance      Instance handle of the module that contains the bitmap resource

 resourceId     ID of the resource to load into the image list

IListView Interface

  C++

  __interface IListView : IControl
  {
      int AddItem([in] LPCTSTR text);
      int AddColumn(int width, [in] LPCTSTR text);
      HRESULT SetSubItem(int index, int column, [in] LPCTSTR text);
      int GetWidth(void);
      void SetExtendedStyle(DWORD style);
      int GetSelectedItem(void);
      HRESULT SelectItem(int index);
      BOOL IsItemChecked(int index);
      int GetItemCount(void);
      HRESULT CreateImageList(int width, int height, UINT flags);
      int AddImage(HINSTANCE hInstance, int resourceId);
      HRESULT SetImage(int index, int imageIndex);
      HRESULT Clear(void);
  };

Overview

<!-- p.1627 -->

This interface is implemented by the ControlWrapper component. You retrieve an
instance of this component using the GetControlWrapper helper function with the type
CONTROL_LIST_VIEW.

int AddItem([in] LPCTSTR text)

Add a new row to the list box. The method returns the index of the item just added.

int AddColumn(int width, [in] LPCTSTR text)

Add a new column to the list view.

HRESULT SetSubItem(int index, int column, [in] LPCTSTR text)

Set the text in a column other than the first column of the list box, as shown in Table 21.

Table 21. HRESULT SetSubItem

                                                                               ﾉ   Expand table

 Parameter   Description

 index       The index of the list item you want to modify

 column      The index of the column you want to update; the first column is set with AddItem,
             columns two and following are set with this method

 text        The string to show in the column

int GetWidth(void)

This method returns the width of the entire text box.

void SetExtendedStyle(DWORD style)

This method allows you to set extended styles on the list box—for example:

  C++

  m_pList->SetExtendedStyle(LVS_EX_FULLROWSELECT);

int GetSelectedItem(void)

<!-- p.1628 -->

This method returns the index of the list view item currently selected.

HRESULT SelectItem(int index)

Set the selected item in the list to this index.

BOOL IsItemChecked(int index)

This method returns TRUE if an item in the list is selected. This method requires that you
call SetExtendedStyle to set the check box style.

int GetItemCount(void)

This method returns the number of items in the list view.

HRESULT CreateImageList(int width, int height, UINT flags)

Create a new image list, and attach it to the list view.

int AddImage(HINSTANCE hInstance, int resourceId)

Add an image to the list view's image list. You need to call CreateImageList, first.

HRESULT SetImage(int index, int imageIndex)

Set the image that will be shown on the left side for a specific list view item.

HRESULT Clear(void)

Remove all items from the list view.

IProgressBar Interface

  C++

  __interface IProgressBar : IControl
  {
      HRESULT SetPercentage(int position);
      int GetPercentage(void);
  };

<!-- p.1629 -->

Overview

This interface is implemented by the ProgressBarWrapper component. You retrieve an
instance of this component using the GetControlWrapper helper function with the type
CONTROL_PROGRESS_BAR.

HRESULT SetPercentage(int position)

Set the position of the progress bar using a number between 0 and 100. By default, new
Win32® progress bars have a maximum range of 100.

int GetPercentage(void)

This method returns the current position of the progress bar.

IRadioButton Interface

  C++

  __interface IRadioButton : IControl
  {
  public:
      void SetGroup(int firstId, int lastId);
      void CheckRadio(int id);
      BOOL IsButtonChecked(int id);
      void EnableRadio(int id, BOOL enable);
  };

Overview

This interface is implemented by the RadioButtonWrapper component. You retrieve an
instance of this component using the GetControlWrapper helper function with the type
CONTROL_RADIO_BUTTON.

void SetGroup(int firstId, int lastId)

Provide the wrapper with the range of radio buttons that should be treated as a group.
Call this method before you call CheckRadio.

void CheckRadio(int id)

<!-- p.1630 -->

Set the specific radio button to be the single button in the group of radio buttons
selected. Call SetGroup before calling this method.

BOOL IsButtonChecked(int id)

This method returns TRUE if the radio button is currently selected, FALSE otherwise.

void EnableRadio(int id, BOOL enable)

This method enables or disables a radio button.

IStaticText Interface

  C++

  __interface IStaticText : IControl
  {
      HRESULT SetText([in] LPCTSTR pText);
      HRESULT GetText([out, retval] LPBSTR pText);
  };

Overview

This interface is implemented by the StaticTextWrapper component. You retrieve an
instance of this component using the GetControlWrapper helper function with the type
CONTROL_STATIC_TEXT.

HRESULT SetText([in] LPCTSTR pText)

Set the text for the control.

HRESULT GetText([out, retval] LPBSTR pText)

This method returns the current value of the text for the control.

ITask Interface

  C++

  __interface IControl : IUnknown
  {
      HRESULT Init(IStringProperties *pProperties, ISettingsProperties

<!-- p.1631 -->

  *pTaskSettings);
      HRESULT Execute(LPDWORD pReturnCode);
  };

Implement this interface if you want your component to be available as a task in the
preflight page or if you want to use the BackgroundTask component to perform work
on a background thread.

Here are components that implement the ITask interface:

       ID_ShellExecuteTask, L"Microsoft.Wizard.ShellExecuteTask"

       ID_CopyFilesTask, L"Microsoft.Wizard.CopyFilesTask"

       ID_ACPowerTask, L"Microsoft.OSDRefresh.ACPowerTask"

       ID_WiredNetworkTask, L"Microsoft.SharedPages.WiredNetworkTask"

Init

  C++

  HRESULT Init(IStringProperties *pProperties, ISettingsProperties
  *pTaskSettings)

If you are writing a task for the preflight page, call this method to initialize your task.
The .config file contain XML that might look something like this:

  XML

  <Task DisplayName="Check Windows Scripting Host"
  Type="Microsoft.Wizard.ShellExecuteTask">
    <Setter Property="filename">%windir%\system32\cscript.exe</Setter>
    <Setter Property="parameters">Preflight\OSDCheckWSH.vbs</Setter>
    <Setter Property="BitmapFilename">images\WinScriptHost.bmp</Setter>
    <ExitCodes>
      <ExitCode State="Success" Type="0" Value="0" Text="" />
      <ExitCode State="Error" Type="-1" Value="*" Text="Windows Scripting Host
  not installed." />
    </ExitCodes>
  </Task>

The pProperties parameter provides access to the three setter values, whereas the
pTaskSettings parameter provides access to the Task element and children. Most tasks
only need to read data from the pProperties parameter.

<!-- p.1632 -->

Execute

  C++

  HRESULT Execute(LPDWORD pReturnCode)

Here is where you write the code that performs the task. This method should return
S_OK if there were no errors, and it can return another HRESULT if an error occurred
while the task was running. Values other than S_OK that this method returns are
matched up to <Error> elements in the <ExitCodes> section if you are using the
preflight page.

The pReturnCode parameter must be updated with a number that reports the state of
the task. These values are matched by the preflights page to <ExitCode> elements.

ITreeView Interface

  C++

  __interface ITreeView : IControl
  {
      void EnableCheckboxes(void);
      HRESULT CreateImageList(int width, int height, UINT flags);
      int AddImage(HINSTANCE hInstance, int resourceId);

        HTREEITEM AddItem(LPCTSTR text, HTREEITEM hParent = NULL);
        void SetImage(HTREEITEM item, int image, int expandImage);

        void Clear(void);
        BOOL SetFirstVisible(HTREEITEM item);
        BOOL SelectItem(HTREEITEM item);
        void CheckItem(HTREEITEM item, UINT checkState);
        HTREEITEM SelectedItem(void);
        int SetItemHeight(SHORT height);
        HRESULT EnableItem(HTREEITEM item, BOOL enable);
        void Expand(HTREEITEM hItem, BOOL expand);

        HTREEITEM GetChild(HTREEITEM hParent);
        HTREEITEM GetParent(HTREEITEM hNode);
        HTREEITEM GetNextItem(HTREEITEM hPrevious);

        UINT IsChecked(HTREEITEM item);
        BOOL IsEnabled(HTREEITEM item);

        INT_PTR CommonControlEvent(WORD controlId, void* pInfo, BOOL *pCancel);
        HRESULT SetEventHandler(ITreeViewEvent *pEventHandler);

<!-- p.1633 -->

       void SetSelectedBackColor(COLORREF color);
  };

Overview

This interface is implemented by the TreeViewWrapper component. You retrieve an
instance of this component using the GetControlWrapper helper function with the type
CONTROL_TREE_VIEW.

void EnableCheckboxes(void)

This method turns on check boxes in the tree view control by setting the
TVS_CHECKBOXES style.

HRESULT CreateImageList(int width, int height, UINT flags)

Add a new image list to the tree view control. The flags parameter is passed in the call
to the ImageList_Create Win32 function.

int AddImage(HINSTANCE hInstance, int resourceId)

Add an image to the image list from a resource (resourceId) in the module with the
instance handle hInstance.

HTREEITEM AddItem(LPCTSTR text, HTREEITEM hParent = NULL)

Add a node to the tree view. The new node will be added at the top level if hParent is
NULL. Otherwise, provide the handle to the parent item where you want the new item
added. This method returns the handle to the new item.

void SetImage(HTREEITEM item, int image, int expandImage)

Set the image to use for a tree view item. You can set both the normal and the
expanded image.

void Clear(void)

Remove all items from the tree view.

BOOL SetFirstVisible(HTREEITEM item)

<!-- p.1634 -->

Ensure that the tree view item is visible. The tree view will scroll if required to make this
item visible.

BOOL SelectItem(HTREEITEM item)

Set the currently selected item to the item that you provide. You can call SetFirstVisible
after this to ensure that the newly selected item is visible.

void CheckItem(HTREEITEM item, UINT checkState)

The method basically sets the image that will be shown for the check box in the tree
view. These images are in a separate ImageList control that the tree view manages. By
default, this image list has three images in it, shown in Table 22.

Table 22.void CheckItem Image List Default

                                                                            ﾉ   Expand table

 checkState                                    Description

 0                                             Blank

 1                                             Cleared

 2                                             Selected

HTREEITEM SelectedItem(void)

This method returns the handle of the tree view item currently selected.

int SetItemHeight(SHORT height)

This method sets the height of all items in the tree view control in pixels. It returns the
previous height in pixels.

HRESULT EnableItem(HTREEITEM item, BOOL enable)

This method enables or disables a single item in the tree. Disabling an item with children
will not disable the children.

void Expand(HTREEITEM hItem, BOOL expand)

<!-- p.1635 -->

This method expands or collapses a node in the tree.

HTREEITEM GetChild(HTREEITEM hParent)

This method returns the first child of a tree view item or NULL if there are no children.

HTREEITEM GetParent(HTREEITEM hNode)

This method returns the handle of the parent for a node in the tree view or NULL if the
node is at the top level.

HTREEITEM GetNextItem(HTREEITEM hPrevious)

You can call this method with a handle that GetChild returns to iterate through all the
children of a node. This method returns the next sibling in the tree that shares the same
parent.

UINT IsChecked(HTREEITEM item)

This method returns 0 if the tree view node is not selected and 1 if it is.

BOOL IsEnabled(HTREEITEM item)

This method returns TRUE if the tree view node is enabled, FALSE otherwise.

INT_PTR CommonControlEvent(WORD controlId, void* pInfo,
BOOL *pCancel)

This method is for internal use only.

HRESULT SetEventHandler(ITreeViewEvent *pEventHandler)

Call this method if you want to receive notification when the selected item changes or
the user changes the check state of a tree view item. You must implement the
ITreeViewEvent in your component to receive these callbacks.

void SetSelectedBackColor(COLORREF color)

Set the background color used for the selected item.

<!-- p.1636 -->

IWmiIteration Interface

  C++

  __interface IWmiIterator : IUnknown
  {
      HRESULT Next(void);
      HRESULT GetProperty(LPCTSTR propertyName, [out] LPVARIANT pValue);
  };

Overview

You typically use this interface, along with IWmiRepository, when working with WMI
calls. The IWmiIteration interface allows you to iterate through the values that a query
returns.

HRESULT Next(void)

Move to the next item in the query results, as shown in Table 23.

Table 23. HRESULT Next(void) Query Returns

                                                                               ﾉ   Expand table

 HRRESULT    Description

 S_OK        Moved to the next result; you can use GetProperty to retrieve properties of that
             result.

 S_FALSE     There are no more items in the list.

 E_NOT_SET   There are no query results

HRESULT GetProperty(LPCTSTR propertyName, [out] LPVARIANT
pValue)

This method retrieves the value of a property from the current result record, as shown in
Table 24 and Table 25.

Table 24. HRESULT GetProperty

                                                                               ﾉ   Expand table

<!-- p.1637 -->

 Parameter        Description

 propertyName     Name of the property you want to retrieve

 pValue           Points to a VARIANT structure that on return contains the property value

Table 25. HRESULT GetProperty Result

                                                                              ﾉ   Expand table

 HRESULT                               Description

 S_OK                                  Property value was retrieved.

 WBEM_E_NOT_FOUND                      There is no property with the name.

 E_NOT_VALID_STATE                     There is no current record.

  ７ Note

  The GetProperty method can return other WMI error codes other than those listed
  in Table 25. The values listed are the common results that are returned.

IWmiRepository Interface

  C++

  __interface IWmiRepository : IUnknown
  {
      HRESULT SetNamespace(LPCWSTR namespaceName);
      HRESULT ExecQuery(LPCWSTR query, [out] IWmiIterator **ppIterator);
  };

Overview

This interface is implemented by the WmiRepository component (ID_WmiRepository).

HRESULT SetNamespace(LPCWSTR namespaceName)

This method sets the WMI namespace that will be used for the query. Call this method
before you call ExecQuery. If you do not call this method, the namespace will be
root\cimv2. This method always returns S_OK.

<!-- p.1638 -->

HRESULT ExecQuery(LPCWSTR query, [out] IWmiIterator
**ppIterator)

Execute a query against the WMI namespace set with a call to SetNamespace, as shown
in Table 26 and Table 27.

Table 26. HRESULT ExecQuery

                                                                                     ﾉ   Expand table

 Parameter    Description

 Query        The string for the WMI query you want to execute

 ppIterator   Pass a pointer to an interface pointer, which on return will be filled in with an
              interface, giving you access to the query results

Table 27. HRESULT Query Result

                                                                                     ﾉ   Expand table

 HRESULT          Description

 S_OK             Query succeeded

 Other            If the query did not succeed, returns a WMI HRESULT

IFormController Interface

  C++

  __interface IFormController : IUnknown
  {
      Init(IWizardPageView *pView, IWizardPageContainer *pContainer);
      SetPageInfo(ISettingsProperties *pPageInfo);

         Validate(void);

         AddToGroup(int groupControlId, int controlId);
         UpdateCheckGroup(int groupControlId);
         AddValidator(int controlId, IValidator *pValidator, IControl *pCOntrol =
  0);

      AddValidator(int controlId, LPCWSTR validatorId, LPCWSTR message,
  IValidator **ppValidator = nullptr);
      DisableValidation(int controlId, BOOL disable);

<!-- p.1639 -->

      AddField(LPCWSTR fieldName, int controlId, BOOL suppressLog,
  DialogControlTypes type);
      AddRadioGroup(LPCWSTR groupName, int radioControlId);
      EnableRadioGroup(LPCWSTR groupName, BOOL enable);
      InitFields(IFieldCallback *pFieldCallback = nullptr);
      SaveFields(IFieldCallback *pFieldCallback = nullptr);
      BOOL IsFieldDisabled(int controlId);

         InitSection(LPCWSTR key, LPCWSTR sectionCaption);
         AddSummaryItem(LPCWSTR first, LPCWSTR second);
         SuppressLogValue(LPCWSTR tsVariableName);
         SaveText(int controlId, LPCWSTR tsVariableName, LPCWSTR summaryCaption);
         LoadText(int controlId, LPCWSTR tsVariableName);

         void ControlEvent(WORD eventId, WORD controlId);
         BOOL IsValid(void);
    };

Overview

Each page in the UDI Wizard has its own form controller that implements this interface.
You use this controller to connect the field data in the .config XML file to the controls on
your page. The form controller then handles many of the details for you.

Setting up the Form

Generally, set up the form controller in your page's OnWindowCreated method. Doing
so usually involves calling the methods shown in Table 28.

Table 28. OnWindowCreated Method

                                                                                  ﾉ    Expand table

 Method            Description

 Init              Initializes the form controller

 AddField          Provides a connection between a field in the .config XML file that is a string
                   name and a control in your page's dialog box that is an ID

 AddRadioGroup     Used to connect a radio button to both a group and a control in your dialog
                   box

 AddToGroup        Allows you "child" controls that are enabled or disabled along with their parent
                   or based on which radio button is selected

 InitFields        Call after you have called all the Add methods to set up the form

<!-- p.1640 -->

 Method             Description

 Validate           Performs the initial validation

Processing Form Events

Add the following call to your OnControlEvent method:

  C++

  Form()->ControlEvent(eventId, controlId);

This call passes events on to the form controller so it can process form-related events.

Save Form Data

In the OnNextSelected method, call the form methods shown in Table 29.

Table 29. OnNextSelected Method

                                                                               ﾉ      Expand table

 Method        Description

 InitSection   Provides the name of the section that will be shown on the Summary page for this
               page

 SaveFields    Save field values to task sequence variables and to the Summary page

Init

  C++

  HRESULT Init(IWizardPageView *pView, IWizardPageContainer *pContainer)

You usually call this method near the start of your page's OnWindowCreated method.
The command should look something like this:

  C++

  Form()->Init(View(), Container());
