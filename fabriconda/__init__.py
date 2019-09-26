# defaults
CONDA_REPO = 'https://repo.continuum.io/miniconda/'

def uname_platform(ctx):
    res = ctx.run('uname -i', hide=True)
    return res.stdout.strip()

def exists(ctx, path):
    cmd = f'test -e "$(echo {path})"'
    return ctx.run(cmd, hide=True, warn=True).ok

def install(ctx, conda_repo=CONDA_REPO, base='Miniconda3', version='latest', platform='Linux', home='~'):
    arch = 'x86' if uname_platform(ctx) == 'i686' else 'x86_64'
    conda_vers = '%s-%s-%s-%s.sh' % (base, version, platform, arch)
    anaconda = home+'/anaconda'
    if not exists(ctx, anaconda):
        ctx.run('mkdir -p %s/downloads' % home)
        with ctx.cd(home+'/downloads'):
            ctx.run('wget -nv -N %s%s' % (conda_repo, conda_vers))
            ctx.run('bash %s -b -p %s' % (conda_vers, anaconda))

def create_env(ctx, environment_yml, name, home='~'):
    anaconda_bin = '%s/anaconda/bin' % home
    env = '%s/anaconda/envs/%s' % (home, name)
    with ctx.cd(anaconda_bin):
        if exists(env):
            ctx.run('./conda env update -f %s -n %s' % (environment_yml, name))
        else:
            ctx.run('./conda env create -f %s -n %s' % (environment_yml, name))

def env(ctx, name, home='~'):
    """Run with an anaconda environment"""
    return ctx.prefix('source %s/anaconda/bin/activate %s' % (home, name))
