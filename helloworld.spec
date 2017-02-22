Name:           helloworld
Version:        1.0
Release:        2
License:        GPL-2.0+
Source:         helloworld-1.0.tar.gz
Group:          Productivity/Other
Summary:        Test helloworld   

# List of additional build dependencies
BuildRequires:  gcc-c++ , libstdc++-devel, automake  
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
helloworld-1.0


%prep
%setup -q

%build

# Assume that the package is built by plain 'make' if there's no ./configure.
# This test is there only because the wizard doesn't know much about the
# package, feel free to clean it up
if test -x ./configure; then
	%configure
fi
make

    

%install

make DESTDIR=%buildroot install



# Write a proper %%files section and remove these two commands and
# the '-f filelist' option to %%files
echo '%%defattr(-,root,root)' >filelist
find %buildroot -type f -printf '/%%P*\n' >>filelist


%clean
rm -rf %buildroot

%files -f filelist
%defattr(-,root,root)

# This is a place for a proper filelist:
# /usr/bin/Qt4
# You can also use shell wildcards:
# /usr/share/Qt4/*
# This installs documentation files from the top build directory
# into /usr/share/doc/...
# %doc README COPYING
# The advantage of using a real filelist instead of the '-f filelist' trick is
# that rpmbuild will detect if the install section forgets to install
# something that is listed here


%changelog
* Tue Feb 21 2017 Liang Yan <lyan@suse.com> 1.0
- Build for 1.0.
