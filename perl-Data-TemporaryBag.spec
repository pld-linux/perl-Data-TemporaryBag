#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	TemporaryBag
Summary:	Data::TemporaryBag - handle long size data using temporary file
Summary(pl):	Data::TemporaryBag - obs³uga danych o du¿ym rozmiarze przy pomocy pliku tymczasowego
Name:		perl-Data-TemporaryBag
Version:	0.08
Release:	0.2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b677da9db9abdb1ff996e56ddb28dacc
URL:		http://search.cpan.org/dist/Data-TemporaryBag/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::TemporaryBag module provides a bag object class handling long
size data. The short size data are kept on memory. When the data size
becomes over $Threshold size, they are saved into a temporary file
internally.

%description -l pl
Modu³ Data::TemporaryBAg dostarcza klasê obiektu torby obs³uguj±c±
dane o du¿ym rozmiarze. Dane o ma³ym rozmiarze s± przechowywane w
pamiêci. Kiedy rozmiar danych przekracza $Threshold, s± one zapisywane
wewnêtrznie do pliku tymczasowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/TemporaryBag.pm
%{_mandir}/man3/*
