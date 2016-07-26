"""
Define option parameters for source_separation.

Also used by feature extraction.
"""


def get_opt():
    opt = {}
    opt['features'] = 1026
    opt['timesteps'] = 8
    opt['d_path'] = '/home/alexhepburn/Documents/Datasets/Separation dataset/'
    opt['dropout'] = 0.25
    opt['layer_init'] = 'glorot_uniform'
    opt['gamma'] = 0.5  # Parameter in front of similarity term for cost.
    opt['epoch'] = 5
    opt['batch_size'] = 200
    opt['plot'] = False
    opt['n_fft'] = 1024
    return opt
