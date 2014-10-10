%define upstream_name       Net-Radius
%define upstream_version 2.103

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Summary:	Object-oriented Perl interface to RADIUS
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
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
