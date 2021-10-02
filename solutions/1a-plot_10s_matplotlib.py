
%matplotlib inline

plt.close('all')
picks = mne.pick_types(raw.info, meg=False, stim=True)
imax = int(raw.info['sfreq'] * 10)
data, times = raw[picks[6], :imax]
plt.plot(times, data.T);
