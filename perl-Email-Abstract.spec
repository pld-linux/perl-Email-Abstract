#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Abstract
Summary:	Unified interface to mail representations
Summary(pl.UTF-8):	Zunifikiowany interfejs do reprezentacji listów
Name:		perl-Email-Abstract
Version:	2.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86717406b12436118e74dc2d593a7b59
URL:		http://search.cpan.org/dist/Email-Abstract/
BuildRequires:	perl-Email-Simple >= 1:1.91
BuildRequires:	perl-Module-Pluggable >= 1.5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Abstract provides module writers with the ability to write
representation-independent mail handling code. For instance, in the
cases of Mail::Thread or Mail::ListDetector, a key part of the code
involves reading the headers from a mail object. Where previously one
would either have to specify the mail class required, or to build a
new object from scratch, Email::Abstract can be used to perform
certain simple operations on an object regardless of its underlying
representation.

Email::Abstract currently supports Mail::Internet, MIME::Entity,
Mail::Message, Email::Simple and Email::MIME. Other representations
are encouraged to create their own Email::Abstract::* class by copying
Email::Abstract::EmailSimple. All modules installed under the
Email::Abstract hierarchy will be automatically picked up and used.

%description -l pl.UTF-8
Email::Abstract dostarcza piszącym moduły możliwość pisania kodu
obsługującego listy elektroniczne niezależnie od reprezentacji. Na
przykład w przypadku Mail::Thread lub Mail::ListDetector znacząca
część kodu dotyczy czytania nagłówków z obiektu listu. Tam, gdzie
poprzednio trzeba było podać wymaganą nazwę klasy lub zbudować nowy
obiekt od początku, można użyć Email::Abstract do wykonania pewnych
prostych operacji na obiekcie niezależnie od jego reprezentacji.

Email::Abstract aktualnie obsługuje Mail::Internet, MIME::Entity,
Mail::Message, Email::Simple oraz Email::MIME. Dla innych
reprezentacji zaleca się stworzyć własną klasę Email::Abstract::*
poprzez skopiowanie Email::Abstract::EmailSimple. Wszystkie moduły
zainstalowane w hierarchii Email::Abstract są automatycznie używane.

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
%{perl_vendorlib}/Email/Abstract.pm
%{perl_vendorlib}/Email/Abstract
%{_mandir}/man3/*
