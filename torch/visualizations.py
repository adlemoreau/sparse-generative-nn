import argparse
import numpy as np
import plotly.graph_objects as go
from plyfile import PlyData
from plotly.offline import iplot


parser = argparse.ArgumentParser(description="Adding flags to specify path of the 3D model to visualize.")
parser.add_argument('--room_id', required=True, help="Give the id of the 3D model to visualize.", type=str)
parser.add_argument('--room_index', required=True, help="Give the index of the 3D model to visualize.", type=int)
args = parser.parse_args()


def load_ply_file(file_path):
    """Load a PLY file and extract vertices and faces."""
    ply_data = PlyData.read(file_path)
    vertices = np.array([(vertex['x'], vertex['y'], vertex['z']) for vertex in ply_data['vertex']])
    faces = np.array([list(face) for face in ply_data['face']['vertex_indices']])
    return vertices, faces


def display_3d_model(path_model):
    """Display a 3D model using Plotly."""
    
    # Load models
    if path_model.endswith('ply'):
        vertices, faces = load_ply_file(path_model)
    else:
        return "Wrong format, only ply files are supported."

    print(len(vertices), len(faces))

    # Extract x, y, z coordinates from vertices
    x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]

    mesh = go.Mesh3d(
        x=x,
        y=y,
        z=z,
        i=faces[:, 0],
        j=faces[:, 1],
        k=faces[:, 2],
        opacity=1,
        #color='rgba(0,0,0,0.5)'
        color = 'skyblue'
        )

    layout = go.Layout(
        scene=dict(
            aspectmode='data',
            camera=dict(eye=dict(x=1.25, y=1.25, z=1.25)),
            xaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                showbackground=False,
                title='',
            ),
            yaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                showbackground=False,
                title='',
            ),
            zaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                showbackground=False,
                title='',
            ),
            
        )
    )

    fig = go.Figure(data=mesh, layout=layout)
    fig.update_layout(width=1000, height=1000)
    
    # Show the figure
    fig.show()
    #iplot(fig)


if __name__ == "__main__":
    ROOM_ID = args.room_id
    ROOM_INDEX = args.room_index 
    PATH_INPUT = f"output/{ROOM_ID}_room{ROOM_INDEX}__0__input-mesh.ply"
    PATH_OUTPUT = f"output/{ROOM_ID}_room{ROOM_INDEX}__0__pred-mesh.ply"
    
    display_3d_model(PATH_INPUT), display_3d_model(PATH_OUTPUT)