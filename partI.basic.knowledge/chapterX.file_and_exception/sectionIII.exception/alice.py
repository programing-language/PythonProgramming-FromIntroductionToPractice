fiename = 'alice.txt'

with open(fiename) as f_obj:
    contents = f_obj.read()

"""
Traceback (most recent call last):
  File "/bigdata/git-projects/PythonProgramming-FromIntroductionToPractice/partI.basic.knowledge/chapterX.file_and_exception/sectionIII.exception/alice.py", line 3, in <module>
    with open(fiename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
"""