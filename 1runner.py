# python 1runner.py python 1test.py 0 -- python 1sol.py

from __future__ import print_function
import sys, subprocess, threading

class SubprocessThread(threading.Thread):
  def __init__(self,
               args,
               stdin_pipe=subprocess.PIPE,
               stdout_pipe=subprocess.PIPE,
               stderr_prefix=None):
    threading.Thread.__init__(self)
    self.stderr_prefix = stderr_prefix
    self.p = subprocess.Popen(
        args, stdin=stdin_pipe, stdout=stdout_pipe, stderr=subprocess.PIPE)

  def run(self):
    try:
      self.pipeToStdErr(self.p.stderr)
      self.return_code = self.p.wait()
      self.error_message = None
    except (SystemError, OSError):
      self.return_code = -1
      self.error_message = "The process crashed or produced too much output."

  def pipeToStdErr(self, stream):
    new_line = True
    while True:
      chunk = stream.readline(1024)
      if not chunk:
        return
      chunk = chunk.decode("UTF-8")
      if new_line and self.stderr_prefix:
        chunk = self.stderr_prefix + chunk
        new_line = False
      sys.stderr.write(chunk)
      if chunk.endswith("\n"):
        new_line = True
      sys.stderr.flush()


assert sys.argv.count("--") == 1, (
    "There should be exactly one instance of '--' in the command line.")
sep_index = sys.argv.index("--")
judge_args = sys.argv[1:sep_index]
sol_args = sys.argv[sep_index + 1:]

t_sol = SubprocessThread(sol_args, stderr_prefix="  sol: ")
t_judge = SubprocessThread(
    judge_args,
    stdin_pipe=t_sol.p.stdout,
    stdout_pipe=t_sol.p.stdin,
    stderr_prefix="judge: ")
t_sol.start()
t_judge.start()
t_sol.join()
t_judge.join()

print()
if t_sol.error_message:
  print("Solution error message:", t_sol.error_message)
  exit()

print("Judge return code:", t_judge.return_code)