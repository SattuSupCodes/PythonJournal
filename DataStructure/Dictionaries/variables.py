# variables are not boxes apparently

class Gizmo:
    def __init__(self):
        print(f'Gizmo id: {id(self)} ')
x = Gizmo()
    # ab ye id kya hai yaha voh bhagwaan jaane