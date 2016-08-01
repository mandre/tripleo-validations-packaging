%{!?upstream_version: %global upstream_version %{version}}
%global upstream_name tripleo-validations

Name:           openstack-tripleo-validations
Summary:        Ansible playbooks to detect potential issues with TripleO deployments
Version:        XXX
Release:        XXX
License:        ASL 2.0
URL:            http://tripleo.org
Source0:        http://tarballs.openstack.org/tripleo-validations/tripleo-validations-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
Requires:       ansible >= 2

Provides:  tripleo-validations = %{version}-%{release}
Obsoletes: tripleo-validations < %{version}-%{release}

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git
rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

# Documentation
sphinx-build -b html doc/source doc/build/html
install -d -m 755 %{buildroot}%{_datadir}/doc/%{name}/html
cp -r doc/build/html/* %{buildroot}%{_datadir}/doc/%{name}/html

%description
A collection of Ansible playbooks to detect and report potential issues during
TripleO deployments.

%package -n openstack-tripleo-validations-tests
Summary:        Tests for TripleO validations
Requires:       openstack-tripleo-validations = %{version}-%{release}

%description -n openstack-tripleo-validations-tests
This package contains the tripleo-validations test files.

%files
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{python2_sitelib}/tripleo_validations*
%exclude %{python2_sitelib}/tripleo_validations/test*
%{_datadir}/%{name}
%{_defaultdocdir}/%{name}

%files -n openstack-tripleo-validations-tests
%license LICENSE
%{python2_sitelib}/tripleo_validations/tests

%changelog
