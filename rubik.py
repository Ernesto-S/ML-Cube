import raylibpy as rl
import numpy as np

class Cube:
    def __init__(self, size, position, face_color):
        self.orientation = np.eye(3) # 3x3 identity matrix
        self.size = size # size of the cube
        self.position = position
        self.face_color = face_color # color of the face

        # Initialize empy list for models and face colors
        self.model = None
        self.gen_meshe(size)

        # Create and position the meshes
        self.create_model()

    def gen_meshe(self, scale):
        # Check if scale is a tuple or a single number
        if isinstance(scale, (tuple, list)) and len(scale) == 3:
            self.mesh = rl.gen_mesh_cube(scale[0], scale[1], scale[2])  # Unpack the tuple
        elif isinstance(scale, (int, float)):
            self.mesh = rl.gen_mesh_cube(scale, scale, scale)  # Use the same value for all dimensions
        else:
            raise ValueError("Invalid scale value. Must be a number or a tuple/list of three numbers.")

    def create_model(self):
        # Create the model for the cube
        self.model = rl.load_model_from_mesh(self.mesh)
        self.model.transform = rl.matrix_translate(self.position[0], self.position[1], self.position[2])

    def __repr__(self):
        return f"Cube(Model: {self.model}, Position: {self.position}, Face Color: {self.face_color})"

class Rubik:
    def __init__(self) -> None:
        self.cubes = []
        self.generate_rubik(3)
        
    def generate_rubik(self, size:int):
        colors = [rl.BLUE, rl.GREEN, rl.ORANGE, rl.RED, rl.WHITE, rl.YELLOW]
        offset = size - 0.7 # Offset for the cubes
        size_z = size, size, size*0.1
        size_y = size, size*0.1, size
        size_x = size*0.1, size, size

        for x in range(3):
            for y in range(3):
                for z in range(3):
                    face_color = [
                        rl.BLACK if z != 2 else colors[0], # Front
                        rl.BLACK if z != 0 else colors[1], # Back
                        rl.BLACK if x != 2 else colors[2], # Right
                        rl.BLACK if x != 0 else colors[3], # Left
                        rl.BLACK if y != 2 else colors[4], # Top
                        rl.BLACK if y != 0 else colors[5]  # Bottom
                    ]

                    center_position = np.array([
                        (x - 1) * offset, # X position
                        (y - 1) * offset, # Y position
                        (z - 1) * offset  # Z position
                    ])

                    position = Cube(size, center_position, rl.BLACK)

                    # front face
                    front_position = np.array([
                        center_position[0],
                        center_position[1],
                        center_position[2] + 0.1
                    ])

                    front = Cube(size_z, front_position, face_color[0])

                    # back face
                    back_position = np.array([
                        center_position[0],
                        center_position[1],
                        center_position[2] - 0.1
                    ])
                    back = Cube(size_z, back_position, face_color[1])

                    # right face
                    right_position = np.array([
                        center_position[0] + 0.1,
                        center_position[1],
                        center_position[2]
                    ])

                    right = Cube(size_x, right_position, face_color[2])

                    # left face
                    left_position = np.array([
                        center_position[0] - 0.1,
                        center_position[1],
                        center_position[2]
                    ])

                    left = Cube(size_x, left_position, face_color[3])

                    # top face
                    top_position = np.array([
                        center_position[0],
                        center_position[1] + 0.1,
                        center_position[2]
                    ])
                    
                    top = Cube(size_y, top_position, face_color[4])

                    # bottom face
                    bottom_position = np.array([
                        center_position[0],
                        center_position[1] - 0.1,
                        center_position[2]
                    ])

                    bottom = Cube(size_y, bottom_position, face_color[5])

                    self.cubes.append([
                        position, front, back, right, left, top, bottom
                    ])
        return self.cubes