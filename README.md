# Guitar Tuner

This repository contains a Python script for tuning a guitar by analyzing the frequency of played notes.

## How to Use

1. Install the required libraries.
2. Run the `SH_P3.py` script and play a guitar string.
3. The script will display the closest note and its frequency.

Recording the sound for 1 second intervals and analyzes the frequency.
Outputs the audio frequency and the analyzed note via plotting.

![image](https://github.com/GalaxyBeer/guitar-tuner/assets/72799974/f04a12cf-e90e-4c0e-810e-f293474499c2)

The frequency with the highest amplitude is determined, and the note closest to this frequency is found. The results are visualized on the screen and continuously updated. This method is a basic signal processing application based on frequency analysis and Fourier transformation.

## Requirements

- `numpy`
- `sounddevice`
- `scipy`
- `matplotlib`

## Contribution

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new pull request.
