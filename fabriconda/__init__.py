from fabric.api import cd, run
from fabric.contrib.files import exists
from fabric.context_managers import prefix

# defaults
CONDA_REPO = 'https://repo.continuum.io/miniconda/'

def install(conda_repo=CONDA_REPO, base='Miniconda2', version='latest', platform='Linux', home='~'):
    arch = 'x86' if run('uname -i') == 'i686' else 'x86_64'
    conda_vers = '%s-%s-%s-%s.sh' % (base, version, platform, arch)
    anaconda = home+'/anaconda'
    if not exists(anaconda):
        run('mkdir -p %s/downloads' % home)
        with cd(home+'/downloads'):
            run('wget -nv -N %s%s' % (conda_repo, conda_vers))
            run('bash %s -b -p %s' % (conda_vers, anaconda))

def create_env(environment_yml, name, home='~'):
    anaconda_bin = '%s/anaconda/bin' % home
    env = '%s/anaconda/envs/%s' % (home, name)
    with cd(anaconda_bin):
        if exists(env):
            run('./conda env update -f %s' % environment_yml)
        else:
            run('./conda env create -f %s' % environment_yml)

def env(name, home='~'):
    """Run with an anaconda environment"""
    return prefix('source %s/anaconda/bin/activate %s' % (home, name))
