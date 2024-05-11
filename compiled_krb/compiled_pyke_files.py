# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'fc_sickness.krb'):
           [1715428177.252724, 'fc_sickness_fc.py'],
         ('', '', 'sickness.kfb'):
           [1715428177.255996, 'sickness.fbc'],
        },
        compiler_version)

