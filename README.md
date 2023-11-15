# 8K-Dataset-MP
Repository which contains scripts for the pipeline and evaluation of a 8K resolution Video Dataset

## Downscale videos
- Downscale the videos using FFmpeg and nearest neighbour scaling
> https://www.ffmpeg.org/

## Calculate Full Reference Metric(s)
- Upscale the previously downscaled video with nearest neighbour scaling and calculate PSNR and SSIM values between scaled and reference video
> https://github.com/slhck/ffmpeg-quality-metrics

## SI/TI calculation
- Calculate SI and TI values
> https://github.com/VQEG/siti-tools

## Dynamic Range utilization
- Calculate Pixel-Based Dynamic Range (DR) and Image Key (IK) as they are objective metrics which correlate with perceived dynamic range according to:
> https://ieeexplore.ieee.org/document/7498953
- $` DR = log_{10} (L_{max} / L_{min} ) `$
> where the Lmin and Lmax are the minimum and maximum relative luminance values of the images respectively, computed after excluding 1% of darkest and brightest pixels.
- $` IK = (logL_{avg} - logL_{min}) / (logL_{max} - logL_{min}) `$
> where the Lavg is computed as logLavg=Σijlog(L(i,j)+δ)/N, <b> δ is a small value (typically 10*e−5) used to avoid the singularity occurring for the black pixels, and N is the number of pixels in the L(i,j) image. Both Lmin and Lmax are calculated robustly, after excluding the 1% of the darkest and the brightest pixels.

## Coding Research suitability
- Inspect File Size after Compression with different video compression standards
- Calculating scene criticality and compressibility according to:
> https://ieeexplore.ieee.org/document/7265973

## Aesthetics and appeal
- Calculate Aesthetics and appeal using Neural Image Assessment (NIMA)
> https://github.com/idealo/image-quality-assessment 
