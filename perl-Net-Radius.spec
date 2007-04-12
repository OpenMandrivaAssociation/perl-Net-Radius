%define module  Net-Radius
%define name    perl-%{module}
%define version 1.49
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Object-oriented Perl interface to RADIUS
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The modules included here provide an interface to the RADIUS
protocol. It consists of the following modules:

Net::Radius::Packet - Deals with RADIUS packets
Net::Radius::Dictionary - Deals with RADIUS dictionaries

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README* examples
%{perl_vendorlib}/Net
%{_mandir}/*/*

