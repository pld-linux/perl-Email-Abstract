#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Abstract
Summary:	Unified interface to mail representations
Summary(pl):	Zunifikiowany interfejs do prezentacji maili
Name:		perl-%{pdir}-%{pnam}
Version:	1.0
Release:	1
# note if it is "same as perl"
License:	GPL v1+ or Artistic	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed5f792c40511b23356cefeea22b0703
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq	'perl(anything_fake_or_conditional)'

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

#%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
# if module isn't noarch, use:
# %{__make} \
#	OPTIMIZE="%{rpmcflags}"

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
# use macros:
%{perl_vendorlib}/Email/Abstract.pm
%{perl_vendorlib}/Email/Abstract
%{_mandir}/man3/*
