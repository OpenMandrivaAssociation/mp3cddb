%define name mp3cddb
%define version 1.6
%define release %mkrel 8

Summary:	Console MP3 renaming program
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.bz2
License: 	GPL
Group: 		File tools
Url: 		http://rufus.hackish.org/wiki/MP3cddb
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	perl-Term-ReadLine-Gnu

%description
Mp3cddb is a console MP3 renaming program. It can retrieve album data
automatically or manually from FreeDB, from ID3 tags, or from a blank
template. Files can be renamed into any imaginable directory structure
and format using a powerful yet simple configuration syntax.

%prep
%setup -q

%install
%__rm -rf $RPM_BUILD_ROOT
%__install -m 755 -D %{name}-%{version}.pl $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}


