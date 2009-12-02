%define upstream_name       Net-Radius
%define upstream_version 2.103

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:        Object-oriented Perl interface to RADIUS
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
Buildrequires:  perl(Test::Warn)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The modules included here provide an interface to the RADIUS
protocol. It consists of the following modules:

Net::Radius::Packet - Deals with RADIUS packets
Net::Radius::Dictionary - Deals with RADIUS dictionaries

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

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

