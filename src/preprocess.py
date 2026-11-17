import pandas as pd

def align_sensor_clock(frame):
    frame = frame.sort_values('timestamp').reset_index(drop=True)
    frame['timestamp'] = pd.to_datetime(frame['timestamp'], utc=True)
    return frame

def remove_shaded_sections(frame, shade_mask):
    keep = frame.loc[~shade_mask].copy()
    return keep.dropna(subset=['temperature_c', 'humidity_pct'])
