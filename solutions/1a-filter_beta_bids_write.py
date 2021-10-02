
from mne_bids import write_raw_bids

raw_beta = raw.copy().load_data().filter(13, 30, verbose=True)

# save the result
raw_beta.save('sample_audvis_beta_raw.fif', overwrite=True)
print(raw_beta.info)  # note the update of raw.info['lowpass'] and raw.info['highpass']

# Now do it with BIDS
bp_out = bp.copy().update(
    root=bids_root + "/derivatives",
    processing="filter"
)
bp_out

write_raw_bids(raw_beta, bp_out, format="FIF", overwrite=True,
               allow_preload=True, verbose=False)
bp_out.fpath
