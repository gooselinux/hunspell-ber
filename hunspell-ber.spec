Name: hunspell-ber
Summary: Amazigh hunspell dictionaries
%define upstreamid 20080210
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://ayaspell.sourceforge.net/data/hunspell-am_test.tar.gz
Group: Applications/Text
URL: http://ayaspell.sourceforge.net/am.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Amazigh hunspell dictionaries.

%prep
%setup -q -n spelling_tifinagh

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p tifinagh.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ber_MA.dic
cp -p tifinagh.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ber_MA.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20080210-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080210-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080210-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 07 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080210-1
- initial version
