#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-HTTP
Version  : 6.07
Release  : 12
URL      : http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/Net-HTTP-6.07.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/Net-HTTP-6.07.tar.gz
Summary  : 'Low-level HTTP connection (client)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Net-HTTP-doc
BuildRequires : perl(URI)

%description
NAME
Net::HTTP - Low-level HTTP connection (client)
SYNOPSIS
use Net::HTTP;
my $s = Net::HTTP->new(Host => "www.perl.com") || die $@;
$s->write_request(GET => "/", 'User-Agent' => "Mozilla/5.0");
my($code, $mess, %h) = $s->read_response_headers;

%package doc
Summary: doc components for the perl-Net-HTTP package.
Group: Documentation

%description doc
doc components for the perl-Net-HTTP package.


%prep
%setup -q -n Net-HTTP-6.07

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/Net/HTTP.pm
/usr/lib/perl5/site_perl/5.24.0/Net/HTTP/Methods.pm
/usr/lib/perl5/site_perl/5.24.0/Net/HTTP/NB.pm
/usr/lib/perl5/site_perl/5.24.0/Net/HTTPS.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
