class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        TIME: Always O(n) because we split the path string and join back
        MEMORY: Always O(n) because we store the parts, which scales matching the input size

        ##stacks
        """
        # DIGESTING:
        #   - only the standard dots are allowed '.' and '..'
        #   - multiple slashes are squashed to '/'
        #   - must start w a '/' for absolute path
        #   - the file/final portion must not end w a '/' unless root
        #   - TLDR we need to clean a given path based on these rules ^
        #   - We will split the path by the slashes
        
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
        partsCleaned = []

        for idx, part in enumerate(parts):
            print("".join(partsCleaned))

            # 1. HANDLE PERIODS
            # Ignore if specifying current dir again
            if part == "." or part == "":
                continue
            # Pop previous/parent dir if walking back
            if part == "..":
                if partsCleaned:
                    partsCleaned.pop()
                continue
            
            # 2. HANDLE SLASHES
            isPreviouslySlash = partsCleaned and partsCleaned[-1] == "/";
            isLastPart = idx == len(parts) - 1
            if part == "/" and (isPreviouslySlash or isLastPart):
                continue
            
            partsCleaned.append(part)
        return "/" + "/".join(partsCleaned) # prefix "/" because we lose the inital one during split