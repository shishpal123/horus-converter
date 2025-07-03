from scipy.io import wavfile
import pandas as pd

def convert_audio_to_horus(input_path, output_path):
    rate, data = wavfile.read(input_path)
    if data.ndim == 2 and data.shape[1] == 2:
        df = pd.DataFrame(data, columns=['Ch1', 'Ch2'])
    else:
        df = pd.DataFrame(data, columns=['Ch1'])
    df.to_csv(output_path, index=False)
