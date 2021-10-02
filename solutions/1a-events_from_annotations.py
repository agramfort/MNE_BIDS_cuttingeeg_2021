
events, event_id = mne.events_from_annotations(raw)
event_id

epochs = mne.Epochs(raw, events, event_id, tmin, tmax, proj=True,
                    picks=picks_meg, baseline=baseline,
                    reject=reject, preload=True)
epochs
