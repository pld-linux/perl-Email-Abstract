#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Abstract
Summary:	Unified interface to mail representations
Summary(pl):	Zunifikiowany interfejs do reprezentacji listów
Name:		perl-Email-Abstract
Version:	2.0
Release:	1
# same as perl
License:	GPL v1+ or Artistic	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82635bfef138b4b70ac4d8c68f4d0598
BuildRequires:	perl-Email-Simple
BuildRequires:	perl-Module-Pluggable
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

%description -l pl
Email::Abstract dostarcza pisz±cym modu³y mo¿liwo¶æ pisania kodu
obs³uguj±cego listy elektroniczne niezale¿nie od reprezentacji. Na
przyk³ad w przypadku Mail::Thread lub Mail::ListDetector znacz±ca
czê¶æ kodu dotyczy czytania nag³ówków z obiektu listu. Tam, gdzie
poprzednio trzeba by³o podaæ wymagan± nazwê klasy lub zbudowaæ
nowy obiekt od pocz±tku, mo¿na u¿yæ Email::Abstract do wykonania
pewnych prostych operacji na obiekcie niezale¿nie od jego
reprezentacji.

Email::Abstract aktualnie obs³uguje Mail::Internet, MIME::Entity,
Mail::Message, Email::Simple oraz Email::MIME. Dla innych
reprezentacji zaleca siê stworzyæ w³asn± klasê Email::Abstract::*
poprzez skopiowanie Email::Abstract::EmailSimple. Wszystkie modu³y
zainstalowane w hierarchii Email::Abstract s± automatycznie u¿ywane.

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
