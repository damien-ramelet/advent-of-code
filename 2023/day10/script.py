<<<<<<< Updated upstream
#with open("test_input") as f:
#    content = f.readlines()
#
#print("##### TEST INPUT #####")

with open("input") as f:
    content = f.readlines()

=======
with open("test_input") as f:
    content = f.readlines()

print("##### TEST INPUT #####")

#with open("input") as f:
#    content = f.readlines()

>>>>>>> Stashed changes
class Tree:
    def __init__(self, content):
        self.raw_content = content
        self.starting_node: Node | None = None
        self.nodes: dict[tuple[int, int], "Node"] = {}
        self.path: list["Node"] = []
<<<<<<< Updated upstream
        self.corners: list["Node"] = []
=======
>>>>>>> Stashed changes

    def build(self):
        for line, chars in enumerate(content):
            for column, char in enumerate(chars):
                if char in (".", "\n"):
                    continue
                elif char == "S":
                    self.starting_node = self.build_node(char, (line, column))
                    self.nodes[(line, column)] = self.starting_node
                else:
                    self.nodes[(line, column)] = node = self.build_node(char, (line, column))

    def build_node(self, representation: str, coordinates: tuple[int, int]) -> "Node":
        line, column = coordinates
        node = self.get_or_create_node(representation=representation, coordinates=coordinates)

        try:
            north_contiguous_node = self.raw_content[line-1][column]
        except IndexError:
            north_contiguous_node = None
        north_contiguous_coodinates = (line-1, column)

        try:
            south_contiguous_node = self.raw_content[line+1][column]
        except IndexError:
            south_contiguous_node = None
        south_contiguous_coordinates = (line+1, column)

        try:
            west_contiguous_node = self.raw_content[line][column-1]
        except IndexError:
            west_contiguous_node = None
        west_contiguous_coordinates = (line, column-1)

        try:
            east_contiguous_node = self.raw_content[line][column+1]
        except IndexError:
            east_contiguous_node = None
        east_contiguous_coordinates = (line, column+1)

        if north_contiguous_node and north_contiguous_node != "." and north_contiguous_coodinates not in node.contiguous_nodes and str(node) in "S|LJ" and north_contiguous_node in "S|F7":
            north_node = self.get_or_create_node(representation=north_contiguous_node, coordinates=north_contiguous_coodinates)
            node.contiguous_nodes.add(north_node)

        if south_contiguous_node and south_contiguous_node != "." and south_contiguous_node not in node.contiguous_nodes and str(node) in "S|F7" and south_contiguous_node in "S|LJ":
            south_node = self.get_or_create_node(representation=south_contiguous_node, coordinates=south_contiguous_coordinates)
            node.contiguous_nodes.add(south_node)

        if east_contiguous_node and east_contiguous_node != "." and east_contiguous_coordinates not in node.contiguous_nodes and str(node) in "S-FL" and east_contiguous_node in "S-7J":
            east_node = self.get_or_create_node(representation=east_contiguous_node, coordinates=east_contiguous_coordinates)
            node.contiguous_nodes.add(east_node)

        if west_contiguous_node and west_contiguous_node != "." and west_contiguous_coordinates not in node.contiguous_nodes and str(node) in "S-7J" and west_contiguous_node in "S-FL":
            west_node = self.get_or_create_node(representation=west_contiguous_node, coordinates=west_contiguous_coordinates)
            node.contiguous_nodes.add(west_node)

        return node

    def get_or_create_node(self, *, representation: str, coordinates: tuple[int, int]):
        if coordinates in self.nodes:
            return self.nodes[coordinates]
        else:
            node = Node(representation=representation, coordinates=coordinates)
            self.nodes[coordinates] = node
            return node

    def find_loop(self):
        assert self.starting_node
        previous_node = None
        current_node = self.starting_node
        while True:
            next_node = current_node.next_node(previous_node)
            if next_node != self.starting_node:
<<<<<<< Updated upstream
                if current_node.is_corner and current_node not in self.corners:
                    self.corners.append(current_node)
=======
>>>>>>> Stashed changes
                self.path.append(current_node)
                previous_node = current_node
                current_node = next_node
            else:
                break
<<<<<<< Updated upstream
    @property
    def surface(self):
        if not self.path:
            raise AssertionError

        surface = 0
        self.corners.append(self.corners[0])

        for i in range(0, len(self.corners), 4):
            a = self.path[i].coordinates
            b = self.path[i+1].coordinates
            c = self.path[i+2].coordinates

            x = abs(max((a[0] - b[0]), a[1] - b[1])) - 1
            y = abs(max((b[0] - c[0]), b[1] - c[1])) - 1

            surface += (x*y)

        return surface



=======
>>>>>>> Stashed changes

class Node:
    representation: str
    coordinates: tuple[int, int]
    contiguous_nodes: set["Node"]

    def __init__(self, *, representation: str, coordinates: tuple[int, int]):
        self.representation = representation
        self.coordinates = coordinates
        self.contiguous_nodes = set()
        self.is_dead_end = False

    def __str__(self):
        return self.representation

    def __repr__(self):
        return f"< {self.representation} at (line: {self.coordinates[0]}, column: {self.coordinates[1]})>"

    def __hash__(self):
        return hash(self.coordinates)

    def next_node(self, previous_node: "Node | None" = None):
        if previous_node is None:
            return list(self.contiguous_nodes)[0]
        else:
            for node in self.contiguous_nodes:
                if node is previous_node:
                    continue
                else:
                    return node
            else:
                raise AssertionError

<<<<<<< Updated upstream
    @property
    def is_corner(self) -> bool:
        return self.representation in "SLJF7"

=======
>>>>>>> Stashed changes


if __name__ == "__main__":
    tree = Tree(content)
    tree.build()
    assert tree.starting_node
    tree.find_loop()
    print(tree.path)
<<<<<<< Updated upstream
    print(len(tree.corners))
    print(f"Total loop length is: {len(tree.path)} - Solution is: {(len(tree.path) + 1) / 2}")
    print(f"Surface is: {tree.surface}")
=======
    print(f"Total loop length is: {len(tree.path)} - Solution is: {(len(tree.path) + 1) / 2}")
>>>>>>> Stashed changes

