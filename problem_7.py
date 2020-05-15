# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler=handler)

    def insert(self, req, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        sub = req.split("/")
        if len(sub) <= 1:
            return

        cur = self.root
        for sub_path in sub[1:]:
            if sub_path in cur.sub:
                cur = cur.sub[sub_path]
            else:
                child_n = RouteTrieNode()
                cur.sub[sub_path] = child_n
                cur = child_n
        cur.handler = handler

    def find(self, req):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        if req[-1] == "/":
            req = req[:-1]
        sub = req.split("/")
        cur = self.root
        if len(sub) <= 1:
            return cur.handler
        for sub_path in sub[1:]:
            if sub_path in cur.sub:
                cur = cur.sub[sub_path]
            else:
                return None

        return cur.handler

    def __str__(self):
        output_str = [""]

        def print_node(node, output_str):
            output_str[0] += f"Node handler: {node.handler}\n"
            for sub_path in node.sub:
                output_str[0] += f"Sub path: {sub_path}\n"

                print_node(node.sub[sub_path], output_str)

        print_node(self.root, output_str)

        return output_str[0]


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler

        # A dictionary of sub-paths to it's corresponding child RouteTrieNode
        self.sub = dict()

    def insert(self, sub_path, handler=None):
        # Insert the node as before
        route_trie_node = RouteTrieNode(handler)
        self.sub[sub_path] = route_trie_node


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler=None, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler=root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, req, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(req, handler)

    def lookup(self, req):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        handler = self.route_trie.find(req)

        if handler is None:
            return self.not_found_handler
        else:
            return handler


# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one