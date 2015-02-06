%define		_class		HTML
%define		_subclass	CSS
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.5.4
Release:	7
Summary:	Class for generating CSS declarations
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_CSS/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
%{upstream_name} provides a simple interface for generating a stylesheet
declaration. It is completely standards compliant, and has some great
features:
- simple OO interface to CSS definitions
- output to:
  - inline stylesheet declarations
  - document internal stylesheet declarations
  - standalone stylesheet declarations
  - array of definitions

In addition, it shares the following with HTML_Common based classes:
- indent style support
- line ending style

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-5mdv2012.0
+ Revision: 741990
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-4
+ Revision: 679341
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-3mdv2011.0
+ Revision: 613668
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.4-2mdv2010.1
+ Revision: 477863
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.4-1mdv2010.0
+ Revision: 394093
- update to new version 1.5.4

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 1.5.3-1mdv2009.1
+ Revision: 333196
- 1.5.3

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-3mdv2009.1
+ Revision: 322098
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-2mdv2009.0
+ Revision: 236850
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.1.3-1mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-1mdv2008.0
+ Revision: 15447
- 1.1.3


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-7mdv2007.0
+ Revision: 81607
- Import php-pear-HTML_CSS

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-1mdk
- initial Mandriva package (PLD import)

