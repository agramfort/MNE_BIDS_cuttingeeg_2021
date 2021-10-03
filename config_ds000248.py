study_name = 'ds000248'
bids_root = './ds000248'
deriv_root = f'{bids_root}/../derivatives/mne-bids-pipeline/'
subjects_dir = f'{bids_root}/derivatives/freesurfer/subjects'

subjects = ['01']
conditions = ['Auditory', 'Visual', 'Auditory/Left', 'Auditory/Right']
contrasts = [('Visual', 'Auditory'),
             ('Auditory/Right', 'Auditory/Left')]

decode = False  # True if you want to do time by time decoding

# Uncomment next for time-frquency
# time_frequency_conditions = ['Auditory', 'Visual']

ch_types = ['meg']
reject = dict(grad=4000e-13, mag=4e-12, eog=150e-6)  # this can be highly data dependent
# reject = "autoreject_global"

# Maxwell filter (uncomment if needed)
# mf_reference_run = '01'
# find_flat_channels_meg = True
# find_noisy_channels_meg = True
# use_maxwell_filter = True

process_er = True
noise_cov = 'emptyroom'

spatial_filter = 'ssp'
n_proj_eog = dict(n_mag=1, n_grad=1, n_eeg=1)
n_proj_ecg = dict(n_mag=1, n_grad=1, n_eeg=0)
ecg_proj_from_average = True
eog_proj_from_average = False

bem_mri_images = 'FLASH'
recreate_bem = False  # set to True if you don't have any
recreate_scalp_surface = False  # set to True if you don't have any

on_error = 'debug'
