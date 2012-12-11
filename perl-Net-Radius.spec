%define upstream_name       Net-Radius
%define upstream_version 2.103

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Object-oriented Perl interface to RADIUS
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Warn)
BuildArch:	noarch

%description
The modules included here provide an interface to the RADIUS
protocol. It consists of the following modules:

Net::Radius::Packet - Deals with RADIUS packets
Net::Radius::Dictionary - Deals with RADIUS dictionaries

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README* examples
%{perl_vendorlib}/Net
%{_mandir}/*/*

%changelog
* Wed Dec 02 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.103.0-1mdv2010.1
+ Revision: 472593
- update to 2.103

* Sat Aug 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.560.0-1mdv2010.0
+ Revision: 419608
- new perl version macro

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.56-4mdv2009.0
+ Revision: 258086
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.56-3mdv2009.0
+ Revision: 246165
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.56-1mdv2008.1
+ Revision: 140693
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.56-1mdv2008.0
+ Revision: 47700
- update to new version 1.56

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.55-1mdv2008.0
+ Revision: 20323
- 1.55


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.49-1mdv2007.0
- New version 1.49
- spec cleanup

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.44-2mdk
- Fix SPEC according to Perl Policy
    - Source URL
- use mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.44-1mdk
- initial Mandriva package

