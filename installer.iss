; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{92ED92E8-F1D4-4E06-BB55-C60765E1BE87}
AppName=Video Split by Ravenous
AppVersion=0.1
;AppVerName=Video Split by Ravenous 0.1
AppPublisher=Ravenous
AppPublisherURL=https://github.com/itsravenous/videosplitter
AppSupportURL=https://github.com/itsravenous/videosplitter
AppUpdatesURL=https://github.com/itsravenous/videosplitter
DefaultDirName={pf}\Video Split by Ravenous
DefaultGroupName=Video Split by Ravenous
AllowNoIcons=yes
LicenseFile=C:\Users\IEUser\Documents\gpl-2_0.txt
OutputBaseFilename=video-split-setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\IEUser\Desktop\video-split\dist\video-split\video-split.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\IEUser\Desktop\video-split\dist\video-split\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Video Split by Ravenous"; Filename: "{app}\video-split.exe"
Name: "{group}\{cm:UninstallProgram,Video Split by Ravenous}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\Video Split by Ravenous"; Filename: "{app}\video-split.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\video-split.exe"; Description: "{cm:LaunchProgram,Video Split by Ravenous}"; Flags: nowait postinstall skipifsilent

