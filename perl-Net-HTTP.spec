#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-HTTP
Version  : 6.21
Release  : 39
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/Net-HTTP-6.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/Net-HTTP-6.21.tar.gz
Summary  : 'Low-level HTTP connection (client)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Net-HTTP-license = %{version}-%{release}
Requires: perl-Net-HTTP-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(URI)

%description
# NAME
Net::HTTP - Low-level HTTP connection (client)
# VERSION
version 6.21
# SYNOPSIS

%package dev
Summary: dev components for the perl-Net-HTTP package.
Group: Development
Provides: perl-Net-HTTP-devel = %{version}-%{release}
Requires: perl-Net-HTTP = %{version}-%{release}

%description dev
dev components for the perl-Net-HTTP package.


%package license
Summary: license components for the perl-Net-HTTP package.
Group: Default

%description license
license components for the perl-Net-HTTP package.


%package perl
Summary: perl components for the perl-Net-HTTP package.
Group: Default
Requires: perl-Net-HTTP = %{version}-%{release}

%description perl
perl components for the perl-Net-HTTP package.


%prep
%setup -q -n Net-HTTP-6.21
cd %{_builddir}/Net-HTTP-6.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-HTTP
cp %{_builddir}/Net-HTTP-6.21/LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-HTTP/6e6fb60587958e5351e6f08e2e2088afb70ac03d
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::HTTP.3
/usr/share/man/man3/Net::HTTP::Methods.3
/usr/share/man/man3/Net::HTTP::NB.3
/usr/share/man/man3/Net::HTTPS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-HTTP/6e6fb60587958e5351e6f08e2e2088afb70ac03d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Net/HTTP.pm
/usr/lib/perl5/vendor_perl/5.34.0/Net/HTTP/Methods.pm
/usr/lib/perl5/vendor_perl/5.34.0/Net/HTTP/NB.pm
/usr/lib/perl5/vendor_perl/5.34.0/Net/HTTPS.pm
