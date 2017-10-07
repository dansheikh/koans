import trees.structs


def build_graph(inputs):
    """Build graph from sequence of values.

    Args:
        vals (list): Sequence of values.

    Returns:
        (Graph): Graph populated with provided sequence.
    """

    vals = sorted(inputs)

    def _build_nodes(vals):

        if type(vals) == int:
            return trees.structs.Node(vals, [])

        size = len(vals)

        if size == 2:
            return trees.structs.Node(vals[1], [_build_nodes(vals[0])])

        elif size == 3:
            return trees.structs.Node(vals[1], [_build_nodes(vals[0]), _build_nodes(vals[2])])

        else:
            return trees.structs.Node(vals[-2], [_build_nodes(vals[0:-2]), _build_nodes(vals[-1])])

    size = len(vals)
    mid = (size - 1) // 2
    root = trees.structs.Node(vals[mid], [_build_nodes(vals[0:mid]), _build_nodes(vals[mid + 1:size])])

    return trees.structs.Graph(root)


def in_order(node, seq=None):
    """Traverses graph in-order.

    Args:
        node (Node): Root node.

    Returns:
        seq (list): Sequence of graph values in-order.

    """

    if seq is None:
        seq = list()

    if len(node.children) >= 1:
        in_order(node.children[0], seq)

    seq.append(node.val)

    if len(node.children) >= 2:
        in_order(node.children[1], seq)

    return seq


def pre_order(node, seq=None):
    """Traverses graph in pre-order.

    Args:
        node (Node): Root node.

    Returns:
        seq (list): Sequence of graph values in pre-order.

    """

    if seq is None:
        seq = list()

    seq.append(node.val)

    if len(node.children) >= 1:
        in_order(node.children[0], seq)

    if len(node.children) >= 2:
        in_order(node.children[1], seq)

    return seq


def post_order(node, seq=None):
    """Traverses graph in post-order.

    Args:
        node (Node): Root node.

    Returns:
        seq (list): Sequence of graph values in post-order.

    """

    if seq is None:
        seq = list()

    if len(node.children) >= 1:
        in_order(node.children[0], seq)

    if len(node.children) >= 2:
        in_order(node.children[1], seq)

    seq.append(node.val)

    return seq
