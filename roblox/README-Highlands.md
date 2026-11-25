# HIGHLANDS — Roblox open-world landscape

Open `Highlands_OpenWorld.rbxlx` in Roblox Studio and press **Play**. The server script builds the terrain and scenery at runtime; press **Stop** to return to edit mode. Save the place from Studio after generation if you want a persistent, baked terrain copy.

## What it builds

- 512×512-stud alpine valley, procedurally sculpted with layered noise, foothills, a northern ridgeline, and material bands (grass, leafy grass, ground, rock, snow, sand).
- Water level, a carved river gorge, fir-tree clusters, trailhead lookout, path, lanterns, spawn point, and streaming enabled.
- Future lighting with atmosphere, clouds, restrained bloom, color correction, and sun rays.
- No toolbox models or third-party scripts embedded. This avoids unreviewed free models and their scripts.

## Notes

Terrain generation happens when you press Play; the `.rbxlx` begins as an editable place containing the generator. Initial generation may take a short while. Rendering quality depends on the player's graphics settings and device; Roblox does not expose desktop-style custom shaders, so the visual treatment uses supported Lighting, Atmosphere, Clouds, water, and terrain materials.

## Design references

- Roblox terrain documentation: https://create.roblox.com/docs/parts/terrain
- Roblox atmospheric effects: https://create.roblox.com/docs/environment/atmosphere
- Roblox outdoor lighting tutorial: https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments
- Open-source procedural terrain reference (MIT): https://github.com/TheArturZh/RTerrainGenerator
- Roblox runtime terrain reference (source): https://github.com/maddoxbouldin/roblox-runtime-terrain

The references inform the voxel/noise and environment approach; their code/assets are not copied into this place. Verify third-party license and inspect scripts before importing any marketplace model.
