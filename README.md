Allows CNN inpainting in portraits of people, i.e. filling in face features painted over with green color. Using a TensorFlow implementation of [Image-to-Image Translation Using Conditional Adversarial Networks](https://arxiv.org/pdf/1611.07004v1.pdf) that learns a mapping from input images to output images. 

## Setup

### Prerequisites
- Linux
- Python with numpy
- NVIDIA GPU + CUDA 8.0 + CuDNNv5.1
- TensorFlow 0.11

### Getting Started
- Clone this repo:
```bash
git clone git@github.com:petee_d/face-inpainting.git
cd pix2pix-tensorflow
```
- Download the dataset:
```bash
bash ./download_dataset.sh
```
- Train the model
```bash
python main.py --phase train
```
- Test the model:
```bash
python main.py --phase test
```

## Results
TODO

## Acknowledgments
Code is an extension of [pix2pix-tensorflow](https://github.com/yenchenlin/pix2pix-tensorflow), which borrows heavily from [pix2pix](https://github.com/phillipi/pix2pix) and [DCGAN-tensorflow](https://github.com/carpedm20/DCGAN-tensorflow/blob/master/model.py). Thanks for their excellent work!

## License
MIT
