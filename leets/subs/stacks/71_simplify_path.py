class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        TIME: Always O(n) because we loop over the entire path
        MEMORY: Always O(n) because we store the parts in a stack, which scales matching the input size

        ##stacks
        """
        root = "/"
        if path == root:
            return path
        
        # Example for "/usr//../j/"
        # [/]
        # [/usr//] <- SQUASH SLASHES: adding a '/'? peek n pop to avoid adding double
        # [/usr/..] <- TRAVERSE DIRS: adding a 2nd '.'? pop until previous dir removed (until we hit a '/')
        # [/usr/../j/] <--- TRIM END: last char? skip if '/'
        # [/usr/j]
        # Response is "/usr/j"
        stack = [] # parts are pushed, not always single chars (part can be single though)
        curr_part = ""

        for idx, char in enumerate(path):
            # print(f'[{ ", ".join(stack) }]')

            # 1. Handle normal chars "abc123..."
            if char != "/":
                curr_part += char

            # 2. Skip the rest unless we are dealing w a slash OR the final part
            if char != "/" and idx != len(path) - 1:
                continue

            # print(f"Encountered a slash or this is the final part: {curr_part}")
            # 3. Skip if empty or we're traversing to the current dir
            if curr_part == ".":
                curr_part = ""
            # 4. Traverse back to parent dir
            elif curr_part == "..":
                if stack:
                    stack.pop()
                curr_part = ""
            # 5. Push the valid part
            elif curr_part != "":
                stack.append(curr_part)
                curr_part = ""
    
        return "/" + "/".join(stack)
