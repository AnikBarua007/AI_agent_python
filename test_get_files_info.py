from functions.get_files_info import get_files_info
print("Result for current directory:")
test = get_files_info("calculator", ".")
# res = """- main.py: file_size=719 bytes, is_dir=False
# - tests.py: file_size=1331 bytes, is_dir=False
# - pkg: file_size=44 bytes, is_dir=True"""

# if test != res:
#     print("Test failed")
#     print(f"Expected:\n{res}")
#     print(f"Got:\n{test}")
# else:
#     print("Test passed")
print(test)
print("Result for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))
print("Result for '/bin' directory:")
print(get_files_info("calculator", "/bin"))
print("Result for '../' directory:")
print(get_files_info("calculator", "../"))
