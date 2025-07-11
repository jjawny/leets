# def backtrack(path, choices):
#     if end_condition(path):
#         result.append(path.copy())
#         return
#     for choice in choices:
#         if is_valid(choice, path):
#             # Make choice to path ref
#             path.append(choice)
#             backtrack(path, choices)
#             # Undo choice from path ref (saves mem by mutating ref in place)
#             path.pop()