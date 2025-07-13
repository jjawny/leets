class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        TIME: Always O(n) because we split the path string and join back
        MEMORY: Always O(n) because we store the parts, which scales matching the input size
        OPTIMIZED: Same Big Os but using split (like join) is written in C and pre-compiled vs iterating to concat (each loop needs to be interpreted on the fly)

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
        parts = path.split("/")
        parts_cleaned = []

        for idx, part in enumerate(parts):
            # print("".join(parts_cleaned))

            # 1. HANDLE PERIODS
            # Ignore if specifying current dir again
            if part == "." or part == "":
                continue
            # Pop previous/parent dir if walking back
            if part == "..":
                if parts_cleaned:
                    parts_cleaned.pop()
                continue
            
            # 2. HANDLE SLASHES
            if part != "/":
                parts_cleaned.append(part)
        return "/" + "/".join(parts_cleaned) # prefix "/" because we lose the inital one during split