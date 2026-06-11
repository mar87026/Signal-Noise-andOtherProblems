# Failure_Log_04 | Resolving Texture Mottling in 3D Reconstruction: A Logic-Driven Approach Over Hardware Calibration

*Watch your step but don’t glue on it*

## Symptom

During the Multi-View 3D Object Reconstruction process (mapping thousands of 640x480 RGB-D frames), the final textured 3D mesh appeared heavily mottled and fragmented—resembling splotchy paint. This aesthetics failure occurred because adjacent meshes frequently selected texture sources from entirely different photographic angles.

## The Traditional CV Blind Spot

The legacy pipeline relied heavily on a 'strongest similarity metric' for feature matching. However, this approach completely ignored the ISP's physical constraints: as the camera moves, the Auto Exposure (AE) and Auto White Balance (AWB) dynamically shift. Fetching textures from drastically different views inevitably breaks color consistency.

Attempting to rectify this post-capture by tuning the hardware ISP's RGB tri-gamma curves was ruled out immediately—it was computationally prohibitive and mathematically unviable for room-scale scanning involving thousands of frames.

## Root Cause Analysis & Architectural Solution

The root cause wasn't the feature matching precision; it was the lack of **spatial coherence** in texture selection. I re-engineered the logic using a top-down, human-behavior-centric approach:

1. **IMU-Guided Pruning:** Based on the heuristic that humans **naturally look at objects horizontally when examining fine details**, we utilized IMU data to immediately filter out frames with extreme pitch or roll angles.
2. **Regional Feature Voting:** Instead of assigning texture frame-by-frame per individual mesh, we grouped them into regional features. We implemented a lightweight C++14 `std::unordered_map` to count feature frequencies. The image containing the highest concentration of features within a specific region (e.g., `image-41`) was selected as the dominant texture source for that entire spatial cluster.

Example code:

```jsx
struct Mesh {
    std::vector<int> feature_source_images; // {41, 45, 59, 61, 62}
};

// step1: global voting(buried in ORB-SLAM2 build up)
std::unordered_map<int, int> global_image_votes; 
for (const auto& mesh : all_meshes) {
    for (int img_id : mesh.feature_source_images) {
        if (imu_angle_too_large(img_id)) continue;
        global_image_votes[img_id]++;              
    }
}
// step2: make a choice
for (auto& mesh : all_meshes) {
    int best_img_id = -1;
    int max_votes = -1;
    
    for (int img_id : mesh.feature_source_images) {
        if (imu_angle_too_large(img_id)) continue;

        if (global_image_votes[img_id] > max_votes) {
            max_votes = global_image_votes[img_id];
            best_img_id = img_id;
        }
    }
    mesh.texture_source = best_img_id;
}
```