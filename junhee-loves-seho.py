from collections.abc import Sequence

from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string('destination', 'output.txt', 'Path to output file.')

# 1MB
CHUNK_SIZE = 1024 * 1024


def main(argv: Sequence[str]) -> None:
  with open(FLAGS.destination, 'w') as f:
    for i in range(1, len(argv)):
      file = argv[i]
      print(f'{file}')
      with open(file) as inf:
        chunk = inf.read(CHUNK_SIZE)
        if i > 1:
          chunk = chunk[1:]
        f.write(chunk)
        while True:
          chunk = inf.read(CHUNK_SIZE)
          if len(chunk) == 0:
            break
          curr_pos = inf.tell()
          next_chunk = inf.read(CHUNK_SIZE)
          inf.seek(curr_pos)
          if len(chunk) < CHUNK_SIZE or len(next_chunk) == 0:
            if i < len(argv) - 1:
              chunk = chunk[:-1] + ','
          f.write(chunk)


if __name__ == '__main__':
  app.run(main)

