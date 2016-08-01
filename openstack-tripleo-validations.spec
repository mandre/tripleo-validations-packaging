%{!?upstream_version: %global upstream_version %{version}}
%global upstream_name tripleo-validations
%global with_doc %{!?_without_doc:1}%{?_without_doc:0}

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
Requires:       python-pbr
Requires:       python-setuptools

Provides:  tripleo-validations = %{version}-%{release}
Obsoletes: tripleo-validations < %{version}-%{release}

%description
A collection of Ansible playbooks to detect and report potential issues during
TripleO deployments.

%package -n openstack-tripleo-validations-tests
Summary:        Tests for TripleO validations
Requires:       %{name} = %{version}-%{release}

BuildRequires:  python-hacking
BuildRequires:  python-coverage
BuildRequires:  python-subunit
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-oslotest
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
BuildRequires:  python-netaddr

Requires:       python-hacking
Requires:       python-coverage
Requires:       python-subunit
Requires:       python-sphinx
Requires:       python-oslo-sphinx
Requires:       python-oslotest
Requires:       python-testrepository
Requires:       python-testscenarios
Requires:       python-testtools
Requires:       python-netaddr

%description -n openstack-tripleo-validations-tests
This package contains the tripleo-validations test files.

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

# docs generation
export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
%if 0%{?with_doc}
SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo
%endif
popd

%check
%{__python2} setup.py testr

%files
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%doc doc/build/html
%{python2_sitelib}/tripleo_validations*
%{python2_sitelib}/*-*.egg-info
%{_datadir}/%{name}
%exclude %{python2_sitelib}/tripleo_validations/test*

%files -n openstack-tripleo-validations-tests
%license LICENSE
%{python2_sitelib}/tripleo_validations/tests

%changelog
