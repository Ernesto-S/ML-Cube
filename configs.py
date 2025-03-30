import raylibpy as rl #library for displaying windows

windows_w = 600
windows_h = 450
fps = 60

#3D Camera 
camera = rl.Camera3D(
    rl.Vector3(18.0, 16.0, 18.0), # Position
    rl.Vector3(0.0, 0.0, 0.0), # Target camera center
    rl.Vector3(0.0, 1.0, 0.0), # Define up orientation
    45.0, # Field of view
    rl.CAMERA_PERSPECTIVE # Camera Mode
    )