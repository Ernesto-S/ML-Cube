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
        # Generate the mesh for the cube
        self.mesh = rl.gen_mesh_cube(scale, scale, scale) # Generate a cube mesh

    def create_model(self):
        # Create the model for the cube
        self.model = rl.load_model_from_mesh(self.mesh)
        self.model.transform = rl.matrix_translate(self.position[0], self.position[1], self.position[2])

    def __repr__(self):
        return f"Cube(Model: {self.model}, Position: {self.position}, Face Color: {self.face_color})"

class Rubik:
    def __init__(self) -> None:
        self.generate_rubik(3)
        
    def generate_rubik(self, size:int):
        position = [0, 0, 0]
        piece = Cube(size, position, rl.BLACK)
        print("\n Cube Properties:")
        print("Model:", piece.model)
        print("Position:", piece.position)
        print("Face Color:", piece.face_color)
        print("\n")
        return piece