# Introduction

This repository is my personal research notebook.  
It serves as a collection of surface-reconstruction–related papers that I come across anytime and anywhere.

## Paper lists
> This repo. just roughly records the contributions of each paper (Why->What->How). My notes are mainly recorded on Notion.

![Static Badge](https://img.shields.io/badge/Surface_Reconstruction-%E8%9C%98%E8%9B%9B%E7%A7%91%E5%AD%A6%E5%AE%B6-critical?style=flat&logo=notion&labelColor=auto&link=https%3A%2F%2Fwww.notion.so%2FNotes-2b13db23b7038076a17bef7408d980e7%3Fsource%3Dcopy_link)

### Extensive Reading

### Intensive Reading
- __NeuSG: Neural Implicit Surface Reconstruction with 3D Gaussian Splatting Guidance.__ _Hanlin Chen et.al._ __ArXiv, 2023.__ [[`Paper`](https://arxiv.org/pdf/2312.00846)] [`No Code`] (★★☆☆☆)
  - Scale regularization (the basis of follow-up 3d Gaussian planes).
  - Surface normal alignment of NeuS.

- __SuGaR: Surface-Aligned Gaussian Splatting for Efficient 3D Mesh Reconstruction and High-Quality Mesh Rendering.__ _Antoine Guédon, Vincent Lepetit._ __CVPR, 2024.__ [[`Paper`](https://arxiv.org/pdf/2311.12775)] [[`Code`](https://github.com/Anttwo/SuGaR)] (★★☆☆☆)(No reading code)
  - To reduce interference from overlapping Gaussians, the Gaussian nearest to the point $p$ is selected. \
    The SDF is then defined by shortening the distance along its smallest scale axis, and this estimated SDF is regularized toward the ground-truth SDF to achieve surface alignment.

- __2D Gaussian Splatting for Geometrically Accurate Radiance Fields.__ _Binbin Huang et.al._  __SIGGRAPH, 2024.__ [[`Paper`](https://arxiv.org/pdf/2403.17888)] [[`Code`](https://github.com/hbb1/2d-gaussian-splatting)] (★★★★☆)
  - __Initialize 2D Gaussian primitives__ to ensure multi-view consistency, and use __homogeneous transformations__ to remove the errors introduced by affine projection approximations.

- __High-quality Surface Reconstruction using Gaussian Surfels.__ _Pinxuan Dai, Jiamin Xu et.al._ __SIGGRAPH, 2024.__ [[`Paper`](https://arxiv.org/pdf/2404.17774)] [[`Code`](https://github.com/turandai/gaussian_surfels)] (★★★★☆)
  - Introduces Gaussian surfels (with scale.z = 0) and __adaptively adjusts pixel-wise depths__ when the surfels align with slanted surfaces.

- __Gaussian Opacity Fields: Efficient Adaptive Surface Reconstruction in Unbounded Scenes.__ _Zehao Yu et.al._ __TOG, 2024.__ [[`Paper`](https://arxiv.org/pdf/2404.10772)] [[`Code`](https://github.com/autonomousvision/gaussian-opacity-fields)] (★★★☆☆)

- __RaDe-GS: Rasterizing Depth in Gaussian Splatting.__ _Baowen Zhang et.al._ __ArXiv, 2024.__ [[`Paper`](https://arxiv.org/pdf/2406.01467)] [[`Code`](https://github.com/HKUST-SAIL/RaDe-GS)] (Unread)


- __PGSR: Planar-based Gaussian Splatting for Efficient and High-Fidelity Surface Reconstruction.__ _Danpeng Chen et.al._ __TVCG, 2024__ [[`Paper`](https://arxiv.org/pdf/2406.06521)] [[`Code`](https://github.com/zju3dv/PGSR)] (★★★☆☆)


- __GS-ROR2: Bidirectional-guided 3DGS and SDF for Reflective Object Relighting and Reconstruction.__ _Zuoliang Zhu et.al._ __ACM TOG, 2025.__ [[`Paper`](https://arxiv.org/pdf/2406.18544)] [[`Code`](https://github.com/NK-CS-ZZL/GS-ROR/tree/main)]
  
- __GS-2M: Gaussian Splatting for Joint Mesh Reconstruction and Material Decomposition.__ _D. M. Nguyen et.al._ __ArXiv, 2025.__ [[`Paper`](https://arxiv.org/pdf/2509.22276)] [[`Code`](https://github.com/ndming/GS-2M/tree/main)] [[`Note`]()] (Unread)

- __VCR-GauS: View Consistent Depth-Normal Regularizer for Gaussian Surface Reconstruction.__ _Hanlin Chen et.al._ __NIPS, 2024.__ [[`Paper`](https://proceedings.neurips.cc/paper_files/paper/2024/file/fc9f83d9925e6885e8f1ae1e17b3c44b-Paper-Conference.pdf)] [[`Code`](https://github.com/HLinChen/VCR-GauS)]

  - 
## Extension (Preparing)

- __GVKF: Gaussian Voxel Kernel Functions for Highly Efficient Surface Reconstruction in Open Scenes.__ _Gaochao Song, Chong Cheng et.al._ __NeurIPS, 2025.__ [[`Paper`](https://arxiv.org/pdf/2411.01853)] [[`Code`](https://github.com/3DAgentWorld/GVKF/tree/main)] [[`Note`]()]

- __GausSurf: Geometry-Guided 3D Gaussian Splatting for Surface Reconstruction.__ _Jiepeng Wang et.al._ __ArXiv, 2024.__ [[`Paper`](https://arxiv.org/pdf/2411.19454)] [[`Code`](https://github.com/jiepengwang/GausSurf)] (Unread)

- __αSurf: Implicit Surface Reconstruction for Semi-Transparent and Thin Objects with Decoupled Geometry and Opacity.__ _Keyang Ye et.al._ __3DV, 2025.__ [[`Paper`](https://arxiv.org/pdf/2303.10083)] [[`Code`](https://github.com/ChikaYan/alphasurf)]  (Unread)

- __Volumetric Surfaces: Representing Fuzzy Geometries with Layered Meshes.__ _Stefano Esposito et.al._ __CVPR, 2025.__ [[`Paper`](https://arxiv.org/pdf/2409.02482)] [[`Code`](https://github.com/autonomousvision/volsurfs/tree/main)]  (Unread)

- __When Gaussian Meets Surfel: Ultra-fast High-fidelity Radiance Field Rendering.__ _Keyang Ye et.al._ __TOG, 2025.__ [[`Paper`](https://arxiv.org/pdf/2504.17545)] [`No Code`] (Unread)

- __Quadratic Gaussian Splatting: High Quality Surface Reconstruction with Second-order Geometric Primitives.__ _Ziyu Zhang, Binbin Huang et.al._  __ICCV, 2025.__ [[`Paper`](https://arxiv.org/pdf/2411.16392)] [[`Code`](https://github.com/will-zzy/QGS)] (★★★★☆)

- __MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions.__ _Qingyuan Zhou et.al._ __ICCV, 2025.__ [[`Paper`](https://arxiv.org/pdf/2503.05182)] [[`Code`](https://github.com/TsingyuanChou/MGSR)] (Unread)

- __MILo: Mesh-In-the-Loop Gaussian Splatting for Detailed and Efficient Surface Reconstruction.__ _Antoine Guédon, Diego Gomez et.al._ __TOG, 2025.__ [[`Paper`](https://arxiv.org/pdf/2506.24096)] [[`Code`](https://github.com/Anttwo/MILo)] (Unread)
- 

reference
- High-Quality Surface Splatting on Today's GPUs. gaussian filter in 2dgs
  - anti-aliasing in magnified as well as in minified regions
