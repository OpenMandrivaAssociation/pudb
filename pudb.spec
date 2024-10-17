%define name	pudb
%define version	2012.3
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %rel
%else
%define	release	%rel
%endif

Summary:	Full-screen, console-based visual debugger for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Source1:	pudb
Patch0:		setup.patch
License:	MIT
Group:		Development/Python
Url:		https://pypi.python.org/pypi/pudb/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-urwid >= 0.9.9.2
Requires:	python-pygments >= 1.0
BuildRequires:	python-setuptools

%description
PuDB is a full-screen, console-based visual debugger for Python.
It aims to provide all the niceties of modern GUI-based debuggers
in a lightweight and keyboard-friendly package. PuDB allows you
to debug code right where you write and test it - in a terminal. If
you've worked with the excellent (but nowadays ancient) DOS-based
Turbo Pascal or C tools, PuDB's UI might look familiar.

%prep
%setup -q
%patch0 -p0

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%__mkdir -p %{buildroot}%{_bindir}
%__install -m 755 %SOURCE1 %{buildroot}%{_bindir}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/pudb
%py_puresitedir/*


%changelog
* Tue Aug 07 2012 Lev Givon <lev@mandriva.org> 2012.3-1
+ Revision: 812367
- Update to 2012.3.

* Wed Jun 06 2012 Lev Givon <lev@mandriva.org> 2012.2.1-1
+ Revision: 802974
- Update to 2012.2.1.
- Don't try to download setuptools when building.

* Wed Feb 01 2012 Lev Givon <lev@mandriva.org> 2012.1-1
+ Revision: 770517
- Update to 2012.1.

* Mon Dec 05 2011 Lev Givon <lev@mandriva.org> 2011.3.1-1
+ Revision: 737944
- Update to 2011.3.1.

* Mon Aug 29 2011 Lev Givon <lev@mandriva.org> 2011.3-1
+ Revision: 697395
- Update to 2011.3.

* Wed Jun 22 2011 Lev Givon <lev@mandriva.org> 2011.2-1
+ Revision: 686707
- Update to 2011.2.

* Fri Mar 18 2011 Lev Givon <lev@mandriva.org> 2011.1-1
+ Revision: 646453
- Update to 2011.1.

* Mon Feb 14 2011 Lev Givon <lev@mandriva.org> 0.93.1-1
+ Revision: 637745
- Update to 0.93.1.

* Sun Nov 07 2010 Funda Wang <fwang@mandriva.org> 0.92.15-1mdv2011.0
+ Revision: 594707
- update file list

* Tue Jan 19 2010 Lev Givon <lev@mandriva.org> 0.92.15-1mdv2010.1
+ Revision: 493639
- Update to 0.92.15.

* Mon Dec 21 2009 Lev Givon <lev@mandriva.org> 0.92.14-1mdv2010.1
+ Revision: 480619
- Update to 0.92.14.

* Tue Nov 10 2009 Lev Givon <lev@mandriva.org> 0.92.13-1mdv2010.1
+ Revision: 464323
- Update to 0.92.13.

* Mon Sep 14 2009 Lev Givon <lev@mandriva.org> 0.92.12-1mdv2010.0
+ Revision: 441033
- Update to 0.92.12.

* Sun Jul 26 2009 Lev Givon <lev@mandriva.org> 0.92.11-1mdv2010.0
+ Revision: 399938
- Update to 0.92.11.

* Mon Jul 20 2009 Lev Givon <lev@mandriva.org> 0.92.9-1mdv2010.0
+ Revision: 398183
- Update to 0.92.9.

* Mon Jul 13 2009 Lev Givon <lev@mandriva.org> 0.92.8-1mdv2010.0
+ Revision: 395667
- imported package pudb


