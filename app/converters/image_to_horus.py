from skimage import io
import pandas as pd

def convert_image_to_horus(input_path, output_path):
    data = io.imread(input_path)
    height, width, _ = data.shape
    rows = []
    for x in range(height):
        for y in range(width):
            r, g, b = data[x, y]
            rows.append([x, y, r, g, b])
    df = pd.DataFrame(rows, columns=['XAxis', 'YAxis', 'Red', 'Green', 'Blue'])
    df.to_csv(output_path, index=False)

