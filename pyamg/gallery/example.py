"""Examples stored in files."""

import os
from glob import glob

from scipy.io import loadmat

base_dir = os.path.split(__file__)[0]
example_dir = os.path.join(base_dir, 'example_data')
example_files = glob(os.path.join(example_dir, '*.mat'))
example_names = sorted(os.path.split(name)[1][:-4] for name in example_files)


def load_example(name):
    """Load an example problem by name.

    Parameters
    ----------
    name : str
        Name of the example to load.

    Returns
    -------
    dict
        Dictionary with variable names and data.

    Notes
    -----
    Each example is stored in a dictionary with the following keys:
        - ``A``        : sparse matrix
        - ``B``        : near-nullspace candidates
        - ``vertices`` : dense array of nodal coordinates
        - ``elements`` : dense array of element indices

    Current example names are:%s
        - ``airfoil``
        - ``bar``
        - ``helmholtz_2D``
        - ``knot``
        - ``local_disc_galerkin_diffusion``
        - ``recirc_flow``
        - ``unit_cube``
        - ``unit_square``

    Examples
    --------
    >>> from pyamg.gallery import load_example
    >>> ex = load_example('knot')

    """
    if name not in example_names:
        raise ValueError(f'No example with name {name}')

    return loadmat(os.path.join(example_dir, name + '.mat'), struct_as_record=True)
