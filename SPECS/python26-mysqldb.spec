%define __python /usr/bin/python2.6

# Python major version.
%{expand: %%define pyver %(%{__python} -c 'import sys;print(sys.version[0:3])')}

%define pybase_ver 26
%define real_name MySQL-python
%define name python%{pybase_ver}-mysqldb

Summary: An interface to MySQL
Name: %{name}
Version: 1.2.3c1
Release: 1.ius%{?dist}
License: GPL
Group: Development/Libraries
Source0: http://prdownloads.sourceforge.net/mysql-python/MySQL-python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://sourceforge.net/projects/mysql-python/
Requires: python%{pybase_ver}, mx, mysql
Requires: python%{pybase_ver} >= %{pyver}
BuildRequires: python%{pybase_ver}-devel >= %{pyver}, openssl-devel
BuildRequires: mysql-devel, python%{pybase_ver}, python%{pybase_ver}-setuptools 
BuildRequires: Distutils, gcc, zlib-devel

%description
Python interface to MySQL

MySQLdb is an interface to the popular MySQL database server for Python.
The design goals are:

-     Compliance with Python database API version 2.0 
-     Thread-safety 
-     Thread-friendliness (threads will not block each other) 
-     Compatibility with MySQL 3.23 and up

This module should be mostly compatible with an older interface
written by Joe Skinner and others. However, the older version is
a) not thread-friendly, b) written for MySQL 3.21, c) apparently
not actively maintained. No code from that version is used in
MySQLdb. MySQLdb is distributed free of charge under a license
derived from the Python license.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__rm} -f doc/*~
export libdirname=%{_lib}
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT

export libdirname=%{_lib}
%{__python} setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README doc/*
%dir /usr/%{_lib}/python%{pyver}/site-packages/MySQLdb
/usr/%{_lib}/python%{pyver}/site-packages/MySQLdb/*.pyo
/usr/%{_lib}/python%{pyver}/site-packages/MySQLdb/constants/*.pyo
/usr/%{_lib}/python%{pyver}/site-packages/*.pyo
%dir /usr/%{_lib}/python%{pyver}/site-packages/MySQLdb/constants

%changelog
* Mon Aug 24 2009 BJ Dierkes <wdierkes@rackwpace.com> 1.2.3c1-1.ius
- Rebuilding for IUS
- Latest sources from upstream
- Renaming as python26-mysql

* Fri Jul 21 2006 Tom Lane <tgl@redhat.com> 1.2.1-1
- Update to 1.2.1
- Remove hardwired python version number in favor of asking Python

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.0-3.2.2.1
- rebuild

* Mon Feb 13 2006 Jesse Keating <jkeating@redhat.com> - 1.2.0-3.2.2
- rebump for build order issues during double-long bump

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.2.0-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.2.0-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov  9 2005 Tom Lane <tgl@redhat.com> 1.2.0-3
- Rebuild due to mysql 5.0 update and openssl library update.

* Wed Aug 03 2005 Karsten Hopp <karsten@redhat.de> 1.2.0-2
- package all python files. INSTALLED_FILES doesn't contain files created
  by the brp-python-bytecompile script

* Thu Apr 21 2005 Tom Lane <tgl@redhat.com> 1.2.0-1
- Update to 1.2.0, per bug #155341
- Link against mysql 4.x not 3.x, per bug #150828

* Sun Mar  6 2005 Tom Lane <tgl@redhat.com> 1.0.0-3
- Rebuild with gcc4.

* Thu Nov 11 2004 Tom Lane <tgl@redhat.com> 1.0.0-2
- bring us to python 2.4

* Thu Nov 11 2004 Tom Lane <tgl@redhat.com> 1.0.0-1
- update to 1.0.0; rebuild against mysqlclient10

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 20 2004 Tom Lane <tgl@redhat.com>
- reinstate (and update) patch for /usr/lib64 compatibility
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Nov 25 2003 Patrick Macdonald <patrickm@redhat.com> 0.9.2-1
- update to 0.9.2
- remove patches (no longer applicable)

* Sat Nov 15 2003 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.1-10
- bring us to python 2.3

* Thu Jul 03 2003 Patrick Macdonald <patrickm@redhat.com> 0.9.1-9
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com> 0.9.1-8
- rebuilt

* Tue Mar 04 2003 Patrick Macdonald <patrickm@redhat.com> 0.9.1-7
- explicitly define the constants directory in case a more
  restrictive umask is encountered (#74019)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.9.1-5
- lib64'ize

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.1-2
- Build for newer python

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.1-1
- 0.9.1

* Tue Feb 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.9.0-6
- Rebuild

* Thu Jan 31 2002 Elliot Lee <sopwith@redhat.com> 0.9.0-5
- Change python conflicts to requires
- Use pybasever/pynextver macros.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Sep 14 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.9.0-3
- Build for Python 2.2

* Mon Jul 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add zlib-devel to buildrequires (#49788)

* Tue Jun 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Initial build
