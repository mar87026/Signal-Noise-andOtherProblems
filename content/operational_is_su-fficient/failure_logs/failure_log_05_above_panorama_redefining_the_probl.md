# Failure Log 05 | Above Panorama Redefining the Problem Before Build the Pipeline

*“Just show me the room ASAP” from CEO*

![image.png](/operational_is_su-fficient/failure_logs/failure_log_05_above_panorama_redefining_the_probl/image.png)

## Original Assumption

I was the one of team who were making 

[Failure Log 04 | Resolving Texture Mottling in 3D Reconstruction: A Logic-Driven Approach Over Hardware Calibration](/operational_is_su-fficient/failure_logs/failure_log_04_resolving_texture_mottling_in_3d_re.md)

Initially, I thought this was another 3D reconstruction problem, perhaps it just needed optimization.

However, after several discussions, I realized the product did **not** require a 3D model immediately.

It only required a new **fast visual preview**. It needed a thumbnail.

## **Discovering Panorama by Accident**

Ironically, panorama was never part of the original proposal.

While exploring possible approaches, I came across several panorama stitching techniques.

Maybe this is enough. The product didn’t need geometric accuracy. And opencv or some library else could deal  with it 😀

## **The Type Mismatch**

Like many engineers, I believed OpenCV had already solved panorama stitching.

My thoughts:

```python
Capture Images
↓
OpenCV Stitcher
↓
Done
```

Reality was different. Unfortunately, the stitching pipeline was highly integrated.

Changing feature extraction, matching strategy, descriptor formats, or integrating IMU information was much more difficult than expected.

I spent several **weeks** trying to make cv::Stitcher fit our product requirements.

That decision consumed time, but also gave me complete control.

## Choosing Features

Several feature extractors were evaluated.
•	SIFT
•	SURF
•	ORB
•	AKAZE

Technically, SIFT produced the best matches.
Its descriptors contained richer information and generally produced more stable correspondences.
However, at that time SIFT licensing was still a concern for commercial products.
AKAZE became the practical compromise.
It provided acceptable robustness while remaining suitable for deployment.

---

## Parallelizing the Pipeline

Feature extraction quickly became the computational bottleneck.
Instead of processing images sequentially, multiple stages were parallelized.
Image loading, feature extraction, descriptor computation, and matching were executed concurrently whenever possible.
This significantly reduced waiting time during capture and preview generation.

## Stitching Is Not Sequential

Most introductory tutorials demonstrate panorama stitching like this:

```python
Image1
↓
Image2
↓
Image3
↓
Image4
```

Each image is stitched onto the previous one.

But after above 45 images comes in, such more homography matrices accumulated, numerical errors also accumulated.

The panorama **started to drift.**

Instead of using the first image as the global reference, I selected a **center frame**.

Images were transformed outward from the center toward both directions.

```python
Left <- Center -> Right
```

This simple change significantly reduced accumulated distortion.

Of course it takes more time (neet to wait for whole capture process)

# IMU Was More Than Pose Estimation

Initially, I only intended to use IMU data to estimate camera orientation.

Later, I realized it could solve another problem.

A normal panorama pipeline has no idea when the user has completed a full rotation.

My application did.

Yaw information from the 6DoF IMU allowed the system to estimate when the camera was approaching the starting direction.

At that moment, the pipeline began matching the newest frames against the earliest captured frames.

Successful matching indicated that the loop had closed.

The application could immediately notify users:

Essential capture completed. Now you can take more pics for making the result completely.

# Why Cylinder Came Before Sphere

One of the largest challenges came later.

Unlike ordinary panorama capture, users had to look upward and downward to include ceilings and floors.

The obvious question became:

Should everything be projected onto a sphere?

After experimenting, I decided to postpone spherical projection.

Instead, the horizontal panorama was stabilized first using a cylindrical model.

**Very few indoor environments resemble the surface of a sphere.**

Separating horizontal stitching from ceiling/floor completion made debugging dramatically easier.

Only after the cylindrical panorama became reliable did I extend the pipeline to include upward and downward captures using IMU orientation.

# Looking Back

This project eventually became part of a commercial solution used by a real-estate platform.

Ironically, what I remember most isn’t the final panorama.

It is how many incorrect assumptions had to be discarded along the way.

And how to make the ceiling and floor normal? Inpainting?

![image.png](/operational_is_su-fficient/failure_logs/failure_log_05_above_panorama_redefining_the_probl/image_1.png)

![image.png](/operational_is_su-fficient/failure_logs/failure_log_05_above_panorama_redefining_the_probl/image_2.png)