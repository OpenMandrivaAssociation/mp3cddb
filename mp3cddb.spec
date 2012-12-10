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




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-8mdv2011.0
+ Revision: 620401
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.6-7mdv2010.0
+ Revision: 430098
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.6-6mdv2009.0
+ Revision: 252928
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.6-4mdv2008.1
+ Revision: 170987
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.6-3mdv2008.1
+ Revision: 136608
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Feb 12 2007 Emmanuel Andry <eandry@mandriva.org> 1.6-3mdv2007.0
+ Revision: 120218
- fix requires
- Requires perl(Term::ReadLine::Gnu:XS)
- Import mp3cddb

* Sun May 14 2006 Emmanuel Andry <eandry@mandriva.org> 1.6-1mdk
- 1.6
- mkrel

* Fri Feb 04 2005 Jérémie Lenfant-Engelmann <tocman@gmail.com> 1.5-1mdk
- new version
- Add a RENAMEVA that if defined will be used on VA cds instead of the normal
- RENAME line. Thankes Sven for the patch.

* Thu Dec 30 2004 Jérémie Lenfant-Engelmann <tocman@gmail.com> 1.4-1mdk
- new version

* Tue Dec 28 2004 Jérémie Lenfant-Engelmann <tocman@gmail.com> 1.3-1mdk
- First package

