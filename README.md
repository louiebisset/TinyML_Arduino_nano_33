# TinyML on the Arduino Nano 33

Experiments with the Arduino Nano 33 [BLE Sense / variant] as a starting point for on-device machine learning with a camera.

## Projects

| Project | What it does |
|---|---|
| [TestingCam](TestingCam) | Streams live grayscale video from an OV7675 camera on the Arduino to a laptop, and saves frames for building an image dataset |

## TestingCam

The Arduino reads frames from an OV7675 camera and sends them over USB serial to a Python viewer on a laptop, which shows the live image. Pressing a key in the viewer saves the current frame as a PNG, so the setup can be used to collect training images for a model.

- Camera: OV7675, QCIF resolution (176 x 144), 8-bit grayscale, 5 fps
- Serial speed: 1,000,000 baud
- Each frame is preceded by a `FRAM` marker so the laptop can stay in sync

## Hardware

- Arduino Nano 33 BLE Sense
- OV7675 camera module
- Tiny Machine Learning Shield 

## Getting started

### Controls

| Key | Action |
|---|---|
| `s` | Save the current frame as `sign_0000.png`, `sign_0001.png`, ... |
| `q` | Quit |

## Next steps

- [e.g. train an image classification model on the saved frames and run it on the Arduino]
