%define name	pudb
%define version	2012.1
%define release %mkrel 2

Summary:	Full-screen, console-based visual debugger for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
Source1:	pudb
Patch0:		setup.patch
License:	MIT
Group:		Development/Python
Url:		http://pypi.python.org/pypi/pudb/
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
